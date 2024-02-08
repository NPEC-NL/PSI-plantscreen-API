"""Test action models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class ActionModels(unittest.TestCase):
    def action_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.action_date_start, exp_dict['ActionDateStart'])
        self.assertEqual(exp_class.action_done, exp_dict['ActionDone'])
        self.assertEqual(exp_class.action_group_id, exp_dict['ActionGroupID'])
        self.assertEqual(exp_class.action_id, exp_dict['ActionID'])
        self.assertEqual(exp_class.action_running, exp_dict['ActionRunning'])
        self.assertEqual(exp_class.action_status, exp_dict['ActionStatus'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])

    def group_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.action_protocol_id, exp_dict['ActionProtocolID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.group_caption, exp_dict['GroupCaption'])
        self.assertEqual(exp_class.group_id, exp_dict['GroupID'])
        self.assertEqual(exp_class.group_repeating_protocol, exp_dict['GroupRepeatingProtocol'])

    def protocol_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.action_id, exp_dict['ActionID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.protocol_body, exp_dict['ProtocolBody'])
        self.assertEqual(exp_class.protocol_date_changed, exp_dict['ProtocolDateChanged'])
        self.assertEqual(exp_class.protocol_id, exp_dict['ProtocolID'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])

    def test_action_none(self):
        reply = models.action.ActionWrapper.from_dict({'JsonActionResult':None})
        self.action_assertor(reply, None)

    def test_action(self):
        reply = models.action.ActionWrapper.from_dict(replies.action.MOCK_ACTION_REPLY)
        self.action_assertor(reply, replies.action.MOCK_ACTION_REPLY['JsonActionResult'])

    def test_action_experiment_none(self):
        reply = models.action.ActionExperiment.from_dict({'JsonActionByExperimentIDResult': None})
        self.assertEqual(reply, [])

    def test_action_experiment_empty(self):
        reply = models.action.ActionExperiment.from_dict({'JsonActionByExperimentIDResult': []})
        self.assertEqual(reply, [])

    def test_action_experiment(self):
        reply = models.action.ActionExperiment.from_dict(replies.action.MOCK_ACTION_EXPERIMENT_REPLY)
        self.assertEqual(len(reply), len(replies.action.MOCK_ACTION_EXPERIMENT_REPLY['JsonActionByExperimentIDResult']))
        for i in range(0, len(replies.action.MOCK_ACTION_EXPERIMENT_REPLY['JsonActionByExperimentIDResult'])):
            self.action_assertor(reply[i], replies.action.MOCK_ACTION_EXPERIMENT_REPLY['JsonActionByExperimentIDResult'][i])

    def test_action_not_done_experiment_none(self):
        reply = models.action.ActionNotDoneExperiment.from_dict({'JsonActionByExperimentIDNotDoneResult': None})
        self.assertEqual(reply, [])

    def test_action_not_done_experiment_empty(self):
        reply = models.action.ActionNotDoneExperiment.from_dict({'JsonActionByExperimentIDNotDoneResult': []})
        self.assertEqual(reply, [])

    def test_action_not_done_experiment(self):
        reply = models.action.ActionNotDoneExperiment.from_dict(replies.action.MOCK_ACTION_NOT_DONE_EXPERIMENT_REPLY)
        self.assertEqual(len(reply),
                         len(replies.action.MOCK_ACTION_NOT_DONE_EXPERIMENT_REPLY['JsonActionByExperimentIDNotDoneResult']))
        for i in range(0,
                       len(replies.action.MOCK_ACTION_NOT_DONE_EXPERIMENT_REPLY['JsonActionByExperimentIDNotDoneResult'])):
            self.action_assertor(reply[i],
                                 replies.action.MOCK_ACTION_NOT_DONE_EXPERIMENT_REPLY['JsonActionByExperimentIDNotDoneResult'][i])

    def test_action_group_none(self):
        reply = models.action.ActionGroup.from_dict(replies.action.MOCK_ACTION_GROUP_REPLY)
        self.group_assertor(reply, replies.action.MOCK_ACTION_GROUP_REPLY['JsonActionGroupResult'])

    def test_action_group(self):
        reply = models.action.ActionGroup.from_dict({'JsonActionGroupResult': None})
        self.group_assertor(reply, None)

    def test_action_group_round_none(self):
        reply = models.action.ActionGroupRound.from_dict({'JsonActionGroupByRoundIDResult': None})
        self.group_assertor(reply, None)        

    def test_action_group_round(self):
        reply = models.action.ActionGroupRound.from_dict(replies.action.MOCK_ACTION_GROUP_ROUND_REPLY)
        self.group_assertor(reply, replies.action.MOCK_ACTION_GROUP_ROUND_REPLY['JsonActionGroupByRoundIDResult'])

    def test_action_protocol_none(self):
        reply = models.action.ActionProtocol.from_dict({'JsonActionProtocolResult': None})
        self.assertEqual(reply, [])

    def test_action_protocol(self):
        reply = models.action.ActionProtocol.from_dict(replies.action.MOCK_ACTION_PROTOCOL_REPLY)
        self.protocol_assertor(reply, replies.action.MOCK_ACTION_PROTOCOL_REPLY['JsonActionProtocolResult'])

    def test_action_protocol_round_none(self):
        reply = models.action.ActionProtocolRound.from_dict({'JsonActionProtocolByRoundIDResult': None})
        self.protocol_assertor(reply, None)

    def test_action_protocol_round(self):
        reply = models.action.ActionProtocolRound.from_dict(replies.action.MOCK_ACTION_PROTOCOL_ROUND_REPLY)
        self.protocol_assertor(reply, replies.action.MOCK_ACTION_PROTOCOL_ROUND_REPLY['JsonActionProtocolByRoundIDResult'])


if __name__ == "__main__":
    """"Helper for debugging purposes""" 
    test_case = ActionModels()
    test_case.test_action_none()
    test_case.test_action()
    test_case.test_action_experiment_none()
    test_case.test_action_experiment_empty()
    test_case.test_action_experiment()
    test_case.test_action_not_done_experiment_none()
    test_case.test_action_not_done_experiment_empty()
    test_case.test_action_not_done_experiment()
    test_case.test_action_group_none()
    test_case.test_action_group()
    test_case.test_action_group_round_none()
    test_case.test_action_group_round()
    test_case.test_action_protocol_none()
    test_case.test_action_protocol()
    test_case.test_action_protocol_round_none()
    test_case.test_action_protocol_round()
