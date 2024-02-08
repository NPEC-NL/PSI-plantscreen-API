""""Mock replies for the profile API"""
MOCK_PROFILE_ID_REPLY = {
    "JsonSystemProfileIDResult": [
        {
            "ProfileID": 1
        },
        {
            "ProfileID": 3
        }
    ]
}

MOCK_PROFILE_BASE = {
    "ProfileActive": False,
    "ProfileID": 4,
    "ProfileInfo": "Only RGBM for 3D reconstruction",
    "ProfileName": "PSI_Large_RGB Multi",
    "SystemHwConfig": """<?xml version="1.0" \
                        encoding="utf-8" ?> <Configuration> <TrayStack> \
                        <RowCount>9</RowCount> \
                        <RowCapacity>30</RowCapacity> </TrayStack> \
                        <AdaptChamber>true</AdaptChamber> \
                        <HeightMeasurement>true</HeightMeasurement> \
                        <Commands> <SetLight>true</SetLight> \
                        <TrayLoad>true</TrayLoad> <TraySwap>true</TraySwap>\
                        <TrayUnload>false</TrayUnload> \
                        <Measure>true</Measure> </Commands> <Lights> <Light\
                        caption="Load">LightLoad</Light> <Light \
                        caption="White">LightMain1</Light> <Light \
                        caption="Red">LightMain2</Light> <Light \
                        caption="IR">LightMain3</Light> </Lights> <Pids> \
                        <PID name="RGBM" caption="RGBM"> <View>Side</View> \
                        <Turntable>true</Turntable> <AxisZ \
                        heightVisible="false">true</AxisZ> </PID> </Pids> \
                        <Analyse> </Analyse> </Configuration>"""
    }

MOCK_PROFILE_REPLY = {"JsonSystemProfileResult": MOCK_PROFILE_BASE}

MOCK_PROFILE_ACTIVE_REPLY = {"JsonSystemProfileActiveResult": MOCK_PROFILE_BASE}
