""""Mock replies for the tray API"""
MOCK_TRAY_REPLY = {
    "JsonTrayResult": {
        "TrayBarcode": "6-6__1",
        "TrayID": 3631,
        "TrayInfo": "R1",
        "TrayStatus": "Active",
        "TrayStatusChanged": "2021-08-16 13:53:11",
        "TrayTypeID": 3
    }
}

MOCK_TRAY_ROUND_REPLY = {
    "JsonTrayByRoundIDResult": [
        {
            "TrayBarcode": "6-1__3",
            "TrayID": 3873,
            "TrayInfo": "R2",
            "TrayStatus": "Active",
            "TrayStatusChanged": "2021-09-28 12:13:38",
            "TrayTypeID": 3
        },
        {
            "TrayBarcode": "3-9__3",
            "TrayID": 3807,
            "TrayInfo": "R2",
            "TrayStatus": "Active",
            "TrayStatusChanged": "2021-09-28 12:13:38",
            "TrayTypeID": 3
        }
    ]
}

MOCK_TRAY_TYPE_REPLY = {
    "JsonTrayTypeResult": {
        "TypeID": 32,
        "TypeInfo": "Test IR masky pro Exp.60/66",
        "TypeMaskBottom": """<?xml version="1.0" \
                                encoding="utf-8"?><TAnyShapes width="-65534" \
                                height="-65534" xratio="1" yratio="1" ps="0" psx="0"\
                                psy="0"><TLineShapes /><TMultiShapes \
                                /></TAnyShapes>","TypeMaskSide": "<?xml version="1.0" encoding="utf-8"?>\
                                <TAnyShapes width="192" height="664" xratio="1" \
                                yratio="1" ps="2.97421469669443" psx="1.67961923" \
                                psy="1.77076723317489"><TLineShapes \
                                /><TMultiShapes><TRectangleShape name="left" \
                                left="0" top="0" right="90" bottom="316" \
                                /><TRectangleShape name="right" left="91" top="1" \
                                right="180" bottom="316" \
                                /></TMultiShapes></TAnyShapes>","TypeMaskTop": "<?xml version="1.0" encoding="utf-8"?>\
                                <TAnyShapes width="-65532" height="-65532" \
                                xratio="1" yratio="1" ps="1" psx="1" \
                                psy="1"><TLineShapes /><TMultiShapes \
                                /></TAnyShapes>","TypeMaskUnderSide": "<?xml version="1.0" \
                                encoding="utf-8"?><TAnyShapes width="-65534" \
                                height="-65534" xratio="1" yratio="1" ps="0" psx="0"\
                                psy="0"><TLineShapes /><TMultiShapes \
                                /></TAnyShapes>""",
        "TypeName": "IRTest03",
        "TypeSizeX": 365,
        "TypeSizeY": 300,
        "TypeSizeZ": 100
    }
}

MOCK_TRAY_TYPE_TRAY_REPLY = {
    "JsonTrayTypeByTrayIDResult": {
        "TypeID": 3,
        "TypeInfo": "One plant",
        "TypeMaskBottom": """<?xml version="1.0" \
                            encoding="utf-8"?> <TAnyShapes width="600" \
                            height="2260" xratio="1.0" yratio="1.0" ps="1"> \
                            <TLineShapes/> <TMultiShapes> <TRectangleShape \
                            name="A1" left="0" top="0" right="599" \
                            bottom="1129"/> </TMultiShapes> </TAnyShapes>","TypeMaskSide": \
                            "<?xml version="1.0" encoding="utf-8"?> <TAnyShapes width="600" height="2260" \
                            xratio="1.0" yratio="1.0" ps="1"> <TLineShapes/> \
                            <TMultiShapes> <TRectangleShape name="A1" left="0" \
                            top="0" right="599" bottom="1129"/> </TMultiShapes> \
                            </TAnyShapes>","TypeMaskTop": "<?xml version="1.0" encoding="utf-8"?> \
                            <TAnyShapes width="1000" height="1000" \
                            xratio="1.0" yratio="1.0" ps="1"> <TLineShapes/> \
                            <TMultiShapes> <TRectangleShape name="A1" left="0" \
                            top="0" right="999" bottom="999"/> </TMultiShapes> \
                            </TAnyShapes>","TypeMaskUnderSide": "<?xml version="1.0" \
                            encoding="utf-8"?> <TAnyShapes width="600" \
                            height="2260" xratio="1.0" yratio="1.0" ps="1"> \
                            <TLineShapes/> <TMultiShapes> <TRectangleShape \
                            name="A1" left="0" top="0" right="599" \
                            bottom="1129"/> </TMultiShapes> </TAnyShapes>""",
        "TypeName": "Tray 1x1",
        "TypeSizeX": 100,
        "TypeSizeY": 100,
        "TypeSizeZ": 100
    }
}

MOCK_TRAY_TYPE_TRAY_PROFILE_REPLY = {
    "JsonTrayTypeByTrayProfileIDResult": {
        "TypeID": 21,
        "TypeInfo": "n/a",
        "TypeMaskBottom": """<?xml version="1.0" \
   encoding="utf-8"?> <TAnyShapes width="600" \
   height="2260" xratio="1.0" yratio="1.0" ps="1"> \
   <TLineShapes/> <TMultiShapes> <TRectangleShape \
   name="A1" left="0" top="0" right="599" \
   bottom="1129"/> </TMultiShapes> </TAnyShapes>","TypeMaskSide": \
   "<?xml version="1.0" encoding="utf-8"?><TAnyShapes width="627" height="1173" \
   xratio="1" yratio="1" ps="0.169491739901072" \
   psx="0.411186961" \
   psy="0.412201154163232"><TLineShapes \
   /><TMultiShapes><TRectangleShape name="Area 0" \
   left="61" top="0" right="627" bottom="326" \
   /></TMultiShapes></TAnyShapes>","TypeMaskTop": \
   "<?xml version="1.0" encoding="utf-8"?><TAnyShapes width="726" height="705" xratio="1"\
   yratio="1" ps="0.070554166084197" psx="0.265620342"\
   psy="0.265620342"><TLineShapes \
   /><TMultiShapes><TCircleShape name="Area 0" \
   left="0" top="0" right="690" bottom="653" \
   /><TCircleShape name="Area 4" left="258" top="285" \
   right="407" bottom="421" \
   /></TMultiShapes></TAnyShapes>","TypeMaskUnderSide": "<?xml version="1.0" \
   encoding="utf-8"?> <TAnyShapes width="600" \
   height="2260" xratio="1.0" yratio="1.0" ps="1"> \
   <TLineShapes/> <TMultiShapes> <TRectangleShape \
   name="A1" left="0" top="0" right="599" \
   bottom="1129"/> </TMultiShapes> </TAnyShapes>""",
        "TypeName": "Tray_Arni",
        "TypeSizeX": 100,
        "TypeSizeY": 100,
        "TypeSizeZ": 100
    }
}

MOCK_TRAY_PROFILE_REPLY = {
    "JsonTrayProfileByIDResult": {
        "ProfileDateStart": "2021-11-10 13:45:06",
        "ProfileDateStop": None,
        "ProfileID": 2569,
        "ProfileName": "2021-11-10 13:45:06",
        "TrayID": 4177
    }
}

MOCK_TRAY_PROFILE_TRAY_REPLY = {
    "JsonTrayProfileByTrayIDResult": [
        {
            "ProfileDateStart": "2021-08-16 13:53:11",
            "ProfileDateStop": "2021-08-17 08:32:48",
            "ProfileID": 24128,
            "ProfileName": "2021-08-16 13:53:11",
            "TrayID": 3631
        },
        {
            "ProfileDateStart": "2021-08-17 08:32:48",
            "ProfileDateStop": "",
            "ProfileID": 24398,
            "ProfileName": "2021-08-17 08:32:48",
            "TrayID": 3631
        }
    ]
}

MOCK_TRAY_PROFILE_USED_TRAY_REPLY = {
    "JsonUsedTrayProfileByTrayIDResult": [
        {
            "ProfileDateStart": "2021-08-16 13:53:11",
            "ProfileDateStop": "2021-08-17 08:32:48",
            "ProfileID": 24114,
            "ProfileName": "2021-08-16 13:53:11",
            "TrayID": 3630
        },
        {
            "ProfileDateStart": "2021-08-12 10:57:10",
            "ProfileDateStop": "2021-08-16 13:53:11",
            "ProfileID": 23832,
            "ProfileName": "2021-08-12 10:57:10",
            "TrayID": 3630
        }
    ]
}

MOCK_TRAY_PROFILE_TO_DATE_TRAY_REPLY = {
    "JsonTrayProfileByTrayIDToDateResult": {
        "ProfileDateStart": "2021-08-16 13:53:11",
        "ProfileDateStop": "2021-08-17 08:32:48",
        "ProfileID": 24128,
        "ProfileName": "2021-08-16 13:53:11",
        "TrayID": 3631
    }
}

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
