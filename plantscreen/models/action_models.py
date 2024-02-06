from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Action:
    """Action baseclass"""
    action_date_start: str
    action_done: bool
    action_group_id: int
    action_id: int
    action_running: bool
    action_status: str
    experiment_id: int

    @staticmethod
    def from_dict(obj: Any) -> Action:
        return Action(
            action_date_start=obj.get("ActionDateStart"),
            action_done=obj.get("ActionDone"),
            action_group_id=obj.get("ActionGroupID"),
            action_id=obj.get("ActionID"),
            action_running=obj.get("ActionRunning"),
            action_status=obj.get("ActionStatus"),
            experiment_id=obj.get("ExperimentID")
        )


@dataclass
class NoAction:
    """NoAction baseclass"""
    action_id: int
    experiment_id: int
    action_group_id: int
    action_date_start: str
    action_status: str
    action_done: bool
    action_running: bool

    @staticmethod
    def from_dict(obj: Any) -> NoAction:
        return NoAction(
            action_id=obj.get("ActionID"),
            experiment_id=obj.get("ExperimentID"),
            action_group_id=obj.get("ActionGroupID"),
            action_date_start=obj.get("ActionDateStart"),
            action_status=obj.get("ActionStatus"),
            action_done=obj.get("ActionDone"),
            action_running=obj.get("ActionRunning")
        )


@dataclass
class Group:
    """Group baseclass"""
    action_protocol_id: int
    experiment_id: int
    group_caption: str
    group_id: int
    group_repeating_protocol: str

    @staticmethod
    def from_dict(obj: Any) -> Group:
        return Group(
            action_protocol_id=obj.get("ActionProtocolID"),
            experiment_id=obj.get("ExperimentID"),
            group_caption=obj.get("GroupCaption"),
            group_id=obj.get("GroupID"),
            group_repeating_protocol=obj.get("GroupRepeatingProtocol")
        )


@dataclass
class Protocol:
    """Protocol baseclass"""
    action_id: int
    experiment_id: int
    protocol_body: str
    protocol_date_changed: str
    protocol_id: int
    round_id: int

    @staticmethod
    def from_dict(obj: Any) -> Protocol:
        return Protocol(
            action_id=obj.get("ActionID"),
            experiment_id=obj.get("ExperimentID"),
            protocol_body=obj.get("ProtocolBody"),
            protocol_date_changed=obj.get("ProtocolDateChanged"),
            protocol_id=obj.get("ProtocolID"),
            round_id=obj.get("RoundID")
        )


@dataclass
class ActionWrapper:
    """Action by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Action:
        if obj.get("JsonActionResult") is None:
            return None
        return Action.from_dict(obj.get("JsonActionResult"))


@dataclass
class ActionExperiment:
    """Action by experiment"""

    @staticmethod
    def from_dict(obj: Any) -> List[Action]:
        if obj.get("JsonActionByExperimentIDResult") is None:
            return []
        return [Action.from_dict(y) for y in obj.get("JsonActionByExperimentIDResult")]


@dataclass
class ActionNotDoneExperiment:
    """Unfinished actions by experiment"""

    @staticmethod
    def from_dict(obj: Any) -> List[NoAction]:
        if obj.get("JsonActionByExperimentIDNotDoneResult") is None:
            return []
        return [NoAction.from_dict(y) for y in obj.get("JsonActionByExperimentIDNotDoneResult")]


@dataclass
class ActionGroup:
    """Scheduled actions by group ID"""

    @staticmethod
    def from_dict(obj: Any) -> Group:
        if obj.get("JsonActionGroupResult") is None:
            return None
        return Group.from_dict(obj.get("JsonActionGroupResult"))


@dataclass
class ActionGroupRound:
    """Scheduled actions by round ID"""

    @staticmethod
    def from_dict(obj: Any) -> Group:
        if obj.get("JsonActionGroupByRoundIDResult") is None:
            return None
        return Group.from_dict(obj.get("JsonActionGroupByRoundIDResult"))


@dataclass
class ActionProtocol:
    """Scheduled actions by protocol ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Protocol]:
        if obj.get("JsonActionProtocolResult") is None:
            return []
        return [Protocol.from_dict(y) for y in obj.get("JsonActionProtocolResult")]


@dataclass
class ActionProtocolRound:
    """Scheduled actions by protocol by round ID"""

    @staticmethod
    def from_dict(obj: Any) -> Protocol:
        if obj.get("JsonActionProtocolByRoundIDResult") is None:
            return None
        return Protocol.from_dict(obj.get("JsonActionProtocolByRoundIDResult"))
