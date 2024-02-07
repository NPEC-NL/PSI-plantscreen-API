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

MOCK_PROFILE_REPLY = {
    "JsonSystemProfileResult": {
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
}

MOCK_PROFILE_ACTIVE_REPLY = {
    "JsonSystemProfileActiveResult": {
        "ProfileActive": True,
        "ProfileID": 1,
        "ProfileInfo": "",
        "ProfileName": "PSI_Large",
        "SystemHwConfig": """<?xml version="1.0" \
                            encoding="utf-8" ?> <Configuration> <TrayStack> \
                            <RowCount>9</RowCount> <RowCapacity>30</RowCapacity>\
                            </TrayStack> <AdaptChamber>true</AdaptChamber> \
                            <HeightMeasurement>true</HeightMeasurement> \
                            <Commands> <SetLight>true</SetLight> \
                            <TrayLoad>true</TrayLoad> <TraySwap>true</TraySwap> \
                            <TrayUnload>false</TrayUnload> \
                            <Measure>true</Measure> </Commands> <Lights> <Light \
                            caption="White">LightMain1</Light> <Light \
                            caption="Red">LightMain2</Light> <Light \
                            caption="IR">LightMain3</Light> </Lights> <Pids> \
                            <PID name="MAN1" caption="MAN1"/> <PID name="FC1" \
                            caption="FC1"> <AxisZ>true</AxisZ> <View>Top</View> \
                            </PID> <PID name="IR1" caption="IR1 (Side)"> \
                            <Turntable>false</Turntable> <AxisZ \
                            heightVisible="false">true</AxisZ> <View>Side</View>\
                            </PID> <PID name="SC1" caption="SC 1"> </PID> <PID \
                            name="MAN2" caption="MAN2"/> </Pids> <Analyse> \
                            <MaskErosionLevel>1</MaskErosionLevel> <IR1> \
                            <PlantMask> \
                            <AutomaticThreshold>true</AutomaticThreshold> \
                            <ManThresholdValue>20.0</ManThresholdValue> \
                            <AutoThresholdShift>0.0</AutoThresholdShift> \
                            <MinObjectSize>0</MinObjectSize> \
                            <UseRgb>false</UseRgb> </PlantMask> <Parameters> \
                            <Parameter>Temp:S1</Parameter> </Parameters> \
                            <Values> \
                            <MinValidPixelsPercentage>0</MinValidPixelsPercentag\
                            e> </Values> </IR1></Analyse> </Configuration>"""
    }
}
