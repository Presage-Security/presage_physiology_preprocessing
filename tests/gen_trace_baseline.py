import sys
sys.path.append('..')
import os
import boto3
import cv2
import time
import shutil
import json
from importlib.metadata import version
from boto3.dynamodb.conditions import Attr, Key
from presage_physiology_preprocessing import process

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
s3 = boto3.resource('s3', region_name="us-east-1")
wpu_table = dynamodb.Table("wpu-trial-data")


def pull_dynamo(person_id, sk=None):
    if sk:
        response = wpu_table.get_item(Key={'id': person_id, 'event': sk})
    else:
        response = wpu_table.query(
            KeyConditionExpression=Key('id').eq(person_id) & Key('event').gte(0))
    return response


def download_video(s3path, save_name, save_path="test_videos"):
    """
    Get videos and data from dynamo for an ID
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    # Download Video
    if not os.path.exists(save_name):
        print("Downloading video", save_name)
        s3.Bucket("presage-wpu-trial-data").download_file(s3path, save_name)
    return save_name


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        print(e)


def wpu_trace_generation():

    # AWS saving to:
    aws_base_dir = 'Physiology/baseline'
    aws_trace_dir = os.path.join(aws_base_dir, "traces")
    aws_meta_txt = os.path.join(aws_base_dir, "meta_traces.txt")

    # local temporary files (to be removed afterwards)
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    trace_temp = os.path.join(temp_dir, 'trace.json')
    meta_temp = os.path.join(temp_dir, 'meta_traces.txt')

    test_ids = [36, 112, 275,  # great hr and great rr
                41, 319, 331,  # great hr, terrible rr
                66, 314, 272,  # terrible hr, great rr
                84, 57, 63,  # terrible hr, terrible hr
                58, 250, 38, 109]  # medium hr, medium rr

    # iterate through all ids
    for person_id in test_ids:
        try:
            # first we get masimo data
            pid = str(person_id).zfill(4)
            meta_row = pull_dynamo(pid, -1)  # gets list of files in direcotry
            if 'Item' not in meta_row:
                print(pid, "Does not exist in table. Skipping.")
                continue
            meta_row = meta_row["Item"]
            file_paths = [meta_row.get("Clipped_Location", None)]

            for file in file_paths:
                if file:
                    # download file from aws
                    print(f"run_accuracy_baseline: Analyzing file: {file}")
                    vid_path = download_video(file.lstrip("s3://presage-wpu-trial-data/"),
                                              os.path.join(temp_dir, pid + "." + file.split(".")[-1]), temp_dir)

                    # Compute trace and vitals
                    print(f'Processing trace for: {vid_path}')
                    trace = process(vid_path)

                    # save traces to temp json
                    print(f'Saving patient: {person_id} to temporary json {trace_temp}')
                    with open(trace_temp, "w") as f:
                        json.dump(trace, f)

                    # upload json trace to AWS
                    print(f"Uploading patient: {person_id} traces json to s3 at: {aws_trace_dir}...")
                    upload_file(trace_temp, "presage-project-files",
                                object_name=os.path.join(aws_trace_dir, '{}_trace.json'.format(person_id)))
                    print("Uploads completed")

                    # Clean up
                    try:
                        os.remove(vid_path)
                        os.remove(trace_temp)
                    except Exception as ex:
                        pass

        except Exception as ex:
            print(ex)
            continue

    # upload meta data text file to AWS
    timestr = time.strftime("%Y%m%dT%H%M%S")
    v = version("presage_physiology_preprocessing")
    f = open(meta_temp, "a")
    f.write("\nTrace baseline created on: " + timestr)
    f.write("\nPresage_physiology_preprocessing version: " + v)
    f.close()

    # upload csv to AWS
    upload_file(meta_temp, "presage-project-files", object_name=aws_meta_txt)

    # clean up local stuff
    try:
        os.remove(meta_temp)
        shutil.rmtree(temp_dir)
    except OSError as e:
        print("Error: %s : %s" % (temp_dir, e.strerror))


if __name__ == '__main__':
    wpu_trace_generation()
