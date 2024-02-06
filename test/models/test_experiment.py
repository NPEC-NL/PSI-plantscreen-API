"""Test experiment models"""
from contextlib import AbstractContextManager
from typing import Any
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class ExperimentModels(unittest.TestCase):
    def experiment_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.created_date, exp_dict['CreatedDate'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.experiment_info, exp_dict['ExperimentInfo'])
        self.assertEqual(exp_class.experiment_mame, exp_dict['ExperimentName'])
        self.assertEqual(exp_class.experiment_status, exp_dict['ExperimentStatus'])
        self.assertEqual(exp_class.owner_id, exp_dict['OwnerID'])
        self.assertEqual(exp_class.status_changed_date, exp_dict['StatusChangedDate'])

    def owner_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.create_date, exp_dict['CreateDate'])
        self.assertEqual(exp_class.email, exp_dict['Email'])
        self.assertEqual(exp_class.first_name, exp_dict['FirstName'])
        self.assertEqual(exp_class.last_failed_date, exp_dict['LastFailedDate'])
        self.assertEqual(exp_class.last_name, exp_dict['LastName'])
        self.assertEqual(exp_class.last_success_login, exp_dict['LastSuccessLogin'])
        self.assertEqual(exp_class.login, exp_dict['Login'])
        self.assertEqual(exp_class.owner_id, exp_dict['OwnerID'])
        self.assertEqual(exp_class.sms_phone_number, exp_dict['SmsPhoneNumber'])

    def note_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.note_created_date, exp_dict['NoteCreatedDate'])
        self.assertEqual(exp_class.note_id, exp_dict['NoteID'])
        self.assertEqual(exp_class.note_text, exp_dict['NoteText'])
        self.assertEqual(exp_class.owner_id, exp_dict['OwnerID'])

    def test_experiment_id_none(self):
        """"None reply"""
        reply = models.experiment.ExperimentIDs.from_dict({'JsonExperimentIDResult': None})
        self.assertEqual(reply, [])

    def test_experiment_id_empty(self):
        """"emply list reply"""
        reply = models.experiment.ExperimentIDs.from_dict({'JsonExperimentIDResult': []})
        self.assertEqual(reply, [])

    def test_experiment_id(self):
        reply = models.experiment.ExperimentIDs.from_dict(replies.experiment.MOCK_EXPERIMENT_ID_REPLY)
        self.assertEqual(len(reply), len(replies.experiment.MOCK_EXPERIMENT_ID_REPLY['JsonExperimentIDResult']))
        for i in range(0, len(replies.experiment.MOCK_EXPERIMENT_ID_REPLY['JsonExperimentIDResult'])):
            self.assertEqual(reply[i], replies.experiment.MOCK_EXPERIMENT_ID_REPLY['JsonExperimentIDResult'][i]['ExperimentID'])

    def test_experiment_wrapper_none(self):
        """"None reply"""
        reply = models.experiment.ExperimentWrapper.from_dict({'JsonExperimentResult': None})
        self.assertEqual(reply, None)

    def test_experiment_wrapper(self):
        reply = models.experiment.ExperimentWrapper.from_dict(replies.experiment.MOCK_EXPERIMENT_REPLY)
        self.experiment_assertor(reply, replies.experiment.MOCK_EXPERIMENT_REPLY['JsonExperimentResult'])

    def test_experiment_date_none(self):
        """"None reply"""
        reply = models.experiment.ExperimentDate.from_dict({'JsonExperimentByDateResult': None})
        self.assertEqual(reply, [])

    def test_experiment_date(self):
        reply = models.experiment.ExperimentDate.from_dict(replies.experiment.MOCK_EXPERIMENT_DATE_REPLY)
        self.experiment_assertor(reply[0], replies.experiment.MOCK_EXPERIMENT_DATE_REPLY['JsonExperimentByDateResult'][0])
        self.experiment_assertor(reply[1], replies.experiment.MOCK_EXPERIMENT_DATE_REPLY['JsonExperimentByDateResult'][1])

    def test_experiment_owner_none(self):
        """"None reply"""
        reply = models.experiment.ExperimentOwner.from_dict({'JsonExperimentByOwnerResult': None})
        self.assertEqual(reply, [])

    def test_experiment_owner(self):
        reply = models.experiment.ExperimentOwner.from_dict(replies.experiment.MOCK_EXPERIMENT_OWNER_REPLY)
        self.experiment_assertor(reply[0], replies.experiment.MOCK_EXPERIMENT_OWNER_REPLY['JsonExperimentByOwnerResult'][0])
        self.experiment_assertor(reply[1], replies.experiment.MOCK_EXPERIMENT_OWNER_REPLY['JsonExperimentByOwnerResult'][1])

    def test_experiment_owner_id_none(self):
        """"None reply"""
        reply = models.experiment.OwnerID.from_dict({'JsonOwnerIDResult': None})
        self.assertEqual(reply, [])

    def test_experiment_owner_id_empty(self):
        """"emply list reply"""
        reply = models.experiment.OwnerID.from_dict({'JsonOwnerIDResult': []})
        self.assertEqual(reply, [])

    def test_experiment_owner_id(self):
        reply = models.experiment.OwnerID.from_dict(replies.experiment.MOCK_OWNER_ID_REPLY)
        self.assertEqual(len(reply), len(replies.experiment.MOCK_OWNER_ID_REPLY['JsonOwnerIDResult']))
        for i in range(0, len(replies.experiment.MOCK_OWNER_ID_REPLY['JsonOwnerIDResult'])):
            self.assertEqual(reply[i], replies.experiment.MOCK_OWNER_ID_REPLY['JsonOwnerIDResult'][i]['OwnerID'])

    def test_experiment_owner_wrapper_none(self):
        """"None reply"""
        reply = models.experiment.OwnerWrapper.from_dict({'JsonOwnerIDResult': None})
        self.assertEqual(reply, [])

    def test_experiment_owner_wrapper_empty(self):
        """"emply list reply"""
        reply = models.experiment.OwnerWrapper.from_dict({'JsonOwnerIDResult': []})
        self.assertEqual(reply, [])

    def test_experiment_owner_wrapper(self):
        reply = models.experiment.OwnerWrapper.from_dict(replies.experiment.MOCK_OWNER_REPLY)
        self.owner_assertor(reply[0], replies.experiment.MOCK_OWNER_REPLY['JsonOwnerResult'][0])
        self.owner_assertor(reply[1], replies.experiment.MOCK_OWNER_REPLY['JsonOwnerResult'][1])

    def test_experiment_note_none(self):
        """"None reply"""
        reply = models.experiment.NoteExperiment.from_dict({'JsonNoteResult': None})
        self.assertEqual(reply, [])

    def test_experiment_note_empty(self):
        """"emply list reply"""
        reply = models.experiment.NoteExperiment.from_dict({'JsonNoteResult': []})
        self.assertEqual(reply, [])

    def test_experiment_note(self):
        reply = models.experiment.NoteExperiment.from_dict(replies.experiment.MOCK_NOTE_EXPERIMENT_REPLY)
        self.note_assertor(reply[0], replies.experiment.MOCK_NOTE_EXPERIMENT_REPLY['JsonNoteResult'][0])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = ExperimentModels()
    test_case.test_experiment_id_none()
    test_case.test_experiment_id_empty()
    test_case.test_experiment_id()
    test_case.test_experiment_wrapper_none()
    test_case.test_experiment_wrapper()
    test_case.test_experiment_date_none()
    test_case.test_experiment_date()
    test_case.test_experiment_owner_none()
    test_case.test_experiment_owner()
    test_case.test_experiment_owner_id_none()
    test_case.test_experiment_owner_id()
    test_case.test_experiment_owner_wrapper_none()
    test_case.test_experiment_owner_wrapper_empty()
    test_case.test_experiment_owner_wrapper()
    test_case.test_experiment_note_empty()
    test_case.test_experiment_note()
