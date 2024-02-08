""""Mock replies for the tray API"""
MOCK_TRAY_BASE = {
    "TrayBarcode": "6-6__1",
    "TrayID": 3631,
    "TrayInfo": "R1",
    "TrayStatus": "Active",
    "TrayStatusChanged": "2021-08-16 13:53:11",
    "TrayTypeID": 3
    }

MOCK_TRAY_BASE_2 = {
    "TrayBarcode": "3-9__3",
    "TrayID": 3807,
    "TrayInfo": "R2",
    "TrayStatus": "Active",
    "TrayStatusChanged": "2021-09-28 12:13:38",
    "TrayTypeID": 3
    }

MOCK_TRAY_REPLY = {"JsonTrayResult": MOCK_TRAY_BASE}

MOCK_TRAY_ROUND_REPLY = {
    "JsonTrayByRoundIDResult": [MOCK_TRAY_BASE, MOCK_TRAY_BASE_2]
    }

MOCK_TRAY_INFO_BASE = {
    "TypeID": 3,
    "TypeInfo": "One plant",
    "TypeMaskBottom": """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<TAnyShapes width=\"1\" height=\"1\" xratio=\"1\" yratio=\"1\" ps=\"1\" psx=\"1\" psy=\"1\">\r\n  <TLineShapes />\r\n  <TMultiShapes />\r\n</TAnyShapes>""",
    "TypeMaskSide": """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<TAnyShapes width=\"600\" height=\"2260\" xratio=\"1.0\" yratio=\"1.0\" ps=\"1\">\r\n  <TLineShapes/>\r\n  <TMultiShapes>\r\n    <TRectangleShape name=\"A1\" left=\"0\" top=\"0\" right=\"599\" bottom=\"1129\"/>\r\n  </TMultiShapes>\r\n</TAnyShapes>""",
    "TypeMaskTop": """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<TAnyShapes width=\"1000\" height=\"1000\" xratio=\"1.0\" yratio=\"1.0\" ps=\"1\">\r\n  <TLineShapes/>\r\n  <TMultiShapes>\r\n    <TRectangleShape name=\"A1\" left=\"0\" top=\"0\" right=\"999\" bottom=\"999\"/>\r\n  </TMultiShapes>\r\n</TAnyShapes>\r\n""",
    "TypeMaskUnderSide": """<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<TAnyShapes width=\"1\" height=\"1\" xratio=\"1\" yratio=\"1\" ps=\"1\" psx=\"1\" psy=\"1\">\r\n  <TLineShapes />\r\n  <TMultiShapes />\r\n</TAnyShapes>""",
    "TypeName": "Tray 1x1",
    "TypeSizeX": 365,
    "TypeSizeY": 300,
    "TypeSizeZ": 100
    }

MOCK_TRAY_TYPE_REPLY = {"JsonTrayTypeResult": MOCK_TRAY_INFO_BASE}

MOCK_TRAY_TYPE_TRAY_REPLY = {"JsonTrayTypeByTrayIDResult": MOCK_TRAY_INFO_BASE}

MOCK_TRAY_TYPE_TRAY_PROFILE_REPLY = {"JsonTrayTypeByTrayProfileIDResult": MOCK_TRAY_INFO_BASE}

MOCK_TRAY_PROFILE_BASE = {
    "ProfileDateStart": "2021-11-10 13:45:06",
    "ProfileDateStop": None,
    "ProfileID": 2569,
    "ProfileName": "2021-11-10 13:45:06",
    "TrayID": 4177
    }

MOCK_TRAY_PROFILE_BASE_2 = {
    "ProfileDateStart": "2021-08-17 08:32:48",
    "ProfileDateStop": "",
    "ProfileID": 24398,
    "ProfileName": "2021-08-17 08:32:48",
    "TrayID": 3631
    }

MOCK_TRAY_PROFILE_REPLY = {"JsonTrayProfileResult": MOCK_TRAY_PROFILE_BASE}

MOCK_TRAY_PROFILE_TRAY_REPLY = {
    "JsonTrayProfileByTrayIDResult": [MOCK_TRAY_PROFILE_BASE,  MOCK_TRAY_PROFILE_BASE_2]
    }

MOCK_TRAY_PROFILE_USED_TRAY_REPLY = {
    "JsonUsedTrayProfileByTrayIDResult": [MOCK_TRAY_PROFILE_BASE,  MOCK_TRAY_PROFILE_BASE_2]
    }

MOCK_TRAY_PROFILE_TO_DATE_TRAY_REPLY = {"JsonTrayProfileByTrayIDToDateResult": MOCK_TRAY_PROFILE_BASE}

MOCK_SCALES_MAPPING_TRAY_REPLY = {
    "JsonScalesMappingByTrayIDResult": [
        {
            "MapArea": "A1",
            "MapColumn": 1,
            "MapRow": 1,
            "TrayTypeID": 3
        }
    ]
}
