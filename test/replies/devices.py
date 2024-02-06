""""Mock replies for the device API"""
MOCK_DEVICE_REPLY = {
    "JsonDeviceResult": {
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
}

MOCK_DEVICE_ACTIVE_REPLY = {
    "JsonDeviceActiveResult": [
        {
            "DeviceCaption": "MAN",
            "DeviceConfig": """Fake config string B""",
            "DeviceFamily": "Position",
            "DeviceID": 10,
            "DeviceName": "Manual position",
            "DevicePID": "MAN",
            "DeviceType": "Manual position",
            "DeviceValidityEnd": None,
            "DeviceValidityStart": "2016-08-05 13:31:28",
            "ProfileID": 1
        },
        {
            "DeviceCaption": "IR",
            "DeviceConfig": "Fake config string C",
            "DeviceFamily": "ThermalCam",
            "DeviceID": 19,
            "DeviceName": "Thermal camera (side linescan)",
            "DevicePID": "IR1",
            "DeviceType": "Infratec 820",
            "DeviceValidityEnd": None,
            "DeviceValidityStart": "2021-04-02 12:02:55",
            "ProfileID": 1
        }
    ]
}

MOCK_DEVICE_PROFILE_REPLY = {
    "JsonDeviceByProfileIDResult": [
        {
            "DeviceCaption": "SC 1",
            "DeviceConfig": """Fake config string D""",
            "DeviceFamily": "Scales",
            "DeviceID": "22",
            "DeviceName": "Scales",
            "DevicePID": "SC1",
            "DeviceType": "Scales 1 position",
            "DeviceValidityEnd": "",
            "DeviceValidityStart": "2016-06-14 17:05:23",
            "ProfileID": 2
        },
        {
            "DeviceCaption": "MAN1",
            "DeviceConfig": """Fake config string E""",
            "DeviceFamily": "Position",
            "DeviceID": "23",
            "DeviceName": "Manual position",
            "DevicePID": "MAN1",
            "DeviceType": "Manual position",
            "DeviceValidityEnd": "",
            "DeviceValidityStart": "2016-08-05 13:31:28",
            "ProfileID": 2
        }
    ]
}
