from presage_physiology_preprocessing import process as video_preprocess
import time
import numpy as np
import json
from json import JSONEncoder


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


vid_path = '/Users/ayaeid/Downloads/test_fail.mov'
DN_SAMPLE = 3
HR_FPS = 10 # float(' inf')

t1 = time.time()
traces = video_preprocess(vid_path, HR_FPS, DN_SAMPLE)
print(f'preprocessing took : {time.time() - t1}s')

with open("/Users/ayaeid/Desktop/test_obj.json", "w") as f:
       json.dump(traces, f, cls=NumpyArrayEncoder)

