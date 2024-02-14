"""Plantscreen API tests"""
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

import mocks
import replies
# Add the parent folder to the path
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from plantscreen import admin_api


@patch('plantscreen.PSI_api.swagger_client', mocks.SwaggerMock())
class MyTestCase(unittest.TestCase):
    def test_init(self):
        """Test the class instantiation"""
        with patch('plantscreen.PSI_api.swagger_client', mocks.SwaggerMock()) as api_mock:
            api = admin_api.PSI_API('test', '33')
            api_mock.Configuration.assert_called_once()
            self.assertEqual(api_mock.Configuration.return_value.host, 'test:33/RestService/json')

    def test_experiment_id(self):
        api = admin_api.PSI_API('test', '33')
        reply = api.experimentID()
        api.exp_api.experiment_id.assert_called_once()
        self.assertEqual(len(reply), len(replies.experiment.MOCK_EXPERIMENT_ID_REPLY['JsonExperimentIDResult']))
        self.assertEqual(reply[0], replies.experiment.MOCK_EXPERIMENT_ID_REPLY['JsonExperimentIDResult'][0]['ExperimentID'])

    def test_experiment_wrapper(self):
        api = admin_api.PSI_API('test', '33')
        reply = api.experiment(72)
        api.exp_api.experiment.assert_called_once()
        self.assertEqual(api.exp_api.experiment.call_args[0][0], 72)
        self.assertEqual(reply.experiment_id, replies.experiment.MOCK_EXPERIMENT_REPLY['JsonExperimentResult']['ExperimentID'])

    def test_experiment_date(self):
        api = admin_api.PSI_API('test', '33')
        start_date = datetime(year=2023, month=9, day=1)
        end_date = datetime(year=2023, month=9, day=1)
        reply = api.experiment_date(start_date, end_date)
        api.exp_api.experiment_date.assert_called_once()
        self.assertEqual(api.exp_api.experiment_date.call_args[0][0], start_date)
        self.assertEqual(api.exp_api.experiment_date.call_args[0][1], end_date)
        self.assertEqual(reply[0].experiment_id, replies.experiment.MOCK_EXPERIMENT_DATE_REPLY['JsonExperimentByDateResult'][0]['ExperimentID'])



if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = MyTestCase()
    test_case.test_init()
    test_case.test_experiment_id()
    test_case.test_experiment_wrapper()
    test_case.test_experiment_date()
