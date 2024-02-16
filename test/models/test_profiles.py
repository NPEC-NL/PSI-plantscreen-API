"""Test experiment models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class ProfileModels(unittest.TestCase):
    def test_profile_id_empty(self):
        """"emply list reply"""
        reply = models.profile_models.ProfileIDs.from_dict({'json_system_profile_id_result': []})
        self.assertEqual(reply, [])

    def test_profile_id(self):
        reply = models.profile_models.ProfileIDs.from_dict(replies.profile.MOCK_PROFILE_ID_JSON)
        self.assertEqual(len(reply), len(replies.profile.MOCK_PROFILE_ID_JSON['json_system_profile_id_result']))
        for i in range(0, len(replies.profile.MOCK_PROFILE_ID_JSON['json_system_profile_id_result'])):
            self.assertEqual(reply[i], replies.profile.MOCK_PROFILE_ID_JSON['json_system_profile_id_result'][i]['profile_id'])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = ProfileModels()
    test_case.test_profile_id_empty()
    test_case.test_profile_id()
