"""Test profile models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class ProfileModels(unittest.TestCase):
    def profile_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.profile_active, exp_dict['ProfileActive'])
        self.assertEqual(exp_class.profile_id, exp_dict['ProfileID'])
        self.assertEqual(exp_class.profile_info, exp_dict['ProfileInfo'])
        self.assertEqual(exp_class.profile_name, exp_dict['ProfileName'])
        self.assertEqual(exp_class.system_hw_config, exp_dict['SystemHwConfig'])

    def test_profile_id_none(self):
        reply = models.profile.ProfileID.from_dict({'JsonSystemProfileIDResult': None})
        self.assertEqual(reply, [])

    def test_profile_id_empty(self):
        reply = models.profile.ProfileID.from_dict({'JsonSystemProfileIDResult': []})
        self.assertEqual(reply, [])

    def test_profile_id(self):
        reply = models.profile.ProfileID.from_dict(replies.profile.MOCK_PROFILE_ID_REPLY)
        self.assertEqual(len(reply), len(replies.profile.MOCK_PROFILE_ID_REPLY['JsonSystemProfileIDResult']))
        self.assertEqual(reply, [1, 3])

    def test_profile_none(self):
        reply = models.profile.ProfileWrapper.from_dict({'JsonSystemProfileResult': None})
        self.assertEqual(reply, None)

    def test_profile(self):
        reply = models.profile.ProfileWrapper.from_dict(replies.profile.MOCK_PROFILE_REPLY)
        self.profile_assertor(reply, replies.profile.MOCK_PROFILE_REPLY['JsonSystemProfileResult'])

    def test_profile_active_none(self):
        reply = models.profile.ProfileActive.from_dict({'JsonSystemProfileActiveResult': None})
        self.assertEqual(reply, None)

    def test_profile_active(self):
        reply = models.profile.ProfileActive.from_dict(replies.profile.MOCK_PROFILE_ACTIVE_REPLY)
        self.profile_assertor(reply, replies.profile.MOCK_PROFILE_ACTIVE_REPLY['JsonSystemProfileActiveResult'])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = ProfileModels()
    test_case.test_profile_id_none()
    test_case.test_profile_id_empty()
    test_case.test_profile_id()
    test_case.test_profile_none()
    test_case.test_profile()
    test_case.test_profile_active_none()
    test_case.test_profile_active()
