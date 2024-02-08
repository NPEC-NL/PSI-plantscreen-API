""""Mock replies for the Multispectral API"""
MOCK_MSC_IMAGE_BASE = {
    "ActionID": 684,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 70,
    "MeasureAngle": 0,
    "MeasureDate": "2021-08-19 10:31:44",
    "MeasureHeight": 0,
    "MeasureID": 2848,
    "RoundID": 598,
    "TrayBarcode": "TAU_SimonB_10Aug21_06",
    "TrayID": 521,
    "TrayProfileID": 522,
    "ImagePath": r"""2021-08-19\MscRawFrame_2021-08-19_10-31-44.usraw"""
}

MOCK_MSC_IMAGE_BASE_2 = {
    "ActionID": 684,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 70,
    "MeasureAngle": 0,
    "MeasureDate": "2021-08-19 10:31:44",
    "MeasureHeight": 0,
    "MeasureID": 2848,
    "RoundID": 598,
    "TrayBarcode": "TAU_SimonB_10Aug21_06",
    "TrayID": 521,
    "TrayProfileID": 522,
    "ImagePath": r"""2021-08-19\MscRawFrame_2021-08-19_10-31-44_2.usraw"""
}

MOCK_MSC_IMAGING_MEASURE_REPLY = {
    "JsonMscImagingByIDResult": [MOCK_MSC_IMAGE_BASE, MOCK_MSC_IMAGE_BASE_2]
    }

MOCK_MSC_IMAGING_REPLY = {
    "JsonMscImagingResult": [MOCK_MSC_IMAGE_BASE, MOCK_MSC_IMAGE_BASE_2]
    }

MOCK_MSC_EXTENDED_BASE = {
    "DeviceID": 0,
    "ExtendedData": """<DataSet> <Item name="latitude"
                    type="double" unit="degree">49.33946426</Item>
                    <Item name="longitude" type="double"
                    unit="degree">16.47588586</Item> <Item
                    name="distanceToWantedPoint" type="double"
                    unit="meters">0.12</Item> <Item name="speed"
                    type="double" unit="km/h">1.9</Item> </DataSet>""",
    "MeasureDate": "2021-04-22 09:40:07",
    "MeasureID": 0,
    "RoundID": 0,
    "TrayID": 0
}

MOCK_MSC_EXTENDED_BASE_2 = {
    "DeviceID": 0,
    "ExtendedData": None,
    "MeasureDate": None,
    "MeasureID": 0,
    "RoundID": 0,
    "TrayID": 0
}

MOCK_MSC_IMAGING_EXTENDED_DATA_MEASURE_REPLY = {"JsonMscMeasureExtendedDataByIDResult": MOCK_MSC_EXTENDED_BASE}

MOCK_MSC_IMAGING_EXTENDED_DATA_REPLY = {"JsonMscMeasureExtendedDataResult": MOCK_MSC_EXTENDED_BASE_2}

MOCK_MSC_MASK_BASE = {
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 71,
    "MaskIsLeaf": False,
    "MeasureAngle": 0,
    "MeasureDate": "2021-09-09 12:04:47",
    "MeasureID": 2855,
    "PlantMaskPath": r"""2021-09-09\MscMask_2021-09-09_12-04-47.xsel""",
    "RoundID": 599,
    "TrayBarcode": "TAU_MoranA_09Sep21_07",
    "TrayID": 528
}

MOCK_MSC_PLANT_MASK_MEASURE_REPLY = {"JsonMscPlantMaskByMeasureIDResult": MOCK_MSC_MASK_BASE}

MOCK_MSC_PLANT_MASK_REPLY = {"JsonMscPlantMaskResult": [MOCK_MSC_MASK_BASE]}

MOCK_MSC_PARAM_BASE = {
    "ParameterID": 5,
    "ParameterName": "Par1",
    "ParameterUnit": "a.u."
}

MOCK_MSC_PARAM_BASE_2 = {
    "ParameterID": 6,
    "ParameterName": "Water Content",
    "ParameterUnit": ""
}

MOCK_MSC_PARAM_REPLY = {"JsonMscParamResult": MOCK_MSC_PARAM_BASE}

MOCK_MSC_PARAM_USED_ANALYSE_REPLY = {
    "JsonMscUsedParamByAnalyseIDResult": [MOCK_MSC_PARAM_BASE, MOCK_MSC_PARAM_BASE_2]
    }

MOCK_MSC_PARAM_USED_REPLY = {
    "JsonMscUsedParamResult": [MOCK_MSC_PARAM_BASE, MOCK_MSC_PARAM_BASE_2]
    }

MOCK_MSC_PARAM_IMAGE_BASE = {
    "AnalyseID": 2331,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 70,
    "MeasureAngle": 0,
    "MeasureID": 2841,
    "ParameterID": 1,
    "ParameterImagePath": r"""2021-08-16\MscParamImage_2021-08-16_11-04-39.fimg","ParameterName": "Water Content""",
    "RoundID": 597,
    "TrayBarcode": "TAU_SimonB_10Aug21_05",
    "TrayID": 520
}

MOCK_MSC_PARAM_IMAGE_ANALYSE_REPLY = {"JsonMscParameterImageByAnalyseIDResult": MOCK_MSC_PARAM_IMAGE_BASE}

MOCK_MSC_PARAM_IMAGE_REPLY = {"JsonMscParameterImageResult": [MOCK_MSC_PARAM_IMAGE_BASE]}

MOCK_MSC_PLANT_BASE = {
    "AnalyseID": 2345,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 71,
    "MeasureAngle": 0,
    "MeasureID": 2855,
    "ParameterAvg": 0.9889633655548096,
    "ParameterID": 1,
    "ParameterMax": 1.6138311624526978,
    "ParameterMedian": 0.974317193031311,
    "ParameterMin": 0.7074135541915894,
    "ParameterName": "Water Content",
    "ParameterStddev": 0.13246586410999298,
    "PlantBarcode": "Moran_09Sep21_121",
    "PlantID": 9724,
    "PlantName": "39",
    "RoundID": 599,
    "TrayArea": "A1",
    "TrayBarcode": "TAU_Moran_A09Sep21_07",
    "TrayID": 528
}

MOCK_MSC_PLANT_BASE_2 = {
    "AnalyseID": 2345,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 71,
    "MeasureAngle": 0,
    "MeasureID": 2855,
    "ParameterAvg": 0.9522637128829956,
    "ParameterID": 1,
    "ParameterMax": 1.3661658763885498,
    "ParameterMedian": 0.9618086817880371,
    "ParameterMin": 0.4688636362552643,
    "ParameterName": "Water Content",
    "ParameterStddev": 0.1264442801475525,
    "PlantBarcode": "Moran_09Sep21_137",
    "PlantID": 9740,
    "PlantName": "col",
    "RoundID": 599,
    "TrayArea": "D2",
    "TrayBarcode": "TAU_Moran_A09Sep21_07",
    "TrayID": 528
}

MOCK_MSC_PLANT_PARAM_ANALYSE_REPLY = {
    "JsonMscPlantParamByAnalyseIDResult": [MOCK_MSC_PLANT_BASE, MOCK_MSC_PLANT_BASE_2]
    }

MOCK_MSC_PLANT_PARAM_REPLY = {
    "JsonMscPlantParamResult": [MOCK_MSC_PLANT_BASE, MOCK_MSC_PLANT_BASE_2]
    }

MOCK_MSC_LEAF_BASE = {
    "AnalyseID": 2345,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 71,
    "LeafIndex": 2,
    "MeasureAngle": 0,
    "MeasureID": 2855,
    "ParameterAvg": 0.9280258417129517,
    "ParameterID": 1,
    "ParameterMax": 1.237754464149475,
    "ParameterMedian": 0.9088473320007324,
    "ParameterMin": 0.5613374710083008,
    "ParameterName": "Water Content",
    "ParameterStddev": 0.13929209113121033,
    "PlantBarcode": "Moran_09Sep21_121",
    "PlantID": 9724,
    "PlantName": "39",
    "RoundID": 599,
    "TrayArea": "A1",
    "TrayBarcode": "TAU_Moran_A09Sep21_07",
    "TrayID": 528
}

MOCK_MSC_LEAF_BASE_2 = {
    "AnalyseID": 2345,
    "DeviceID": 6,
    "DevicePID": "MSC1",
    "ExperimentID": 1,
    "LeafIndex": 3,
    "MeasureAngle": 0,
    "MeasureID": 2855,
    "ParameterAvg": 1.0147314071655273,
    "ParameterID": 1,
    "ParameterMax": 1.6480330228805542,
    "ParameterMedian": 1.0433568954467773,
    "ParameterMin": 0.48780107498168945,
    "ParameterName": "Water Content",
    "ParameterStddev": 0.1551567018032074,
    "PlantBarcode": "Moran_09Sep21_137",
    "PlantID": 9724,
    "PlantName": "39",
    "RoundID": 599,
    "TrayArea": "A1",
    "TrayBarcode": "TAU_Moran_A09Sep21_07",
    "TrayID": 528
}

MOCK_MSC_LEAF_PARAM_ANALYSE_REPLY = {
    "JsonMscLeafParamByAnalyseIDResult": [MOCK_MSC_LEAF_BASE, MOCK_MSC_LEAF_BASE_2]
    }

MOCK_MSC_LEAF_PARAM_REPLY = {
    "JsonMscLeafParamResult": [MOCK_MSC_LEAF_BASE, MOCK_MSC_LEAF_BASE_2]
    }

MOCK_MSC_LIGHT_BASE = {
    "ChannelID": 4,
    "LightSetCaption": "300 nm",
    "LightSetID": 9,
    "LightSetPidName": "MSC",
    "LightSetValid": True
}

MOCK_MSC_LIGHT_BASE_2 = {
    "ChannelID": 2,
    "LightSetCaption": "200 nm",
    "LightSetID": 5,
    "LightSetPidName": "MSC",
    "LightSetValid": True
}

MOCK_MSC_LIGHT_SET_REPLY = {"JsonMscLightSetResult": MOCK_MSC_LIGHT_BASE}

MOCK_MSC_LIGHT_SET_USED_REPLY = {
    "JsonMscLightSetUsedResult": [MOCK_MSC_LIGHT_BASE, MOCK_MSC_LIGHT_BASE_2]
    }

MOCK_MSC_CALIBRATE_BASE = {
    "CalibrationDate": "2019-09-26 16:41:24",
    "CalibrationID": 8,
    "CalibrationImagePath": r"""2019-09-26\MscRawFrame_2019-09-26_16-41-24_calibFrame.usraw""",
    "CameraExposure": 2000,
    "CameraGain": 0,
    "LightSetID": 1
}

MOCK_MSC_CALIBRATION_REPLY = {"JsonMscCalibrationResult": MOCK_MSC_CALIBRATE_BASE}

MOCK_MSC_CALIBRATION_LIGHT_SET_REPLY = {"JsonMscCalibrationByLightSetIDResult": [MOCK_MSC_CALIBRATE_BASE]}

# MOCK OF Multispectral calibration light by ID TODO

MOCK_MSC_CALIBRATION_LIGHT_REPLY = {
    "JsonMscCalibrationLightResult": [
        {
            "CalibrationID": 5,
            "CalibrationLightID": 6,
            "CalibrationLightLevel": 100,
            "LightCaption": "1450 nm",
            "LightID": 2,
            "LightSetID": 2
        },
        {
            "CalibrationID": 6,
            "CalibrationLightID": 7,
            "CalibrationLightLevel": 15,
            "LightCaption": "940 nm",
            "LightID": 1,
            "LightSetID": 3
        },
        {
            "CalibrationID": 6,
            "CalibrationLightID": 8,
            "CalibrationLightLevel": 45,
            "LightCaption": "1450 nm",
            "LightID": 2,
            "LightSetID": 3
        },
        {
            "CalibrationID": 8,
            "CalibrationLightID": 10,
            "CalibrationLightLevel": 32,
            "LightCaption": "940 nm",
            "LightID": 1,
            "LightSetID": 1
        }
    ]
}
