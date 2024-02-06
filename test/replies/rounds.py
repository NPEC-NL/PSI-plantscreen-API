""""Mock replies for the rounds API"""
MOCK_Round_REPLY = {
    "JsonRoundResult": {
        "ActionID": 4379,
        "ExperimentID": 73,
        "RoundDateStart": "2021-08-24 08:30:00",
        "RoundDateStop": "",
        "RoundDone": False,
        "RoundID": 3522,
        "RoundProtocolPath": "2021-08-24RoundProtocol_2021-08-24_08-30-00.txt ",
        "RoundStatus": "Running"
    }
}

MOCK_ROUND_EXPERIMENT_REPLY = {
    "JsonRoundByExperimentIDResult": [
        {
            "ActionID": 2547,
            "ExperimentID": 50,
            "RoundDateStart": "2019-11-11 10:58:40",
            "RoundDateStop": "2019-11-11 11:45:11",
            "RoundDone": True,
            "RoundID": 1792,
            "RoundProtocolPath": "2019-11-11RoundProtocol_2019-11-11_10-58-40.txt",
            "RoundStatus": "Ok"
        },
        {
            "ActionID": 2548,
            "ExperimentID": 50,
            "RoundDateStart": "2019-11-12 09:15:33",
            "RoundDateStop": "2019-11-12 09:30:20",
            "RoundDone": True,
            "RoundID": 1793,
            "RoundProtocolPath": "2019-11-12RoundProtocol_2019-11-12_09-15-32.txt",
            "RoundStatus": "Ok"
        }
    ]
}

MOCK_ROUND_DATE_EXPERIMENT_REPLY = {
    "JsonRoundByExperimentIDAndDateResult": [
        {
            "ActionID": 2242,
            "ExperimentID": 23,
            "RoundDateStart": "2021-12-23 14:38:12",
            "RoundDateStop": "2021-12-23 15:13:19",
            "RoundDone": True,
            "RoundID": 1062,
            "RoundProtocolPath": "2021-12-23RoundProtocol_2021-12-23_14-38-12.txt",
            "RoundStatus": "UserTerminated"
        },
        {
            "ActionID": 2299,
            "ExperimentID": 23,
            "RoundDateStart": "2021-12-23 15:53:44",
            "RoundDateStop": "2021-11-23 16:54:29",
            "RoundDone": True,
            "RoundID": 1063,
            "RoundProtocolPath": "2021-12-23RoundProtocol_2021-12-23_15-53-44.txt",
            "RoundStatus": "Ok"
        }
    ]
}

MOCK_ROUND_ORDER_ROUND_REPLY = {
    "JsonRoundOrderResult": {
        "ExperimentID": 84,
        "Order": 11,
        "RoundID": 4337
    }
}

MOCK_ROUND_ORDER_EXPERIMENT_REPLY = {
    "JsonRoundOrderByExperimentIDResult": [
        {
            "ExperimentID": 83,
            "Order": 1,
            "RoundID": 4256
        },
        {
            "ExperimentID": 83,
            "Order": 2,
            "RoundID": 4257
        }
    ]
}

MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY = {
    "JsonRoundOrderByExperimentIDAndDateResult": [
        {
            "ExperimentID": 82,
            "Order": 84,
            "RoundID": 4272
        },
        {
            "ExperimentID": 82,
            "Order": 85,
            "RoundID": 4273
        }
    ]
}
