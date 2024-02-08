"""Test plant models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class PlantModels(unittest.TestCase):
    def plant_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_info, exp_dict['PlantInfo'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.tray_area, exp_dict['TrayArea'])

    def plant_height_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.height_date, exp_dict['HeightDate'])
        self.assertEqual(exp_class.height_value, exp_dict['HeightValue'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])

    def leaf_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.leaf_index, exp_dict['LeafIndex'])
        self.assertEqual(exp_class.plant_barcode, exp_dict['PlantBarcode'])
        self.assertEqual(exp_class.plant_id, exp_dict['PlantID'])
        self.assertEqual(exp_class.plant_name, exp_dict['PlantName'])
        self.assertEqual(exp_class.tray_id, exp_dict['TrayID'])

    def test_plant_none(self):
        reply = models.plant.PlantWrapper.from_dict({'JsonPlantResult': None})
        self.assertEqual(reply, [])

    def test_plant_empty(self):
        reply = models.plant.PlantWrapper.from_dict({'JsonPlantResult': []})
        self.assertEqual(reply, [])

    def test_plant(self):
        reply = models.plant.PlantWrapper.from_dict(replies.plant.MOCK_PLANT_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_REPLY['JsonPlantResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_REPLY['JsonPlantResult'])):
            self.plant_assertor(reply[i], replies.plant.MOCK_PLANT_REPLY['JsonPlantResult'][i])

    def test_plant_tray_none(self):
        reply = models.plant.PlantTray.from_dict({'JsonPlantByTrayIDResult': None})
        self.assertEqual(reply, [])

    def test_plant_tray_empty(self):
        reply = models.plant.PlantTray.from_dict({'JsonPlantByTrayIDResult': []})
        self.assertEqual(reply, [])

    def test_plant_tray(self):
        reply = models.plant.PlantTray.from_dict(replies.plant.MOCK_PLANT_TRAY_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_TRAY_REPLY['JsonPlantByTrayIDResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_TRAY_REPLY['JsonPlantByTrayIDResult'])):
            self.plant_assertor(reply[i], replies.plant.MOCK_PLANT_TRAY_REPLY['JsonPlantByTrayIDResult'][i])

    def test_plant_tray_profile_tray_none(self):
        reply = models.plant.PlantTrayProfileTray.from_dict({'JsonPlantByTrayIDAndDatesResult': None})
        self.assertEqual(reply, [])

    def test_plant_tray_profile_tray_empty(self):
        reply = models.plant.PlantTrayProfileTray.from_dict({'JsonPlantByTrayIDAndDatesResult': []})
        self.assertEqual(reply, [])

    def test_plant_tray_profile_tray(self):
        reply = models.plant.PlantTrayProfileTray.from_dict(replies.plant.MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY['JsonPlantByTrayIDAndDatesResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY['JsonPlantByTrayIDAndDatesResult'])):
            self.plant_assertor(reply[i], replies.plant.MOCK_PLANT_TRAY_PROFILE_TRAY_REPLY['JsonPlantByTrayIDAndDatesResult'][i])

    def test_plant_tray_profile_none(self):
        reply = models.plant.PlantTrayProfile.from_dict({'JsonPlantByTrayProfileIDResult': None})
        self.assertEqual(reply, [])

    def test_plant_tray_profile_empty(self):
        reply = models.plant.PlantTrayProfile.from_dict({'JsonPlantByTrayProfileIDResult': []})
        self.assertEqual(reply, [])

    def test_plant_tray_profile(self):
        reply = models.plant.PlantTrayProfile.from_dict(replies.plant.MOCK_PLANT_TRAY_PROFILE_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_TRAY_PROFILE_REPLY['JsonPlantByTrayProfileIDResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_TRAY_PROFILE_REPLY['JsonPlantByTrayProfileIDResult'])):
            self.plant_assertor(reply[i], replies.plant.MOCK_PLANT_TRAY_PROFILE_REPLY['JsonPlantByTrayProfileIDResult'][i])

    def test_plant_height_round_none(self):
        reply = models.plant.PlantHeightRound.from_dict({'JsonPlantHeightByRoundIDResult': None})
        self.assertEqual(reply, [])

    def test_plant_height_round_empty(self):
        reply = models.plant.PlantHeightRound.from_dict({'JsonPlantHeightByRoundIDResult': []})
        self.assertEqual(reply, [])

    def test_plant_height_round(self):
        reply = models.plant.PlantHeightRound.from_dict(replies.plant.MOCK_PLANT_HEIGHT_ROUND_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_HEIGHT_ROUND_REPLY['JsonPlantHeightByRoundIDResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_HEIGHT_ROUND_REPLY['JsonPlantHeightByRoundIDResult'])):
            self.plant_height_assertor(reply[i], replies.plant.MOCK_PLANT_HEIGHT_ROUND_REPLY['JsonPlantHeightByRoundIDResult'][i])

    def test_plant_leaf_none(self):
        reply = models.plant.PlantLeaf.from_dict({'JsonPlantLeavesByPlantAndTrayIDResult': None})
        self.assertEqual(reply, [])

    def test_plant_leaf_empty(self):
        reply = models.plant.PlantLeaf.from_dict({'JsonPlantLeavesByPlantAndTrayIDResult': []})
        self.assertEqual(reply, [])

    def test_plant_leaf(self):
        reply = models.plant.PlantLeaf.from_dict(replies.plant.MOCK_PLANT_LEAF_REPLY)
        self.assertEqual(len(reply), len(replies.plant.MOCK_PLANT_LEAF_REPLY['JsonPlantLeavesByPlantAndTrayIDResult']))
        for i in range(0, len(replies.plant.MOCK_PLANT_LEAF_REPLY['JsonPlantLeavesByPlantAndTrayIDResult'])):
            self.leaf_assertor(reply[i], replies.plant.MOCK_PLANT_LEAF_REPLY['JsonPlantLeavesByPlantAndTrayIDResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = PlantModels()
    test_case.test_plant_none()
    test_case.test_plant_empty()
    test_case.test_plant()
    test_case.test_plant_tray_none()
    test_case.test_plant_tray_empty()
    test_case.test_plant_tray()
    test_case.test_plant_tray_profile_tray_none()
    test_case.test_plant_tray_profile_tray_empty()
    test_case.test_plant_tray_profile_tray()
    test_case.test_plant_tray_profile_none()
    test_case.test_plant_tray_profile_empty()
    test_case.test_plant_tray_profile()
    test_case.test_plant_height_round_none()
    test_case.test_plant_height_round_empty()
    test_case.test_plant_height_round()
    test_case.test_plant_leaf_none()
    test_case.test_plant_leaf_empty()
    test_case.test_plant_leaf()
