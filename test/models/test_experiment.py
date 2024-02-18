"""Test experiment models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class ExperimentModels(unittest.TestCase):
    def test_experiment_id_empty(self):
        """"emply list reply"""
        reply = models.experiment.ExperimentIDs.from_dict({'json_experiment_id_result': []})
        self.assertEqual(reply, [])

    def test_experiment_id(self):
        reply = models.experiment.ExperimentIDs.from_dict(replies.experiment.MOCK_EXPERIMENT_ID_JSON)
        self.assertEqual(len(reply), len(replies.experiment.MOCK_EXPERIMENT_ID_JSON['json_experiment_id_result']))
        for i in range(0, len(replies.experiment.MOCK_EXPERIMENT_ID_JSON['json_experiment_id_result'])):
            self.assertEqual(reply[i], replies.experiment.MOCK_EXPERIMENT_ID_JSON['json_experiment_id_result'][i]['experiment_id'])

    def test_experiment_owner_id_empty(self):
        """"emply list reply"""
        reply = models.experiment.OwnerID.from_dict({'json_owner_id_result': []})
        self.assertEqual(reply, [])

    def test_experiment_owner_id(self):
        reply = models.experiment.OwnerID.from_dict(replies.experiment.MOCK_OWNER_ID_JSON)
        self.assertEqual(len(reply), len(replies.experiment.MOCK_OWNER_ID_JSON['json_owner_id_result']))
        for i in range(0, len(replies.experiment.MOCK_OWNER_ID_JSON['json_owner_id_result'])):
            self.assertEqual(reply[i], replies.experiment.MOCK_OWNER_ID_JSON['json_owner_id_result'][i]['owner_id'])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = ExperimentModels()
    test_case.test_experiment_id_empty()
    test_case.test_experiment_id()
    test_case.test_experiment_owner_id()
