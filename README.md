# presage_physiology_preprocessing

**The information contained in this Python helper, API, or data responses as expected from normal usage of the data should not be used to diagnose, treat, or prevent any disease or illness whether directly or indirectly. This is for informational and research purposes only.**

A Python helper packages for preprocessing video prior to uploading to Presage Technologies' APIs. [Presage Technologies](https://presagetechnologies.com)

## General

Helper package for [Physiology API](https://physiology.presagetech.com)
Please refer to our [documentation](https://docs.physiology.presagetech.com) for API usage.

## Installation

All of the below is pre-implemented in the [presage_technologies python client](https://github.com/Presage-Security/presage_technologies). This package is only needed for very specific usecases. Installation for the package can be done via `pip`:

```bash
$ pip install presage_physiology_preprocessing
```

## Preprocessing Usage


After installation, import the client class into your project and initialize with the API key:

```python
from presage_physiology_preprocessing import process
data_dict = process("/path/to/video/file")
```

Process return a dictionary, denoted as `data_dict` above to upload your preprocessed object to the Physiology API.


## Limitations

In order to ensure best performance, we recommend that the videos you process meet the following conditions.  Within a 20 second window, it is ideal if there is a single foremost subject in view.  That subject's gaze is mostly unchanged and looking in the general direction of the acquiring camera. The subject’s face, shoulders and chest should be visible.  Well-lit, uniformly-lit, and consistently-lit environments will also ensure optimal performance.  Videos must be acquired at frame rates greater than 10 frames per second.


#### Video format

The current API requires that input videos have a standard, RGB color encoding.  We ensure support for the following formats: AVI, MOV and MP4.

#### ISO/Exposure/Gain

Some cameras automatically adjust exposure time, gain, ISO or f/stop in order to optimize image brightness.  This can be problematic for Presage Vitals if said values vary dramatically. While Presage can deal with varying lighting changes in the recording environment, rapid lighting changes can cause ISO, gain, and exposure to vary significantly and be problematic for proper vital extraction. For optimal results, ensure the recording device is not performing rapid ISO/exposure/gain adjustments or keep the scene illumination relative constant.

#### Distance

Presage technology can measure vitals for a large degree of subject to camera distance.  It only requires that there are at least approximately 100 camera pixels across the face and that said face is in focus.  For a 12 megapixel camera, this is approximately 3-5% of the total width of the image.

Extreme imaging distances in atmospheric conditions that display visible scintillation in recorded videos can cause errors in the vital extraction.

#### Lighting
While Presage can deal with monochromatic visible light sources for illumination, broadband light sources covering the entire visible spectrum are ideal.

Scene illumination should not be too dark or too bright. Ensure the average recorded pixel intensity of the subject's face is above 30% of the dynamic range of the recording device without gain being applied. Also, ensure the pixels corresponding to the subject's face are not saturated. Video recorded not following these lighting guidelines could result in no vitals being obtained.


#### Motion
_Camera motion_

Although we expect to handle camera motion in the future, currently large degrees of camera motion will severely impact the ability to generate respiration rate and may impact heart rate output.  For optimal results, maintain a fairly still camera position during each 20 second window in which vital measurements are desired.

_Subject motion_

Similar to camera motion, we have found that subject motion can degrade the ability to reliably generate a respiratory rate measurement and to a lesser degree, a heart rate measurement.  It takes approximately 10 seconds of video with a stationary subject before a new vital measurement is returned. If a subject moves their head significantly, that counter resets.  We recommend the subject remains still, with their gaze pointed towards the acquiring camera. The subject should also refrain from talking as this leads to errors in respiration rate measurements.
