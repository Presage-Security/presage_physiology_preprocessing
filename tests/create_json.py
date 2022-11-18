import json
import sys
sys.path.append('..')
from presage_physiology_preprocessing import process

vid_path = "test_videos/mobile_example.mp4"
# vid_path = "/Users/rick/Desktop/test_videos/vid_aya_15x30bpm.avi"
trace = process(vid_path)
with open("test_traces/mobile_example.json", "w") as f:
    json.dump(trace, f)
