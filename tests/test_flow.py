import sys
sys.path.append('..')
from presage_physiology_preprocessing import process
import presage_physiology
import unittest

vid_path = "test_videos/mobile_example.mp4"
trace = process(vid_path)
class DefaultFunctionsTest(unittest.TestCase):
    def test_get_hr_rr(self):
        hr, rr = presage_physiology.get_hr_rr(trace=trace)
        print(hr, rr)
    def test_get_hr(self):
        hr = presage_physiology.get_hr(trace=trace)
        print(hr)
    def test_get_rr(self):
        rr = presage_physiology.get_rr(trace=trace)
        print(rr)
    def test_get_all(self):
        hr, rr, so2 = presage_physiology.get_all(trace=trace)
        print(hr, rr, so2)

if __name__ == '__main__':
    unittest.main()
