"""Test experiment models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class DeviceModels(unittest.TestCase):
    def device_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.device_caption, exp_dict['DeviceCaption'])
        self.assertEqual(exp_class.device_config, exp_dict['DeviceConfig'])
        self.assertEqual(exp_class.device_family, exp_dict['DeviceFamily'])
        self.assertEqual(exp_class.device_id, exp_dict['DeviceID'])
        self.assertEqual(exp_class.device_name, exp_dict['DeviceName'])
        self.assertEqual(exp_class.device_pid, exp_dict['DevicePID'])
        self.assertEqual(exp_class.device_type, exp_dict['DeviceType'])
        self.assertEqual(exp_class.device_validity_end, exp_dict['DeviceValidityEnd'])
        self.assertEqual(exp_class.device_validity_start, exp_dict['DeviceValidityStart'])
        self.assertEqual(exp_class.profile_id, exp_dict['ProfileID'])

    def test_device_none(self):
        reply = models.device.DeviceWrapper.from_dict({'JsonDeviceResult': None})
        self.device_assertor(reply, None)

    def test_device(self):
        reply = models.device.DeviceWrapper.from_dict(replies.devices.MOCK_DEVICE_REPLY)
        self.device_assertor(reply, replies.devices.MOCK_DEVICE_REPLY['JsonDeviceResult'])

    def test_device_active_none(self):
        reply = models.device.DeviceActive.from_dict({'JsonExperimentIDResult': None})
        self.assertEqual(reply, [])

    def test_device_active_empty(self):
        reply = models.device.DeviceActive.from_dict({'JsonExperimentIDResult': []})
        self.assertEqual(reply, [])

    def test_device_active(self):
        reply = models.device.DeviceActive.from_dict(replies.devices.MOCK_DEVICE_ACTIVE_REPLY)
        self.assertEqual(len(reply), len(replies.devices.MOCK_DEVICE_ACTIVE_REPLY['JsonDeviceActiveResult']))
        for i in range(0, len(replies.devices.MOCK_DEVICE_ACTIVE_REPLY['JsonDeviceActiveResult'])):
            self.device_assertor(reply[i], replies.devices.MOCK_DEVICE_ACTIVE_REPLY['JsonDeviceActiveResult'][i])

    def test_device_profile_none(self):
        reply = models.device.DeviceProfile.from_dict({'JsonDeviceByProfileIDResult': None})
        self.assertEqual(reply, [])

    def test_device_profile_empty(self):
        reply = models.device.DeviceProfile.from_dict({'JsonDeviceByProfileIDResult': []})
        self.assertEqual(reply, [])

    def test_device_profile(self):
        reply = models.device.DeviceProfile.from_dict(replies.devices.MOCK_DEVICE_PROFILE_REPLY)
        self.assertEqual(len(reply), len(replies.devices.MOCK_DEVICE_PROFILE_REPLY['JsonDeviceByProfileIDResult']))
        for i in range(0, len(replies.devices.MOCK_DEVICE_PROFILE_REPLY['JsonDeviceByProfileIDResult'])):
            self.device_assertor(reply[i], replies.devices.MOCK_DEVICE_PROFILE_REPLY['JsonDeviceByProfileIDResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = DeviceModels()
    test_case.test_device_none()
    test_case.test_device()
    test_case.test_device_active_none()
    test_case.test_device_active_empty()
    test_case.test_device_active()
    test_case.test_device_profile_none()
    test_case.test_device_profile_empty()
    test_case.test_device_profile()
