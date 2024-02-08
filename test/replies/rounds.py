""""Mock replies for the rounds API"""
MOCK_ROUND_BASE = {
    "ActionID": 4379,
    "ExperimentID": 73,
    "RoundDateStart": "2021-08-24 08:30:00",
    "RoundDateStop": "",
    "RoundDone": False,
    "RoundID": 3522,
    "RoundProtocolPath": r"""2021-08-24\RoundProtocol_2021-08-24_08-30-00.txt """,
    "RoundStatus": "Running"
    }

MOCK_ROUND_BASE_2 = {
    "ActionID": 2548,
    "ExperimentID": 50,
    "RoundDateStart": "2019-11-12 09:15:33",
    "RoundDateStop": "2019-11-12 09:30:20",
    "RoundDone": True,
    "RoundID": 1793,
    "RoundProtocolPath": r"""2019-11-12\RoundProtocol_2019-11-12_09-15-32.txt""",
    "RoundStatus": "Ok"
}

MOCK_Round_REPLY = {"JsonRoundResult": MOCK_ROUND_BASE}

MOCK_ROUND_EXPERIMENT_REPLY = {
    "JsonRoundByExperimentIDResult": [MOCK_ROUND_BASE, MOCK_ROUND_BASE_2]
    }

MOCK_ROUND_DATE_EXPERIMENT_REPLY = {
    "JsonRoundByExperimentIDAndDateResult": [MOCK_ROUND_BASE, MOCK_ROUND_BASE_2]
    }

MOCK_ORDER_BASE = {
    "ExperimentID": 84,
    "Order": 11,
    "RoundID": 4337
    }

MOCK_ORDER_BASE_2 = {
    "ExperimentID": 83,
    "Order": 2,
    "RoundID": 4257
    }

MOCK_ROUND_ORDER_ROUND_REPLY = {"JsonRoundOrderResult": MOCK_ORDER_BASE}

MOCK_ROUND_ORDER_EXPERIMENT_REPLY = {
    "JsonRoundOrderByExperimentIDResult": [MOCK_ORDER_BASE, MOCK_ORDER_BASE_2]
    }

MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY = {
    "JsonRoundOrderByExperimentIDAndDateResult": [MOCK_ORDER_BASE, MOCK_ORDER_BASE_2]
    }
