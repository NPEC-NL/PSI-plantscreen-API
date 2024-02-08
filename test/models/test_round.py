"""Test round models"""
import unittest

from os import path
import sys

# Add the parent folder to the path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
sys.path.append(path.dirname(path.dirname(path.realpath(__file__))))
from plantscreen import models
import replies


class RoundModels(unittest.TestCase):
    def round_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.action_id, exp_dict['ActionID'])
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.round_date_start, exp_dict['RoundDateStart'])
        self.assertEqual(exp_class.round_date_stop, exp_dict['RoundDateStop'])
        self.assertEqual(exp_class.round_done, exp_dict['RoundDone'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])
        self.assertEqual(exp_class.round_protocol_path, exp_dict['RoundProtocolPath'])
        self.assertEqual(exp_class.round_status, exp_dict['RoundStatus'])

    def order_assertor(self, exp_class, exp_dict):
        self.assertEqual(exp_class.experiment_id, exp_dict['ExperimentID'])
        self.assertEqual(exp_class.order, exp_dict['Order'])
        self.assertEqual(exp_class.round_id, exp_dict['RoundID'])

    def test_round_none(self):
        reply = models.round.RoundWrapper.from_dict({'JsonRoundResult': None})
        self.round_assertor(reply, None)

    def test_round(self):
        reply = models.round.RoundWrapper.from_dict(replies.rounds.MOCK_Round_REPLY)
        self.round_assertor(reply, replies.rounds.MOCK_Round_REPLY['JsonRoundResult'])

    def test_round_experiment_none(self):
        reply = models.round.RoundExperiment.from_dict({'JsonRoundByExperimentIDResult': None})
        self.assertEqual(reply, [])

    def test_round_experiment_empty(self):
        reply = models.round.RoundExperiment.from_dict({'JsonRoundByExperimentIDResult': []})
        self.assertEqual(reply, [])

    def test_round_experiment(self):
        reply = models.round.RoundExperiment.from_dict(replies.rounds.MOCK_ROUND_EXPERIMENT_REPLY)
        self.assertEqual(len(reply), len(replies.rounds.MOCK_ROUND_EXPERIMENT_REPLY['JsonRoundByExperimentIDResult']))
        for i in range(0, len(replies.rounds.MOCK_ROUND_EXPERIMENT_REPLY['JsonRoundByExperimentIDResult'])):
            self.round_assertor(reply[i], replies.rounds.MOCK_ROUND_EXPERIMENT_REPLY['JsonRoundByExperimentIDResult'][i])

    def test_round_date_experiment_none(self):
        reply = models.round.RoundDateExperiment.from_dict({'JsonRoundByExperimentIDAndDateResult': None})
        self.assertEqual(reply, [])

    def test_round_date_experiment_empty(self):
        reply = models.round.RoundDateExperiment.from_dict({'JsonRoundByExperimentIDAndDateResult': []})
        self.assertEqual(reply, [])

    def test_round_date_experiment(self):
        reply = models.round.RoundDateExperiment.from_dict(replies.rounds.MOCK_ROUND_DATE_EXPERIMENT_REPLY)
        self.assertEqual(len(reply), len(replies.rounds.MOCK_ROUND_DATE_EXPERIMENT_REPLY['JsonRoundByExperimentIDAndDateResult']))
        for i in range(0, len(replies.rounds.MOCK_ROUND_DATE_EXPERIMENT_REPLY['JsonRoundByExperimentIDAndDateResult'])):
            self.round_assertor(reply[i],
                                replies.rounds.MOCK_ROUND_DATE_EXPERIMENT_REPLY['JsonRoundByExperimentIDAndDateResult'][i])

    def test_round_order_round_none(self):
        reply = models.round.RoundOrderRound.from_dict({'JsonRoundOrderResult': None})
        self.order_assertor(reply, None)

    def test_round_order_round(self):
        reply = models.round.RoundOrderRound.from_dict(replies.rounds.MOCK_ROUND_ORDER_ROUND_REPLY)
        self.order_assertor(reply, replies.rounds.MOCK_ROUND_ORDER_ROUND_REPLY['JsonRoundOrderResult'])

    def test_round_order_experiment_none(self):
        reply = models.round.RoundOrderExperiment.from_dict({'JsonRoundOrderByExperimentIDResult': None})
        self.assertEqual(reply, [])

    def test_round_order_experiment_empty(self):
        reply = models.round.RoundOrderExperiment.from_dict({'JsonRoundOrderByExperimentIDResult': []})
        self.assertEqual(reply, [])

    def test_round_order_experiment(self):
        reply = models.round.RoundOrderExperiment.from_dict(replies.rounds.MOCK_ROUND_ORDER_EXPERIMENT_REPLY)
        self.assertEqual(len(reply), len(replies.rounds.MOCK_ROUND_ORDER_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDResult']))
        for i in range(0, len(replies.rounds.MOCK_ROUND_ORDER_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDResult'])):
            self.round_assertor(reply[i],
                                replies.rounds.MOCK_ROUND_ORDER_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDResult'][i])

    def test_round_order_date_experiment_none(self):
        reply = models.round.RoundOrderDateExperiment.from_dict({'JsonRoundOrderByExperimentIDAndDateResult': None})
        self.assertEqual(reply, [])

    def test_round_order_date_experiment_empty(self):
        reply = models.round.RoundOrderDateExperiment.from_dict({'JsonRoundOrderByExperimentIDAndDateResult': []})
        self.assertEqual(reply, [])

    def test_round_order_date_experiment(self):
        reply = models.round.RoundOrderDateExperiment.from_dict(replies.rounds.MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY)
        self.assertEqual(len(reply),
                         len(replies.rounds.MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDAndDateResult']))
        for i in range(0,
                       len(replies.rounds.MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDAndDateResult'])):
            self.round_assertor(reply[i],
                                replies.rounds.MOCK_ROUND_ORDER_DATE_EXPERIMENT_REPLY['JsonRoundOrderByExperimentIDAndDateResult'][i])


if __name__ == "__main__":
    """"Helper for debugging purposes"""
    test_case = RoundModels()
    test_case.test_round_none()
    test_case.test_round()
    test_case.test_round_experiment_none()
    test_case.test_round_experiment_empty()
    test_case.test_round_experiment()
    test_case.test_round_date_experiment_none()
    test_case.test_round_date_experiment_empty()
    test_case.test_round_date_experiment()
    test_case.test_round_order_round_none()
    test_case.test_round_order_round()
    test_case.test_round_order_experiment_none()
    test_case.test_round_order_experiment_empty()
    test_case.test_round_order_experiment()
    test_case.test_round_order_date_experiment_none()
    test_case.test_round_order_date_experiment_empty()
    test_case.test_round_order_date_experiment()
