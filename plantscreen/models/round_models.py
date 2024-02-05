from dataclasses import dataclass
from typing import List
from typing import Any
import json


# Round baseclass
@dataclass
class Round:
    ActionID: int
    ExperimentID: int
    RoundDateStart: str
    RoundDateStop: str
    RoundDone: bool
    RoundID: int
    RoundProtocolPath: str
    RoundStatus: str

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        return Round(
            ActionID=obj.get("ActionID"),
            ExperimentID=obj.get("ExperimentID"),
            RoundDateStart=obj.get("RoundDateStart"),
            RoundDateStop=obj.get("RoundDateStop"),
            RoundDone=obj.get("RoundDone"),
            RoundID=obj.get("RoundID"),
            RoundProtocolPath=obj.get("RoundProtocolPath"),
            RoundStatus=obj.get("RoundStatus")
        )
    
# Order baseclass
@dataclass
class Order:
    ExperimentID: int
    Order: int
    RoundID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        return Order(
            ExperimentID=obj.get("ExperimentID"),
            Order=obj.get("Order"),
            RoundID=obj.get("RoundID"),
        )
    


# round by ID
@dataclass
class RoundWrapper:
    Round: Round

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        if obj.get("JsonRoundResult") is None:
            return None
        return Round.from_dict(obj.get("JsonRoundResult"))
    
# List rounds by experiment
@dataclass
class RoundExperiment:
    Round: Round

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        if obj.get("JsonRoundByExperimentIDResult") is None:
            return []
        return [Round.from_dict(y) for y in obj.get("JsonRoundByExperimentIDResult")]


# List rounds by experiment and date
@dataclass
class RoundDateExperiment:
    Round: Round

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        if obj.get("JsonRoundByExperimentIDAndDateResult") is None:
            return []
        return [Round.from_dict(y) for y in obj.get("JsonRoundByExperimentIDAndDateResult")]    

# Round order by round ID
@dataclass
class RoundOrderRound:
    Order: Order

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        if obj.get("JsonRoundOrderResult") is None:
            return None
        return Order.from_dict(obj.get("JsonRoundOrderResult"))

# Round order by experiment
@dataclass
class RoundOrderExperiment:
    Order: Order

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        if obj.get("JsonRoundOrderByExperimentIDResult") is None:
            return []
        return [Order.from_dict(y) for y in obj.get("JsonRoundOrderByExperimentIDResult")]    
    
# Round order by experiment and date
@dataclass
class RoundOrderDateExperiment:
    Order: Order

    @staticmethod
    def from_dict(obj: Any) -> 'Order':
        if obj.get("JsonRoundOrderByExperimentIDAndDateResult") is None:
            return []
        return [Order.from_dict(y) for y in obj.get("JsonRoundOrderByExperimentIDAndDateResult")]    
    

