# Changelog

<!--next-version-placeholder-->

## v1.2.9 (2024-06-18)

### Fix

* **requirements.py:** Dependency fixes ([`51d812a`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/51d812a7b55176fdf1c5baa4cf502dc2986534e7))

## v1.2.8 (2024-06-10)

### Fix

* **setup.py,requirements.py:** Downgrade to the exact version of numpy that Physiology core is using ([`d4d04d5`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/d4d04d5b25bc10a9d0901b2d947f44dab4c2f516))

## v1.2.7 (2024-06-06)

### Fix

* **setup.py:** Make package versions exact ([`8be7dd4`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/8be7dd4ec316e05eb74e216c03069290bfbb334d))

## v1.2.6 (2024-02-12)

### Fix

* License update to LGPLv3 ([`55aba06`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/55aba0642fb986ad8d85b7bf39fd0116e9b8aa62))

## v1.2.5 (2024-01-23)

### Fix

* January Immediate Security Fixes ([`aec825f`](https://source.presagesecurity.com/presage/developers/presage_physiology_preprocessing/-/commit/aec825ff018d6eb927a5fd24fdd5f2b0fd8deb4b))

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
