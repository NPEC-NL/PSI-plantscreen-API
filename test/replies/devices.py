""""Mock replies for the device API"""
MOCK_DEVICE = {
    "DeviceCaption": "RGB 2",
    "DeviceConfig": "Fake config string A",
    "DeviceFamily": "RgbCam",
    "DeviceID": 3,
    "DeviceName": "RGB camera (top)",
    "DevicePID": "RGB2",
    "DeviceType": "PSI 12Mpx",
    "DeviceValidityEnd": None,
    "DeviceValidityStart": "2022-10-11 14:59:08",
    "ProfileID": 1
    }

MOCK_DEVICE_2 = {
    "DeviceCaption": "MAN",
    "DeviceConfig": "Fake config string B",
    "DeviceFamily": "Position",
    "DeviceID": 8,
    "DeviceName": "Manual position",
    "DevicePID": "MAN",
    "DeviceType": "Manual position",
    "DeviceValidityEnd": None,
    "DeviceValidityStart": "2016-08-05 13:31:28",
    "ProfileID": 1
    }

MOCK_DEVICE_REPLY = {"JsonDeviceResult": MOCK_DEVICE}
MOCK_DEVICE_ACTIVE_REPLY = {"JsonDeviceActiveResult": [MOCK_DEVICE, MOCK_DEVICE_2]}
MOCK_DEVICE_PROFILE_REPLY = {"JsonDeviceByProfileIDResult": [MOCK_DEVICE, MOCK_DEVICE_2]}
