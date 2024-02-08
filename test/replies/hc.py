""""Mock replies for the Hyperspectral API"""
MOCK_HC_IMAGING = {
    "ActionID": 4858,
    "DeviceID": 46,
    "DevicePID": "VNIR",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureDate": "2021-11-21 15:32:16",
    "MeasureHeight": 9330,
    "MeasureID": 25229,
    "RoundID": 3810,
    "TrayBarcode": "11-15__5",
    "TrayID": 3915,
    "TrayProfileID": 25506,
    "CalibrationDarkContentPath": r"""2021-11-21\2021-11-21--15-31-06_round-0_cam-1_calibFrame.bil""",
    "CalibrationDarkHeaderPath": r"""2021-11-21\2021-11-21--15-31-06_round-0_cam-1_calibFrame.hdr""",
    "CalibrationWhiteContentPath": r"""2021-11-21\2021-11-21--15-31-08_round-0_cam-1_calibFrame.bil""",
    "CalibrationWhiteHeaderPath": r"""2021-11-21\2021-11-21--15-31-08_round-0_cam-1_calibFrame.hdr""",
    "DataContentPath": r"""2021-11-21\2021-11-21--15-32-16_round-0_cam-1_tray-11-15__5.bil""",
    "DataHeaderPath": r"""2021-11-21\2021-11-21--15-32-16_round-0_cam-1_tray-11-15__5.hdr"""
}

MOCK_HC_DATA = {
    "DeviceID": 7,
    "ExtendedData": """<DataSet> <Item name="gain" \
                    type="int" unit="a.u.">236</Item> <Item \
                    name="latitude" type="double" \
                    unit="degree">49.33953033</Item> <Item \
                    name="longitude" type="double" \
                    unit="degree">16.47612798</Item> <Item \
                    name="distanceToWantedPoint" type="double" \
                    unit="meters">0.25</Item> <Item name="speed" \
                    type="double" unit="km/h">1.7</Item> </DataSet>""",
    "MeasureDate": "2021-09-23 10:09:20",
    "MeasureID": 673,
    "RoundID": 240,
    "TrayID": 248
}

MOCK_HC_RGB_IMAGE = {
    "DeviceID": 46,
    "DevicePID": "VNIR",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureID": 25229,
    "RgbImagePath": """2021-11-21\2021-11-21_15-32-16.png""",
    "RoundID": 3810,
    "TrayBarcode": "11-15__5",
    "TrayID": 3915
}

MOCK_HC_PLANT_MASK = {
    "DeviceID": 46,
    "DevicePID": "VNIR",
    "ExperimentID": 75,
    "MaskIsLeaf": False,
    "MeasureAngle": 0,
    "MeasureDate": "2021-11-21 15:35:16",
    "MeasureID": 25229,
    "PlantMaskPath": r"""2021-11-21\HcMask_2021-11-21_15-32-16.xsel""",
    "RoundID": 3810,
    "TrayBarcode": "11-15__5",
    "TrayID": 3915
}

MOCK_HC_PARAM = {
    "ParameterID": 1,
    "ParameterName": "PRI",
    "ParameterUnit": ""
}

MOCK_HC_PARAM_2 = {
    "ParameterID": 2,
    "ParameterName": "NDVI2",
    "ParameterUnit": ""
}


MOCK_HC_PARAM_IMAGE = {
    "AnalyseID": 18281,
    "DeviceID": 46,
    "DevicePID": "VNIR",
    "ExperimentID": 75,
    "MeasureAngle": 0,
    "MeasureID": 24959,
    "ParameterID": 7,
    "ParameterImagePath": r"""2021-11-14\HcParamImage_2021-11-14_15-32-01_6.fimg""",
    "ParameterName": "OSAVI",
    "RoundID": 3781,
    "TrayBarcode": "25-13__5",
    "TrayID": 4000
}

MOCK_HC_PLANT_PARAM = {
            "AnalyseID": 2230,
            "DeviceID": 168,
            "DevicePID": "VNIR",
            "ExperimentID": 142,
            "MeasureAngle": 0,
            "MeasureID": 2651,
            "ParameterAvg": -0.07001832420636284,
            "ParameterID": 4,
            "ParameterMax": 0.031234258798663303,
            "ParameterMedian": -0.07626538668603312,
            "ParameterMin": -0.11145615220384669,
            "ParameterName": "PSRI",
            "ParameterStddev": 0.03058898391667995,
            "PlantBarcode": "IceBerg-11-Bl",
            "PlantID": 10728,
            "PlantName": "IceBerg-11-Bl",
            "RoundID": 5811,
            "TrayArea": "A1",
            "TrayBarcode": "PS_Tray_364",
            "TrayID": 93
}

MOCK_HC_PLANT_PARAM_2 = {
            "AnalyseID": 2230,
            "DeviceID": 168,
            "DevicePID": "VNIR",
            "ExperimentID": 142,
            "MeasureAngle": 0,
            "MeasureID": 2651,
            "ParameterAvg": -0.06134910801895601,
            "ParameterID": 4,
            "ParameterMax": -0.007699479732845969,
            "ParameterMedian": -0.060640355892126394,
            "ParameterMin": -0.1547312562342659,
            "ParameterName": "PSRI",
            "ParameterStddev": 0.01823760747936414,
            "PlantBarcode": "Design-9-Bl",
            "PlantID": 10729,
            "PlantName": "Design-9-Bl",
            "RoundID": 5811,
            "TrayArea": "A5",
            "TrayBarcode": "PS_Tray_364",
            "TrayID": 93
}

MOCK_HC_LEAF_PARAM = {
    "AnalyseID": 10,
    "DeviceID": 8,
    "DevicePID": "VNIR",
    "ExperimentID": 2,
    "LeafIndex": 1,
    "MeasureAngle": 0,
    "MeasureID": 14,
    "ParameterAvg": 0.10160069498823517,
    "ParameterID": 6,
    "ParameterMax": 0.18943101587918962,
    "ParameterMedian": 0.07506238796096608,
    "ParameterMin": 0.028485006833620045,
    "ParameterName": "MCARI1",
    "ParameterStddev": 0.052060799122892354,
    "PlantBarcode": "PS_Tray_120",
    "PlantID": 72,
    "PlantName": "IPAP_MA_19",
    "RoundID": 89,
    "TrayArea": "A1",
    "TrayBarcode": "PS_Tray_120",
    "TrayID": 71
}

MOCK_HC_LEAF_PARAM_2 = {
    "AnalyseID": 10,
    "DeviceID": 8,
    "DevicePID": "VNIR",
    "ExperimentID": 2,
    "LeafIndex": 2,
    "MeasureAngle": 0,
    "MeasureID": 14,
    "ParameterAvg": 0.2312990914821672,
    "ParameterID": 6,
    "ParameterMax": 0.5477579569460691,
    "ParameterMedian": 0.2226733140697425,
    "ParameterMin": 0.014776641743017335,
    "ParameterName": "MCARI1",
    "ParameterStddev": 0.11508643635455965,
    "PlantBarcode": "PS_Tray_120",
    "PlantID": 72,
    "PlantName": "IPAP_MA_19",
    "RoundID": 89,
    "TrayArea": "A1",
    "TrayBarcode": "PS_Tray_120",
    "TrayID": 71
}

MOCK_HC_IMAGING_MEASURE_REPLY = {"JsonHcImagingByIDResult": MOCK_HC_IMAGING}
MOCK_HC_IMAGING_REPLY = {"JsonHcImagingResult": [MOCK_HC_IMAGING]}
MOCK_HC_IMAGING_EXTENDED_DATA_MEASURE_REPLY = {"JsonHcMeasureExtendedDataByIDResult": MOCK_HC_DATA}
MOCK_HC_IMAGING_EXTENDED_DATA_REPLY = {"JsonHcMeasureExtendedDataResult": MOCK_HC_DATA}
MOCK_HC_RGB_IMAGE_MEASURE_REPLY = {"JsonHcRgbImageByMeasureIDResult": MOCK_HC_RGB_IMAGE}
MOCK_HC_RGB_IMAGE_REPLY = {"JsonHcRgbImageResult": [MOCK_HC_RGB_IMAGE]}
MOCK_HC_PLANT_MASK_MEASURE_REPLY = {"JsonHcPlantMaskByMeasureIDResult": MOCK_HC_PLANT_MASK}
MOCK_HC_PLANT_MASK_REPLY = {"JsonHcPlantMaskResult": [MOCK_HC_PLANT_MASK]}
MOCK_HC_PARAM_REPLY = {"JsonHcParamResult": MOCK_HC_PARAM}
MOCK_HC_PARAM_USED_ANALYSE_REPLY = {"JsonHcUsedParamByAnalyseIDResult": [MOCK_HC_PARAM]}
MOCK_HC_PARAM_USED_REPLY = {"JsonHcUsedParamResult": [MOCK_HC_PARAM, MOCK_HC_PARAM_2]}
MOCK_HC_PARAM_IMAGE_ANALYSE_REPLY = {"JsonHcParameterImageByAnalyseIDResult": MOCK_HC_PARAM_IMAGE}
MOCK_HC_PARAM_IMAGE_REPLY = {"JsonHcParameterImageResult": [MOCK_HC_PARAM_IMAGE]}
MOCK_HC_PLANT_PARAM_ANALYSE_REPLY = {"JsonHcPlantParamByAnalyseIDResult": [MOCK_HC_PLANT_PARAM]}
MOCK_HC_PLANT_PARAM_REPLY = {"JsonHcPlantParamResult": [MOCK_HC_PLANT_PARAM, MOCK_HC_PLANT_PARAM_2]}
MOCK_HC_LEAF_PARAM_ANALYSE_REPLY = {"JsonHcLeafParamByAnalyseIDResult": [MOCK_HC_LEAF_PARAM, MOCK_HC_LEAF_PARAM_2]}
MOCK_HC_LEAF_PARAM_REPLY = {"JsonHcLeafParamsResult": [MOCK_HC_LEAF_PARAM, MOCK_HC_LEAF_PARAM_2]}
