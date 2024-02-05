from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Action baseclass
@dataclass
class Action:
    ActionDateStart: str
    ActionDone: bool
    ActionGroupID: int
    ActionID: int
    ActionRunning: bool
    ActionStatus: str
    ExperimentID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        return Action(
            ActionDateStart=obj.get("ActionDateStart"),
            ActionDone=obj.get("ActionDone"),
            ActionGroupID=obj.get("ActionGroupID"),
            ActionID=obj.get("ActionID"),
            ActionRunning=obj.get("ActionRunning"),
            ActionStatus=obj.get("ActionStatus"),
            ExperimentID=obj.get("ExperimentID")
        )


# NoAction baseclass
@dataclass
class NoAction:
    ActionID: int
    ExperimentID: int
    ActionGroupID: int   
    ActionDateStart: str
    ActionStatus: str
    ActionDone: bool
    ActionRunning: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        return Action(
            ActionID=obj.get("ActionID"),
            ExperimentID=obj.get("ExperimentID"),
            ActionGroupID=obj.get("ActionGroupID"),
            ActionDateStart=obj.get("ActionDateStart"),
            ActionStatus=obj.get("ActionStatus"),
            ActionDone=obj.get("ActionDone"),
            ActionRunning=obj.get("ActionRunning")
        )

# Group baseclass
@dataclass
class Group:
    ActionProtocolID: int
    ExperimentID: int
    GroupCaption: str
    GroupID: int
    GroupRepeatingProtocol: str

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        return Group(
            ActionProtocolID=obj.get("ActionProtocolID"),
            ExperimentID=obj.get("ExperimentID"),
            GroupCaption=obj.get("GroupCaption"),
            GroupID=obj.get("GroupID"),
            GroupRepeatingProtocol=obj.get("GroupRepeatingProtocol")
        )

# Protocol baseclass
@dataclass
class Protocol:
    ActionID: int
    ExperimentID: int
    ProtocolBody: str
    ProtocolDateChanged: str
    ProtocolID: int
    RoundID: int


    @staticmethod
    def from_dict(obj: Any) -> 'Protocol':
        return Protocol(
            ActionID=obj.get("ActionID"),
            ExperimentID=obj.get("ExperimentID"),
            ProtocolBody=obj.get("ProtocolBody"),
            ProtocolDateChanged=obj.get("ProtocolDateChanged"),
            ProtocolID=obj.get("ProtocolID"),
            RoundID=obj.get("RoundID")
        )
    


# Action by ID
@dataclass
class ActionWrapper:
    Action: Action

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        return Action.from_dict(obj.get("JsonActionResult"))
    

# Action by experiment
@dataclass
class ActionExperiment:
    Action: Action

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        return [Action.from_dict(y) for y in obj.get("JsonActionByExperimentIDResult")]

# Unfinished actions by experiment
@dataclass
class ActionNotDoneExperiment:
    NoAction: NoAction

    @staticmethod
    def from_dict(obj: Any) -> 'NoAction':
        return [NoAction.from_dict(y) for y in obj.get("JsonActionByExperimentIDNotDoneResult")]

# Scheduled actions by group ID
@dataclass
class ActionGroup:
    Group: Group

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        return Group.from_dict(obj.get("JsonActionGroupResult"))

# Scheduled actions by round ID
@dataclass
class ActionGroupRound:
    Group: Group

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        return Group.from_dict(obj.get("JsonActionGroupByRoundIDResult"))  
    
# Scheduled actions by protocol ID
@dataclass
class ActionProtocol:
    Protocol: Protocol

    @staticmethod
    def from_dict(obj: Any) -> 'Protocol':
        return [Protocol.from_dict(y) for y in obj.get("JsonActionProtocolResult")]
    
# Scheduled actions by protocol by round ID
@dataclass
class ActionProtocolRound:
    Protocol: Protocol

    @staticmethod
    def from_dict(obj: Any) -> 'Protocol':
        return Protocol.from_dict(obj.get("JsonActionProtocolByRoundIDResult"))  
    
    