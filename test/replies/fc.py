""""Mock replies for the fluorcam API"""
MOCK_FC_IMAGING = {
        "ActionID": 4881,
        "DeviceID": 45,
        "DevicePID": "FC1",
        "ExperimentID": 75,
        "MeasureAngle": 0,
        "MeasureDate": "2021-11-23 22:08:33",
        "MeasureHeight": 500,
        "MeasureID": 70019,
        "RoundID": 3819,
        "TrayBarcode": "35-4__5",
        "TrayID": 4060,
        "TrayProfileID": 25650,
        "ProtocolPath": "2021-11-23FcProtocol_2021-11-23_22-08-32.txt ",
        "TarPath": "2021-11-23Exp-2021-11-23-22-8-32-35-4__5.tar "
    }

MOCK_FC_PARAM_IMAGE = {
        "AnalyseID": 68185,
        "DeviceID": 45,
        "DevicePID": "FC1",
        "ExperimentID": 75,
        "MeasureAngle": 0,
        "MeasureID": 70272,
        "ParameterID": 94,
        "ParameterImagePath": "2021-11-24FcParamImage_2021-11-24_11-04-51.fimg",
        "ParameterName": "Fm_Lss1",
        "RoundID": 3823,
        "TrayBarcode": "11-9__5",
        "TrayID": 3920
    }

MOCK_FC_PLANT_MASK = {
        "DeviceID": 45,
        "DevicePID": "FC1",
        "ExperimentID": 75,
        "MaskIsLeaf": False,
        "MeasureAngle": 0,
        "MeasureDate": "2021-11-24 15:35:02",
        "MeasureID": 70444,
        "PlantMaskPath": """2021-11-24FcPlantMask_2021-11-24_15-15-01.xsel""",
        "RoundID": 3823,
        "TrayBarcode": "24-13__5",
        "TrayID": 3987
    }

MOCK_FC_PARAM = {
    "ParameterID": 10,
    "ParameterName": "Fm_L4",
    "ParameterUnit": "a.u."
}

MOCK_FC_PARAM_2 = {
    "ParameterID": 95,
    "ParameterName": "Fm_Lss2",
    "ParameterUnit": "a.u."
}

MOCK_FC_IMAGING_EXTENDED_DATA = {
        "DeviceID": 10,
        "ExtendedData": "<DataSet> Fake </DataSet>",
        "MeasureDate": "2021-06-17 02:01:54",
        "MeasureID": 14,
        "RoundID": 232,
        "TrayID": 71
    }

MOCK_FC_PLANT_PARAM = {
    "AnalyseID": 68185,
    "DeviceID": 45,
    "DevicePID": "FC1",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureID": 70272,
    "ParameterID": 95,
    "ParameterName": "Fm_Lss2",
    "ParameterValue": 2853.2431300980215,
    "PlantBarcode": "11-9__R3__A3",
    "PlantID": 5451,
    "PlantName": "11-9",
    "RoundID": 3823,
    "TrayArea": "A1",
    "TrayBarcode": "11-9__5",
    "TrayID": 3920
}

MOCK_FC_PLANT_PARAM_2 = {
    "AnalyseID": 9807,
    "DeviceID": 170,
    "DevicePID": "FC1",
    "ExperimentID": 132,
    "MeasureAngle": 0,
    "MeasureID": 10487,
    "ParameterID": 2,
    "ParameterName": "Fo",
    "ParameterValue": 172.07021290625482,
    "PlantBarcode": "Design-12",
    "PlantID": 10585,
    "PlantName": "Design-12",
    "RoundID": 5866,
    "TrayArea": "A4",
    "TrayBarcode": "PS_Tray_408",
    "TrayID": 492
}

MOCK_FC_LEAF_PARAM = {
    "AnalyseID": 107,
    "DeviceID": 1,
    "DevicePID": "FC1",
    "ExperimentID": 2,
    "LeafIndex": 1,
    "MeasureAngle": 0,
    "MeasureID": 114,
    "ParameterID": 5,
    "ParameterName": "QY_max",
    "ParameterValue": 0.7436362189405105,
    "PlantBarcode": "PS_Tray_120",
    "PlantID": 72,
    "PlantName": "IPAP_MA_19",
    "RoundID": 89,
    "TrayArea": "A1",
    "TrayBarcode": "PS_Tray_120",
    "TrayID": 71
}

MOCK_FC_LEAF_PARAM_2 = {
    "AnalyseID": 107,
    "DeviceID": 1,
    "DevicePID": "FC1",
    "ExperimentID": 2,
    "LeafIndex": 2,
    "MeasureAngle": 0,
    "MeasureID": 114,
    "ParameterID": 5,
    "ParameterName": "QY_max",
    "ParameterValue": 0.7415756339312725,
    "PlantBarcode": "PS_Tray_120",
    "PlantID": 72,
    "PlantName": "IPAP_MA_19",
    "RoundID": 89,
    "TrayArea": "A1",
    "TrayBarcode": "PS_Tray_120",
    "TrayID": 71
}

MOCK_FC_IMAGING_MEASURE_REPLY = {"JsonFcImagingByIDResult": MOCK_FC_IMAGING}
MOCK_FC_IMAGING_REPLY = {"JsonFcImagingResult": [MOCK_FC_IMAGING]}
MOCK_FC_IMAGING_EXTENDED_DATA_MEASURE_REPLY = {"JsonFcMeasureExtendedDataByIDResult": MOCK_FC_IMAGING_EXTENDED_DATA}
MOCK_FC_IMAGING_EXTENDED_DATA_REPLY = {"JsonFcMeasureExtendedDataResult": MOCK_FC_IMAGING_EXTENDED_DATA}
MOCK_FC_PLANT_MASK_MEASURE_REPLY = {"JsonFcPlantMaskByMeasureIDResult": MOCK_FC_PLANT_MASK}
MOCK_FC_PLANT_MASK_REPLY = {"JsonFcPlantMaskResult": [MOCK_FC_PLANT_MASK]}
MOCK_FC_PARAM_REPLY = {"JsonFcParamResult": MOCK_FC_PARAM}
MOCK_FC_PARAM_USED_ANALYSE_REPLY = {"JsonFcUsedParamByAnalyseIDResult": [MOCK_FC_PARAM, MOCK_FC_PARAM_2]}
MOCK_FC_PARAM_USED_REPLY = {"JsonFcUsedParamResult": [MOCK_FC_PARAM, MOCK_FC_PARAM_2]}
MOCK_FC_PARAM_IMAGE_ANALYSE_REPLY = {"JsonFcParameterImageByAnalyseIDResult": MOCK_FC_PARAM_IMAGE}
MOCK_FC_PARAM_IMAGE_REPLY = {"JsonFcParameterImageResult": [MOCK_FC_PARAM_IMAGE]}
MOCK_FC_PLANT_PARAM_ANALYSE_REPLY = {"JsonFcPlantParamByAnalyseIDResult": [MOCK_FC_PLANT_PARAM]}
MOCK_FC_PLANT_PARAM_REPLY = {"JsonFcPlantParamResult": [MOCK_FC_PLANT_PARAM, MOCK_FC_PLANT_PARAM_2]}
MOCK_FC_LEAF_PARAM_ANALYSE_REPLY = {"JsonFcLeafParamByAnalyseIDResult": [MOCK_FC_LEAF_PARAM, MOCK_FC_LEAF_PARAM_2]}
MOCK_FC_LEAF_PARAM_REPLY = {"JsonFcLeafParamResult": [MOCK_FC_LEAF_PARAM, MOCK_FC_LEAF_PARAM_2]}
