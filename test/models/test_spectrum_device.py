"""Test experiment models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class SpectrumDeviceModels(unittest.TestCase):
    def test_spectrum_devices_empty(self):
        """"emply list reply"""
        reply = models.spectrum_device.SpectrumDeviceIDs.from_dict({'json_spectrum_device_id_result': []})
        self.assertEqual(reply, [])

    def test_spectrum_devices(self):
        reply = models.spectrum_device.SpectrumDeviceIDs.from_dict(replies.spectum_device.MOCK_SPECTRUMDEVICE_ID_JSON)
        self.assertEqual(len(reply), len(replies.spectum_device.MOCK_SPECTRUMDEVICE_ID_JSON['json_spectrum_device_id_result']))
        for i in range(0, len(replies.spectum_device.MOCK_SPECTRUMDEVICE_ID_JSON['json_spectrum_device_id_result'])):
            self.assertEqual(reply[i], replies.spectum_device.MOCK_SPECTRUMDEVICE_ID_JSON['json_spectrum_device_id_result'][i]['spectrum_device_id'])



if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = SpectrumDeviceModels()
    test_case.test_spectrum_devices_empty()
    test_case.test_spectrum_devices()
