""""Mock replies for the action API"""
MOCK_ACTION_REPLY = {
    "JsonActionResult": {
        "ActionDateStart": "2021-11-18 06:00:00",
        "ActionDone": True,
        "ActionGroupID": 2867,
        "ActionID": 4900,
        "ActionRunning": False,
        "ActionStatus": "ActionConflict",
        "ExperimentID": 75
    }
}

MOCK_ACTION_EXPERIMENT_REPLY = {
    "JsonActionByExperimentIDResult": [
        {
            "ActionDateStart": "2019-11-11 10:58:40",
            "ActionDone": True,
            "ActionGroupID": 1490,
            "ActionID": 2547,
            "ActionRunning": False,
            "ActionStatus": "Ok",
            "ExperimentID": 50
        },
        {
            "ActionDateStart": "2019-11-12 09:14:52",
            "ActionDone": True,
            "ActionGroupID": 1491,
            "ActionID": 2548,
            "ActionRunning": False,
            "ActionStatus": "Ok",
            "ExperimentID": 50
        }
    ]
}

MOCK_ACTION_NOT_DONE_EXPERIMENT_REPLY = {
    "JsonActionByExperimentIDNotDoneResult": [
        {
            "ActionDateStart": "2021-03-09 10:52:00",
            "ActionDone": False,
            "ActionGroupID": 2423,
            "ActionID": 3903,
            "ActionRunning": False,
            "ActionStatus": "Pending",
            "ExperimentID": 64
        },
        {
            "ActionDateStart": "2021-03-09 10:56:00",
            "ActionDone": False,
            "ActionGroupID": 2424,
            "ActionID": 3904,
            "ActionRunning": False,
            "ActionStatus": "Pending",
            "ExperimentID": 64
        }
    ]
}

MOCK_ACTION_GROUP_REPLY = {
    "JsonActionGroupResult": {
        "ActionProtocolID": 2211,
        "ExperimentID": 60,
        "GroupCaption": "SWAP_0310",
        "GroupID": 2210,
        "GroupRepeatingProtocol": """<GroupTiming type="Once"> \
            <DateTime>2020-10-03 16:13:48</DateTime> </GroupTiming>"""
    }
}

MOCK_ACTION_GROUP_ROUND_REPLY = {
    "JsonActionGroupByRoundIDResult": {
        "ActionProtocolID": 2668,
        "ExperimentID": 72,
        "GroupCaption": "FC+VNIR+SWAP",
        "GroupID": 2667,
        "GroupRepeatingProtocol": """<GroupTiming type="Once"> \
            <DateTime>2021-08-05 16:09:06</DateTime> </GroupTiming>"""
    }
}

MOCK_ACTION_PROTOCOL_REPLY = {
    "JsonActionProtocolResult": {
        "ActionD": 4377,
        "ExperimentID": 73,
        "ProtocolBody": """<Protocol> <SetLight> <Light name="LightMain1" value="16" /> \
                            <Light name="LightMain2" value="0" /> </SetLight> \
                            <TrayLoad row="3" count="30" /> <Measure> \
                            <AdaptTime>00: 00: 00</AdaptTime> \
                            <Prescription id="1" name="Recipe New:1"> <IR1 height="Default"> \
                            <Offset>0</Offset> <Protocol name='Single imaging'>(begin-measure (take-image))</Protocol> \
                            <Delay>00: 00: 00</Delay> </IR1> /> <Analyse> \
                            <MaskErosionLevel>1</MaskErosionLevel> </Analyse> \
                            </Prescription> <Batch name="PS90" pid="1" date="2021-08-19" /> <Tray sid="10-1__1" id="3354" \
                            pid="1" /> <Tray sid="10-12__1" id="3355" pid="1" /\
                            > </Measure> <SetLight> <Light name="LightMain1" \
                            value="0" /> <Light name="LightMain2" value="0" /> \
                            </SetLight> </Protocol> """,
        "ProtocolDateChanged": "2021-08-19 11:38:01",
        "ProtocolID": 2700,
        "RoundID": 3522
    }
}

MOCK_ACTION_PROTOCOL_ROUND_REPLY = {
    "JsonActionProtocolByRoundIDResult": {
        "ActionD": 4379,
        "ExperimentID": 73,
        "ProtocolBody": """<Protocol> <SetLight> <Light \
                            name="LightMain1" value="16" /> <Light \
                            name="LightMain2" value="0" /> </SetLight> <TrayLoad\
                            row="3" count="30" /> <Measure> \
                            <AdaptTime>00: 00: 00</AdaptTime> <Prescription \
                            id="1" name="Recipe New:1"> <IR1 height="Default"> \
                            <Offset>0</Offset> <Protocol name="Single \
                            imaging">(begin-measure (take-image))</Protocol> \
                            <Delay>00: 00: 00</Delay> </IR1> /> <Analyse> \
                            <MaskErosionLevel>1</MaskErosionLevel> </Analyse> \
                            </Prescription> <Batch name="PS90" pid="1" \
                            date="2021-08-19" /> <Tray sid="10-1__1" id="3354" \
                            pid="1" /> <Tray sid="10-12__1" id="3355" pid="1" /\
                            > </Measure> <SetLight> <Light name="LightMain1" \
                            value="0" /> <Light name="LightMain2" value="0" /> \
                            </SetLight> </Protocol> """,
        "ProtocolDateChanged": "2021-08-19 11:38:01",
        "ProtocolID": 2700,
        "RoundID": 3522
    }
}
