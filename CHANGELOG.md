# Changelog

<!--next-version-placeholder-->

## v1.2.4 (2023-11-29)

### Fix

* Missed one ([`c7f90f5`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/c7f90f542ceef6f0d6469d7d529125068439ef9b))
* Vulnerable dependency updates ([`24ca2f5`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/24ca2f511832fa63cd755bbd8a85e006c9975dbf))

## v1.2.3 (2023-07-13)

### Fix

* Minor bug fix to ensure RR works correctly on downsampled images.  Using OpenCV 4.5 and HR_FPS=30 by default ([`2abedbc`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/2abedbc32c429771eb8179478972e5ddf0eee757))

## v1.2.2 (2023-07-11)

### Fix

* **rr:** Minor bug fixes to ensure RR works correct iwth downsampled images.  Using OpenCV 4.5. and HR_FPS=30 as default ([`fe02e3d`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/fe02e3d6e0e1f577bdc90cfcb171e98b08d89508))

## v1.2.1 (2022-12-21)
### Fix
* Forcing version rebuild to handle CI/CD changes ([`0c75de5`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/0c75de516596cecbb1cd14c438fb641d51a13d4b))

## v1.2.0 (2022-12-20)
### Feature
* **core:** Changed preprocessing format to a list instead of a dictionary to support continuous reading mode without repetitive data transforms. ([`022b52b`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/022b52b84d741f3f7e140b6af236fec94429c91a))

## v1.1.0 (2022-11-03)
### Feature
* **core:** Import version number at init to access at top level ([`98ced0b`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/98ced0b594b6d9742a03917c40c4120f9cf13e8a))

## v1.0.7 (2022-11-03)
### Fix
* **core:** Set bgr floats to round to 8 decimal places in hopes to fix float point precision across multiple machines. ([`9ae399d`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/9ae399d7c864194a6992ff0ca83e8c9aeffb669f))

## v1.0.6 (2022-10-27)
### Fix
* **core:** Fixed error where python versions below 3.8 could not correct get the version number of the package ([`f924d58`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/f924d581b2ef79aa7ecea0f0e296bdc2484ad121))

## v1.0.5 (2022-10-26)
### Fix
* Mediapipe initialization bug, semantic release implementation ([`3ad8070`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/3ad8070853d661a9e8e0e649c3cd0dd27c3a9dbe))
