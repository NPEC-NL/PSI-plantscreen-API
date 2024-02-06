""""Mock replies for the device API"""
MOCK_DEVICE_REPLY = {
    "JsonDeviceResult": {
        "Config": """<?xml version="1.0" encoding="utf-8"?> \
   <Configuration> <WindowingMode>1</WindowingMode> \
   <ExtractLines>1</ExtractLines> <Focus>10508</Focus>\
   <Width>640</Width> <Height>710</Height> \
   <DefaultZ>0</DefaultZ> \
   <MaskCenterX>308</MaskCenterX> \
   <MaskCenterY>637</MaskCenterY> \
   <Barrel>-0.04</Barrel> \
   <MaskRotation>0.0</MaskRotation> \
   <ZConversion>1367</ZConversion> \
   <RatioCoefficient>0.00123869</RatioCoefficient> \
   <BackwardFEC>true</BackwardFEC> \
   <FixedX>false</FixedX> \
   <FixedXPxMmRatio>0</FixedXPxMmRatio> <FixedY>true</\
   FixedY> \
   <FixedYPxMmRatio>0.564726962</FixedYPxMmRatio> \
   <CenterShift> <Item> <Z>0</Z> <XShift>0</XShift> \
   <YShift>0</YShift> </Item> </CenterShift> \
   <ScanLines>710</ScanLines> \
   <PositionStart>1300</PositionStart> \
   <PositionEnd>0</PositionEnd> \
   <ScanSpeed>1770</ScanSpeed> \
   <MoveSpeed>1700</MoveSpeed> <ScanAxis>Z</ScanAxis>\
   <HeatingTempDiff>8.0</HeatingTempDiff> \
   <HeatingTime>1200</HeatingTime> </Configuration>""",
        "DeviceCaption": "IR",
        "DeviceFamily": "ThermalCam",
        "DeviceID": "41",
        "DeviceName": "Thermal camera (side linescan)",
        "DevicePID": "IR1",
        "DeviceType": "FLIR A615",
        "ProfileID": 1,
        "ValidityEnd": "2020-05-05 13:35:41",
        "ValidityStart": "2020-04-22 16:23:57"
    }
}

MOCK_DEVICE_ACTIVE_REPLY = {
    "JsonDeviceActiveResult": [
        {
            "DeviceCaption": "MAN",
            "DeviceConfig": """<?xml version="1.0" encoding="utf-8" ?> <Configuration/>""",
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
            "DeviceConfig": """<?xml version="1.0" encoding="utf-8"?> <Configuration> \
                                <WindowingMode>0</WindowingMode> \
                                <ExtractLines>1</ExtractLines> <Focus>86</Focus> \
                                <Width>1024</Width> <Height>620</Height> \
                                <DefaultZ>0</DefaultZ> \
                                <MaskCenterX>526</MaskCenterX> \
                                <MaskCenterY>601</MaskCenterY> \
                                <Barrel>-0.15</Barrel> \
                                <MaskRotation>0.0</MaskRotation> <ZConversion>630</\
                                ZConversion> \
                                <RatioCoefficient>0.00115742</RatioCoefficient> \
                                <BackwardFEC>true</BackwardFEC> \
                                <FixedX>false</FixedX> \
                                <FixedXPxMmRatio>0</FixedXPxMmRatio> <FixedY>true</\
                                FixedY> \
                                <FixedYPxMmRatio>0.933333333</FixedYPxMmRatio> \
                                <CenterShift> <Item> <Z>0</Z> <XShift>0</XShift> \
                                <YShift>0</YShift> </Item> </CenterShift> \
                                <ScanLines>620</ScanLines> \
                                <PositionStart>885</PositionStart> \
                                <PositionEnd>220</PositionEnd> \
                                <ScanSpeed>325</ScanSpeed> \
                                <MoveSpeed>1300</MoveSpeed> <ScanAxis>Z</ScanAxis> \
                                <HeatingTempDiff>6.0</HeatingTempDiff> \
                                <HeatingTime>1200</HeatingTime> </Configuration>""",
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
            "DeviceConfig": """<?xml version="1.0" encoding="utf-8" ?> <Configuration> \
                                <Row>1</Row> <SU name="1"/> </Configuration>""",
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
            "DeviceConfig": """<?xml version="1.0" encoding="utf-8" ?> <Configuration/>""",
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
