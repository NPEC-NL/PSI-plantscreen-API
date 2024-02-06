""""Mock replies for the plants API"""
MOCK_PLANT_REPLY = {
    "JsonPlantResult": [
        {
            "PlantBarcode": "Bonus 2p",
            "PlantID": 4261,
            "PlantInfo": "5L-2p",
            "PlantName": "Bonus",
            "TrayArea": "A3"
        },
        {
            "PlantBarcode": "Malteo_c",
            "PlantID": 4294,
            "PlantInfo": "maize",
            "PlantName": "maize_malteo_c",
            "TrayArea": "D1"
        }
    ]
}

MOCK_PLANT_TRAY_REPLY = {
    "JsonPlantByTrayIDResult": [
        {
            "PlantBarcode": "5-12__R1__A",
            "PlantID": 5125,
            "PlantInfo": "5-12",
            "PlantName": "5-12__A",
            "TrayArea": "A1"
        }
    ]
}

MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY = {
    "JsonPlantByTrayIDAndDatesResult": [
        {
            "PlantBarcode": "A1",
            "PlantID": 4190,
            "PlantInfo": "",
            "PlantName": "Tomato",
            "TrayArea": "A1"
        },
        {
            "PlantBarcode": "A2",
            "PlantID": 4191,
            "PlantInfo": "",
            "PlantName": "Tomato",
            "TrayArea": "A2"
        }
    ]
}

MOCK_PLANT_TRAY_PROFILE_REPLY = {
    "JsonPlantByTrayProfileIDResult": [
        {
            "PlantBarcode": "6-6__R1__A",
            "PlantID": 5126,
            "PlantInfo": "",
            "PlantName": "6-6__A",
            "TrayArea": "A2"
        }
    ]
}

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
