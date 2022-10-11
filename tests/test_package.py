import sys
sys.path.append('..')
from presage_physiology_preprocessing import process
import unittest

vid_path = "test_videos/mobile_example.mp4"

class DefaultFunctionsTest(unittest.TestCase):

    def test_return(self):
        output = process(vid_path)
        print(output.keys())

if __name__ == '__main__':
    unittest.main()
