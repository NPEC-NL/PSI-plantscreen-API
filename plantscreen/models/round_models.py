from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Round:
    """Round baseclass"""
    action_id: int
    experiment_id: int
    round_date_start: str
    round_date_stop: str
    round_done: bool
    round_id: int
    round_protocol_path: str
    round_status: str

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        return Round(
            action_id=obj.get("ActionID"),
            experiment_id=obj.get("ExperimentID"),
            round_date_start=obj.get("RoundDateStart"),
            round_date_stop=obj.get("RoundDateStop"),
            round_done=obj.get("RoundDone"),
            round_id=obj.get("RoundID"),
            round_protocol_path=obj.get("RoundProtocolPath"),
            round_status=obj.get("RoundStatus")
        )


@dataclass
class Order:
    """Order baseclass"""
    experiment_id: int
    order: int
    round_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        return Order(
            experiment_id=obj.get("ExperimentID"),
            order=obj.get("Order"),
            round_id=obj.get("RoundID")
        )


@dataclass
class RoundWrapper:
    """Round by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Round:
        if obj.get("JsonRoundResult") is None:
            return None
        return Round.from_dict(obj.get("JsonRoundResult"))


@dataclass
class RoundExperiment:
    """List rounds by experiment"""

    @staticmethod
    def from_dict(obj: Any) -> List[Round]:
        if obj.get("JsonRoundByExperimentIDResult") is None:
            return []
        return [Round.from_dict(y) for y in obj.get("JsonRoundByExperimentIDResult")]


@dataclass
class RoundDateExperiment:
    """List rounds by experiment and date"""

    @staticmethod
    def from_dict(obj: Any) -> List[Round]:
        if obj.get("JsonRoundByExperimentIDAndDateResult") is None:
            return []
        return [Round.from_dict(y) for y in obj.get("JsonRoundByExperimentIDAndDateResult")]


@dataclass
class RoundOrderRound:
    """Round order by round ID"""

    @staticmethod
    def from_dict(obj: Any) -> Order:
        if obj.get("JsonRoundOrderResult") is None:
            return None
        return Order.from_dict(obj.get("JsonRoundOrderResult"))


@dataclass
class RoundOrderExperiment:
    """Round order by experiment"""

    @staticmethod
    def from_dict(obj: Any) -> List[Order]:
        if obj.get("JsonRoundOrderByExperimentIDResult") is None:
            return []
        return [Order.from_dict(y) for y in obj.get("JsonRoundOrderByExperimentIDResult")]


@dataclass
class RoundOrderDateExperiment:
    """Round order by experiment and date"""

    @staticmethod
    def from_dict(obj: Any) -> List[Order]:
        if obj.get("JsonRoundOrderByExperimentIDAndDateResult") is None:
            return []
        return [Order.from_dict(y) for y in obj.get("JsonRoundOrderByExperimentIDAndDateResult")]
