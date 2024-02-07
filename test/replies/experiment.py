""""Mock replies for the experiment API"""
MOCK_EXPERIMENT_ID_REPLY = {
    "JsonExperimentIDResult": [
        {
            "ExperimentID": 2
        },
        {
            "ExperimentID": 3
        }
    ]
}

MOCK_EXPERIMENT_REPLY = {
    "JsonExperimentResult": {
        "CreatedDate": "2021-07-22 13:53:42",
        "ExperimentID": 72,
        "ExperimentInfo": "Data can be deleted",
        "ExperimentName": "Modular - testing -BARA",
        "ExperimentStatus": "Active",
        "OwnerID": 6,
        "StatusChangedDate": "2021-07-22 13:53:42"
    }
}

MOCK_EXPERIMENT_DATE_REPLY = {
    "JsonExperimentByDateResult": [
        {
            "CreatedDate": "2021-07-22 13:53:42",
            "ExperimentID": 72,
            "ExperimentInfo": "Data can be deleted",
            "ExperimentName": "Modular - testing -BARA",
            "ExperimentStatus": "Active",
            "OwnerID": 6,
            "StatusChangedDate": "2021-07-22 13:53:42"
        },
        {
            "CreatedDate": "2021-08-11 15:42:05",
            "ExperimentID": 73,
            "ExperimentInfo": "Round 1",
            "ExperimentName": "PS90 CAPITALIZE_B1K",
            "ExperimentStatus": "Active",
            "OwnerID": 6,
            "StatusChangedDate": "2021-08-11 15:42:05"
        }
    ]
}

MOCK_EXPERIMENT_OWNER_REPLY = {
    "JsonExperimentByOwnerResult": [
        {
            "CreatedDate": "2017-12-06 13:12:56",
            "ExperimentID": 18,
            "ExperimentInfo": "Various tests",
            "ExperimentName": "TEST",
            "ExperimentStatus": "Deleted",
            "OwnerID": 11,
            "StatusChangedDate": "2020-06-02 13:28:57"
        },
        {
            "CreatedDate": "2018-0426 10:06:08",
            "ExperimentID": 31,
            "ExperimentInfo": "K.K",
            "ExperimentName": "PS37_wheatDrought",
            "ExperimentStatus": "Active",
            "OwnerID": 11,
            "StatusChangedDate": "2018-04-26 10:06:08"
        }
    ]
}

MOCK_OWNER_ID_REPLY = {
    "JsonOwnerIDResult": [
        {
            "OwnerID": 6
        },
        {
            "OwnerID": 13
        }
    ]
}

MOCK_OWNER_REPLY = {
    "JsonOwnerResult": [
        {
            "CreateDate": "2016-06-13 16:08:38",
            "Email": "admin@admin.cz",
            "FirstName": "",
            "LastFailedDate": "2021-07-26 11:18:01",
            "LastName": "admin",
            "LastSuccessLogin": "2021-07-30 14:33:59",
            "Login": "admin",
            "OwnerID": "6",
            "SmsPhoneNumber": "123456789"
        },
        {
            "CreateDate": "2017-10-16 13:48:13",
            "Email": "",
            "FirstName": "Michal",
            "LastFailedDate": "2018-03-29 10:22:50",
            "LastName": "Navsteva Polsko",
            "LastSuccessLogin": "2017-11-03 13:59:05",
            "Login": "Michal",
            "OwnerID": "7",
            "SmsPhoneNumber": ""
        }
    ]
}

MOCK_NOTE_EXPERIMENT_REPLY = {
    "JsonNoteResult": [
        {
            "ExperimentID": 6,
            "NoteCreatedDate": "2016-11-29 14:45:59",
            "NoteID": 1,
            "NoteText": "Test pro Zbynka - pouze RGB top a side jeden uhel plus vazeni, maual D2",
            "OwnerID": 6
        }
    ]
}
