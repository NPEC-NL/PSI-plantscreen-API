"""Plantscreen API tests"""
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

# Add the parent folder to the path
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from plantscreen import xml_decoder

PROTOCOL_XML = '<Protocol>\r\n \
                    <Measure>\r\n\
                        <Prescription id="1" name="Recipe New:1">\r\n\
                            <FC1 height="Default">\r\n\
                                <Offset>0</Offset>\r\n\
                                <Protocol id="16" sid="phiPSII_default" />\r\n\
                                <Delay>00:00:00</Delay>\r\n\
                            </FC1>\r\n\
                            <Analyse>\r\n\
                                <MaskErosionLevel>1</MaskErosionLevel>\r\n\
                                <FC1>\r\n\
                                    <PlantMask>\r\n\
                                        <AutomaticThreshold>false</AutomaticThreshold>\r\n\
                                        <ManMinThresholdValue>4500</ManMinThresholdValue>\r\n\
                                        <ManMaxThresholdValue>65535</ManMaxThresholdValue>\r\n\
                                        <MaskFrameIndex>false</MaskFrameIndex>\r\n\
                                        <MaskFrameIndexValue>1</MaskFrameIndexValue>\r\n\
                                        <MinSize>25</MinSize>\r\n\
                                    </PlantMask>\r\n\
                                </FC1>\r\n\
                            </Analyse>\r\n\
                        </Prescription>\r\n\
                        <Batch name="G8_3x3_square_all_tables" pid="1" date="2023-06-22" />\r\n\
                        <Tray sid="NPEC_G8_3x3_001" id="61" pid="1" />\r\n\
                        <Tray sid="NPEC_G8_3x3_006" id="66" pid="1" />\r\n\
                        <Tray sid="NPEC_G8_3x3_041" id="101" pid="1" />\r\n\
                        <Tray sid="NPEC_G8_3x3_046" id="106" pid="1" />\r\n\
                        <TrayOrder>Custom</TrayOrder>\r\n\
                        <SafeMovement>False</SafeMovement>\r\n\
                        <TrayPosRegistr id="36" name="NPEC_G8_3x3" />\r\n\
                    </Measure>\r\n\
                </Protocol>'

PROTOCOL_JSON = {
    "Prescription": [
        {
            "id": "1",
            "name": "Recipe New:1",
            "FC1": [
                {
                    "height": "Default",
                    "Offset": [
                        {
                            "_text": "0"
                        }
                    ],
                    "Protocol": [
                        {
                            "id": "16",
                            "sid": "phiPSII_default"
                        }
                    ],
                    "Delay": [
                        {
                            "_text": "00:00:00"
                        }
                    ]
                }
            ],
            "Analyse": [
                {
                    "MaskErosionLevel": [
                        {
                            "_text": "1"
                        }
                    ],
                    "FC1": [
                        {
                            "PlantMask": [
                                {
                                    "AutomaticThreshold": [
                                        {
                                            "_text": "false"
                                        }
                                    ],
                                    "ManMinThresholdValue": [
                                        {
                                            "_text": "4500"
                                        }
                                    ],
                                    "ManMaxThresholdValue": [
                                        {
                                            "_text": "65535"
                                        }
                                    ],
                                    "MaskFrameIndex": [
                                        {
                                            "_text": "false"
                                        }
                                    ],
                                    "MaskFrameIndexValue": [
                                        {
                                            "_text": "1"
                                        }
                                    ],
                                    "MinSize": [
                                        {
                                            "_text": "25"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "Batch": [
        {
            "name": "G8_3x3_square_all_tables",
            "pid": "1",
            "date": "2023-06-22"
        }
    ],
    "Tray": [
        {
            "sid": "NPEC_G8_3x3_001",
            "id": "61",
            "pid": "1"
        },
        {
            "sid": "NPEC_G8_3x3_006",
            "id": "66",
            "pid": "1"
        },
        {
            "sid": "NPEC_G8_3x3_041",
            "id": "101",
            "pid": "1"
        },
        {
            "sid": "NPEC_G8_3x3_046",
            "id": "106",
            "pid": "1"
        }],
    "TrayOrder": [
            {
                "_text": "Custom"
            }
        ],
    "SafeMovement": [
            {
                "_text": "False"
            }
        ],
    "TrayPosRegistr": [
            {
                "id": "36",
                "name": "NPEC_G8_3x3"
            }
        ]
    }


class MyTestCase(unittest.TestCase):
    def test_protocolxml_to_dict(self):
        result_dict = xml_decoder.protocolxml_to_dict(PROTOCOL_XML)
        self.assertDictEqual(result_dict, PROTOCOL_JSON)


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = MyTestCase()
    test_case.test_protocolxml_to_dict()
