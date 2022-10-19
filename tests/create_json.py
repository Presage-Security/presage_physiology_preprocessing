import json
import sys
sys.path.append('..')
from presage_physiology_preprocessing import process

vid_path = "test_videos/mobile_example.mp4"
trace = process(vid_path)
with open("mobile_example2.json", "w") as f:
    json.dump(trace, f)
