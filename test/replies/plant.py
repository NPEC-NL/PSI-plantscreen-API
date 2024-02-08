""""Mock replies for the plants API"""
MOCK_PLANT_BASE = {
        "PlantBarcode": "Bonus 2p",
        "PlantID": 4261,
        "PlantInfo": "5L-2p",
        "PlantName": "Bonus",
        "TrayArea": "A3"
    }

MOCK_PLANT_BASE_2 = {
        "PlantBarcode": "Malteo_c",
        "PlantID": 4294,
        "PlantInfo": "maize",
        "PlantName": "maize_malteo_c",
        "TrayArea": "D1"
    }

MOCK_ACTION_EXPERIMENT_REPLY = {
    "JsonPlantResult": [MOCK_PLANT_BASE, MOCK_PLANT_BASE_2]
}

MOCK_PLANT_TRAY_REPLY = {"JsonPlantByTrayIDResult": [MOCK_PLANT_BASE]}

MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY = {
    "JsonPlantByTrayIDAndDatesResult": [MOCK_PLANT_BASE, MOCK_PLANT_BASE_2]
}

MOCK_PLANT_TRAY_PROFILE_REPLY = {"JsonPlantByTrayProfileIDResult": [MOCK_PLANT_BASE]}

MOCK_PLANT_HEIGHT_ROUND_REPLY = {
    "JsonPlantHeightByRoundIDResult": [
        {
            "ExperimentID": 72,
            "HeightDate": "2021-08-03 14:04:41",
            "HeightValue": 380,
            "PlantBarcode": "11-4-C",
            "PlantID": 4103,
            "PlantName": "11",
            "RoundID": 3465
        },
        {
            "ExperimentID": 72,
            "HeightDate": "2021-08-03 13:57:33",
            "HeightValue": 430,
            "PlantBarcode": "oy1_N_1583_b",
            "PlantID": 4284,
            "PlantName": "maize_oy1_N_1583_b",
            "RoundID": 3465
        }
    ]
}

MOCK_PLANT_LEAF_REPLY = {
    "JsonPlantLeavesByPlantAndTrayIDResult": [
        {
            "LeafIndex": 1,
            "PlantBarcode": "PS_Tray_120",
            "PlantID": 72,
            "PlantName": "IPAP_MA_19",
            "TrayID": 71
        },
        {
            "LeafIndex": 2,
            "PlantBarcode": "PS_Tray_120",
            "PlantID": 72,
            "PlantName": "IPAP_MA_19",
            "TrayID": 71
        }
    ]
}
