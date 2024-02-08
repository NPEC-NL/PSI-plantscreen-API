"""Test tray models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class TrayModels(unittest.TestCase):
    def tray_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.tray_barcode, exp_dict['TrayBarcode'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])
        self.assertEqual(exp_class.tray_info, exp_dict['TrayInfo'])
        self.assertEqual(exp_class.tray_status, exp_dict['TrayStatus'])
        self.assertEqual(exp_class.tray_status_changed, exp_dict['TrayStatusChanged'])
        self.assertEqual(exp_class.tray_type_id, exp_dict['TrayTypeID'])

    def tray_info_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.type_id, exp_dict['TypeID'])
        self.assertEqual(exp_class.type_info, exp_dict['TypeInfo'])
        self.assertEqual(exp_class.type_mask_bottom, exp_dict['TypeMaskBottom'])
        self.assertEqual(exp_class.type_mask_side, exp_dict['TypeMaskSide'])
        self.assertEqual(exp_class.type_mask_top, exp_dict['TypeMaskTop'])
        self.assertEqual(exp_class.type_mask_under_side, exp_dict['TypeMaskUnderSide'])
        self.assertEqual(exp_class.type_name, exp_dict['TypeName'])
        self.assertEqual(exp_class.type_size_x, exp_dict['TypeSizeX'])
        self.assertEqual(exp_class.type_size_y, exp_dict['TypeSizeY'])
        self.assertEqual(exp_class.type_size_z, exp_dict['TypeSizeZ'])

    def tray_profile_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.profile_date_start, exp_dict['ProfileDateStart'])
        self.assertEqual(exp_class.profile_date_stop, exp_dict['ProfileDateStop'])
        self.assertEqual(exp_class.profile_id, exp_dict['ProfileID'])
        self.assertEqual(exp_class.profile_name, exp_dict['ProfileName'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def scales_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.map_area, exp_dict['MapArea'])
        self.assertEqual(exp_class.map_column, exp_dict['MapColumn'])
        self.assertEqual(exp_class.map_row, exp_dict['MapRow'])
        self.assertEqual(exp_class.tray_type_id, exp_dict['TrayTypeID'])

    def test_tray_none(self):
        reply = models.tray.TrayWrapper.from_dict({'JsonTrayResult': None})
        self.assertEqual(reply, None)

    def test_tray(self):
        reply = models.tray.TrayWrapper.from_dict(replies.tray.MOCK_TRAY_REPLY)
        self.tray_assertor(reply, replies.tray.MOCK_TRAY_REPLY['JsonTrayResult'])

    def test_tray_round_none(self):
        reply = models.tray.TrayRound.from_dict({'JsonTrayByRoundIDResult': None})
        self.assertEqual(reply, [])

    def test_tray_round_empty(self):
        reply = models.tray.TrayRound.from_dict({'JsonTrayByRoundIDResult': []})
        self.assertEqual(reply, [])

    def test_tray_round(self):
        reply = models.tray.TrayRound.from_dict(replies.tray.MOCK_TRAY_ROUND_REPLY)
        self.assertEqual(len(reply), len(replies.tray.MOCK_TRAY_ROUND_REPLY['JsonTrayByRoundIDResult']))
        for i in range(0, len(replies.tray.MOCK_TRAY_ROUND_REPLY['JsonTrayByRoundIDResult'])):
            self.tray_assertor(reply[i], replies.tray.MOCK_TRAY_ROUND_REPLY['JsonTrayByRoundIDResult'][i])

    def test_tray_type_none(self):
        reply = models.tray.TrayType.from_dict({'JsonTrayTypeResult': None})
        self.assertEqual(reply, None)

    def test_tray_type(self):
        reply = models.tray.TrayType.from_dict(replies.tray.MOCK_TRAY_TYPE_REPLY)
        self.tray_info_assertor(reply, replies.tray.MOCK_TRAY_TYPE_REPLY['JsonTrayTypeResult'])

    def test_tray_type_tray_none(self):
        reply = models.tray.TrayTypeTray.from_dict({'JsonTrayTypeByTrayIDResult': None})
        self.assertEqual(reply, None)

    def test_tray_type_tray(self):
        reply = models.tray.TrayTypeTray.from_dict(replies.tray.MOCK_TRAY_TYPE_TRAY_REPLY)
        self.tray_info_assertor(reply, replies.tray.MOCK_TRAY_TYPE_TRAY_REPLY['JsonTrayTypeByTrayIDResult'])

    def test_tray_type_tray_profile_none(self):
        reply = models.tray.TrayTypeTrayProfile.from_dict({'JsonTrayTypeByTrayProfileIDResult': None})
        self.assertEqual(reply, None)

    def test_tray_type_tray_profile(self):
        reply = models.tray.TrayTypeTrayProfile.from_dict(replies.tray.MOCK_TRAY_TYPE_TRAY_PROFILE_REPLY)
        self.tray_info_assertor(reply, replies.tray.MOCK_TRAY_TYPE_TRAY_PROFILE_REPLY['JsonTrayTypeByTrayProfileIDResult'])

    def test_tray_profile_tray_none(self):
        reply = models.tray.TrayProfileTray.from_dict({'JsonTrayProfileByTrayIDResult': None})
        self.assertEqual(reply, [])

    def test_tray_profile_tray_empty(self):
        reply = models.tray.TrayProfileTray.from_dict({'JsonTrayProfileByTrayIDResult': []})
        self.assertEqual(reply, [])

    def test_tray_profile_tray(self):
        reply = models.tray.TrayProfileTray.from_dict(replies.tray.MOCK_TRAY_PROFILE_TRAY_REPLY)
        self.assertEqual(len(reply), len(replies.tray.MOCK_TRAY_PROFILE_TRAY_REPLY['JsonTrayProfileByTrayIDResult']))
        for i in range(0, len(replies.tray.MOCK_TRAY_PROFILE_TRAY_REPLY['JsonTrayProfileByTrayIDResult'])):
            self.tray_profile_assertor(reply[i], replies.tray.MOCK_TRAY_PROFILE_TRAY_REPLY['JsonTrayProfileByTrayIDResult'][i])

    def test_tray_profile_used_tray_none(self):
        reply = models.tray.TrayProfileUsedTray.from_dict({'JsonUsedTrayProfileByTrayIDResult': None})
        self.assertEqual(reply, [])

    def test_tray_profile_used_tray_empty(self):
        reply = models.tray.TrayProfileUsedTray.from_dict({'JsonUsedTrayProfileByTrayIDResult': []})
        self.assertEqual(reply, [])

    def test_tray_profile_used_tray(self):
        reply = models.tray.TrayProfileUsedTray.from_dict(replies.tray.MOCK_TRAY_PROFILE_USED_TRAY_REPLY)
        self.assertEqual(len(reply), len(replies.tray.MOCK_TRAY_PROFILE_USED_TRAY_REPLY['JsonUsedTrayProfileByTrayIDResult']))
        for i in range(0, len(replies.tray.MOCK_TRAY_PROFILE_USED_TRAY_REPLY['JsonUsedTrayProfileByTrayIDResult'])):
            self.tray_profile_assertor(reply[i], replies.tray.MOCK_TRAY_PROFILE_USED_TRAY_REPLY['JsonUsedTrayProfileByTrayIDResult'][i])

    def test_tray_profile_date_none(self):
        reply = models.tray.TrayProfileToDateTray.from_dict({'JsonTrayProfileByTrayIDToDateResult': None})
        self.assertEqual(reply, None)

    def test_tray_profile_date(self):
        reply = models.tray.TrayProfileToDateTray.from_dict(replies.tray.MOCK_TRAY_PROFILE_TO_DATE_TRAY_REPLY)
        self.tray_profile_assertor(reply, replies.tray.MOCK_TRAY_PROFILE_TO_DATE_TRAY_REPLY['JsonTrayProfileByTrayIDToDateResult'])

    def test_scale_mapping_tray_none(self):
        reply = models.tray.ScalesMappingTray.from_dict({'JsonScalesMappingByTrayIDResult': None})
        self.assertEqual(reply, [])

    def test_scale_mapping_tray_empty(self):
        reply = models.tray.ScalesMappingTray.from_dict({'JsonScalesMappingByTrayIDResult': []})
        self.assertEqual(reply, [])

    def test_scale_mapping_tray(self):
        reply = models.tray.ScalesMappingTray.from_dict(replies.tray.MOCK_SCALES_MAPPING_TRAY_REPLY)
        self.assertEqual(len(reply), len(replies.tray.MOCK_SCALES_MAPPING_TRAY_REPLY['JsonScalesMappingByTrayIDResult']))
        for i in range(0, len(replies.tray.MOCK_SCALES_MAPPING_TRAY_REPLY['JsonScalesMappingByTrayIDResult'])):
            self.scales_assertor(reply[i], replies.tray.MOCK_SCALES_MAPPING_TRAY_REPLY['JsonScalesMappingByTrayIDResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = TrayModels()
    test_case.test_tray_none()
    test_case.test_tray()
    test_case.test_tray_round_empty()
    test_case.test_tray_round()
    test_case.test_tray_type_none()
    test_case.test_tray_type()
    test_case.test_tray_type_tray_none()
    test_case.test_tray_type_tray()
    test_case.test_tray_type_tray_profile_none()
    test_case.test_tray_type_tray_profile()
    test_case.test_tray_profile_tray_none()
    test_case.test_tray_profile_tray_empty()
    test_case.test_tray_profile_tray()
    test_case.test_tray_profile_used_tray_none()
    test_case.test_tray_profile_used_tray_empty()
    test_case.test_tray_profile_used_tray()
    test_case.test_tray_profile_date_none()
    test_case.test_tray_profile_date()
    test_case.test_scale_mapping_tray_none()
    test_case.test_scale_mapping_tray_empty()
    test_case.test_scale_mapping_tray()
