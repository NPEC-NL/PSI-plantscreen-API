""""Mock replies for the Thermal API"""
MOCK_IR_IMAGE = {
    "ActionID": 4845,
    "DeviceID": 44,
    "DevicePID": "IR1",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureDate": "2021-11-25 14:35:51",
    "MeasureHeight": 0,
    "MeasureID": 53948,
    "RoundID": 3826,
    "TrayBarcode": "27-15__5",
    "TrayID": 4015,
    "TrayProfileID": 25605,
    "ImagePath": r"""2021-11-25\IrRawFrame_2021-11-25_14-35-50.raw"""
}

MOCK_IR_EXTENDED = {
    "DeviceID": 5,
    "ExtendedData": """<DataSet> <Item name="latitude" \
                    type="double" unit="degree">49.33952739</Item> \
                    <Item name="longitude" type="double" \
                    unit="degree">16.47612696</Item> <Item \
                    name="distanceToWantedPoint" type="double" \
                    unit="meters">0.09</Item> <Item name="speed" \
                    type="double" unit="km/h">1.7</Item> </DataSet>""",
    "MeasureDate": "2021-09-23 10:09:21",
    "MeasureID": 166,
    "RoundID": 240,
    "TrayID": 248
}

MOCK_IR_MASK = {
    "DeviceID": 44,
    "DevicePID": "IR1",
    "ExperimentID": 75,
    "MaskIsLeaf": False,
    "MeasureAngle": 0,
    "MeasureDate": "2021-11-25 14:35:51",
    "MeasureID": 53948,
    "PlantMaskPath": r"""2021-11-25\IrMask_2021-11-25_14-35-50.xsel""",
    "RoundID": 3826,
    "TrayBarcode": "27-15__5",
    "TrayID": 4015
}

MOCK_IR_PARAM = {
    "ParameterID": 5,
    "ParameterName": "Temp4",
    "ParameterUnit": "a.u."
}

MOCK_IR_PARAM_2 = {
    "ParameterID": 6,
    "ParameterName": "Size",
    "ParameterUnit": ""
}

MOCK_IR_PLANT = {
    "AnalyseID": 53424,
    "DeviceID": 44,
    "DevicePID": "IR1",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureID": 54052,
    "ParameterAvg": 1385.9840087890625,
    "ParameterID": 1,
    "ParameterMax": 1385.9840087890625,
    "ParameterMedian": 1385.9840087890625,
    "ParameterMin": 1385.9840087890625,
    "ParameterName": "T-Size",
    "ParameterStddev": 0,
    "PlantBarcode": "26-5__R3__A3",
    "PlantID": 5505,
    "PlantName": "26-5",
    "RoundID": 3826,
    "TrayArea": "A1",
    "TrayBarcode": "26-5__5",
    "TrayID": 4010
}

MOCK_IR_LEAF = {
    "AnalyseID": 6211,
    "DeviceID": 163,
    "DevicePID": "IR1",
    "ExperimentID": 36,
    "LeafIndex": 3,
    "MeasureAngle": 0,
    "MeasureID": 7433,
    "ParameterAvg": 20.55652618408203,
    "ParameterID": 1,
    "ParameterMax": 22.08148193359375,
    "ParameterMedian": 20.407989501953125,
    "ParameterMin": 24.22625732421875,
    "ParameterName": "Temp",
    "ParameterStddev": 0.45809194445610046,
    "PlantBarcode": "Plant136",
    "PlantID": 9490,
    "PlantName": "Plant136",
    "RoundID": 5356,
    "TrayArea": "D1",
    "TrayBarcode": "PS_Tray_312",
    "TrayID": 41
}

MOCK_IR_LEAF_2 = {
    "AnalyseID": 6211,
    "DeviceID": 163,
    "DevicePID": "IR1",
    "ExperimentID": 36,
    "LeafIndex": 4,
    "MeasureAngle": 0,
    "MeasureID": 7433,
    "ParameterAvg": 20.650304794311523,
    "ParameterID": 1,
    "ParameterMax": 21.952789306640625,
    "ParameterMedian": 20.4951171875,
    "ParameterMin": 20.046173095703125,
    "ParameterName": "Temp",
    "ParameterStddev": 0.423615425825119,
    "PlantBarcode": "Plant136",
    "PlantID": 9490,
    "PlantName": "Plant136",
    "RoundID": 5356,
    "TrayArea": "D1",
    "TrayBarcode": "PS_Tray_312",
    "TrayID": 41
}

MOCK_IR_IMAGING_MEASURE_REPLY = {"JsonIrImagingByIDResult": MOCK_IR_IMAGE}
MOCK_IR_IMAGING_REPLY = {"JsonIrImagingResult": [MOCK_IR_IMAGE]}
MOCK_IR_IMAGING_EXTENDED_DATA_MEASURE_REPLY = {"JsonIrMeasureExtendedDataByIDResult": MOCK_IR_EXTENDED}
MOCK_IR_IMAGING_EXTENDED_DATA_REPLY = {"JsonIrMeasureExtendedDataResult": MOCK_IR_EXTENDED}
MOCK_IR_PLANT_MASK_MEASURE_REPLY = {"JsonIrPlantMaskByMeasureIDResult": MOCK_IR_MASK}
MOCK_IR_PLANT_MASK_REPLY = {"JsonIrPlantMaskResult": [MOCK_IR_MASK]}
MOCK_IR_PLANT_MASK_IMAGE_MEASURE_REPLY = {"JsonIrPlantMaskImageByMeasureIDResult": MOCK_IR_IMAGE}
MOCK_IR_PLANT_MASK_IMAGE_REPLY = {"JsonIrPlantMaskImageResult": [MOCK_IR_IMAGE]}
MOCK_IR_PARAM_REPLY = {"JsonIrParamResult": MOCK_IR_PARAM}
MOCK_IR_PARAM_USED_ANALYSE_REPLY = {"JsonIrUsedParamByAnalyseIDResult": [MOCK_IR_PARAM, MOCK_IR_PARAM_2]}
MOCK_IR_PARAM_USED_REPLY = {"JsonIrUsedParamResult": [MOCK_IR_PARAM, MOCK_IR_PARAM_2]}
MOCK_IR_PLANT_PARAM_ANALYSE_REPLY = {"JsonIrPlantParamByAnalyseIDResult": [MOCK_IR_PLANT]}
MOCK_IR_PLANT_PARAM_REPLY = {"JsonIrPlantParamResult": [MOCK_IR_PLANT]}
MOCK_IR_LEAF_PARAM_ANALYSE_REPLY = {"JsonIrLeafParamByAnalyseIDResult": [MOCK_IR_LEAF, MOCK_IR_LEAF_2]}
MOCK_IR_LEAF_PARAM_REPLY = {"JsonIrLeafParamResult": [MOCK_IR_LEAF, MOCK_IR_LEAF_2]}
