from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class SystemLog:
    """SystemLog baseclass"""
    experiment_id: int
    log_date: str
    log_id: int
    log_tag: str
    log_text: str
    log_type: str
    round_id: int
    tray_barcode: str
    tray_id: int
    tray_profile_id: int

    @staticmethod
    def from_dict(obj: Any) -> SystemLog:
        return SystemLog(
            experiment_id=obj.get("ExperimentID"),
            log_date=obj.get("LogDate"),
            log_id=obj.get("LogID"),
            log_tag=obj.get("LogTag"),
            log_text=obj.get("LogText"),
            log_type=obj.get("LogType"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_profile_id=obj.get("TrayProfileID")
        )


@dataclass
class SystemLogType:
    """SystemLogType baseclass"""
    log_type: str

    @staticmethod
    def from_dict(obj: Any) -> SystemLogType:
        return SystemLogType(
            log_type=obj.get("LogType")
        )


@dataclass
class SystemLogTag:
    """SystemLogTag baseclass"""
    log_tag: str

    @staticmethod
    def from_dict(obj: Any) -> SystemLogTag:
        return SystemLogTag(
            log_tag=obj.get("LogTag")
        )


@dataclass
class SystemLogRound:
    """System Log by Round ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByRoundIDResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByRoundIDResult")]


@dataclass
class SystemLogDateRound:
    """System Log by Round ID and Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByRoundIDAndDateResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByRoundIDAndDateResult")]


@dataclass
class SystemLogTray:
    """System Log by Tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByTrayIDResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByTrayIDResult")]


@dataclass
class SystemLogDateTray:
    """System Log by Tray ID and Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByTrayIDAndDateResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByTrayIDAndDateResult")]


@dataclass
class SystemLogLogType:
    """System Log Type"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLogType]:
        if obj.get("JsonSystemLogTypeResult") is None:
            return []
        return [SystemLogType.from_dict(y) for y in obj.get("JsonSystemLogTypeResult")]


@dataclass
class SystemLogDateLogType:
    """System Log by Log Type and Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByLogTypeAndDateResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByLogTypeAndDateResult")]


@dataclass
class SystemLogLogTag:
    """System Log Tag"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLogTag]:
        if obj.get("JsonSystemLogTagResult") is None:
            return []
        return [SystemLogTag.from_dict(y) for y in obj.get("JsonSystemLogTagResult")]


@dataclass
class SystemLogDateLogTag:
    """System Log by Log Tag and Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[SystemLog]:
        if obj.get("JsonSystemLogByLogTagAndDateResult") is None:
            return []
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByLogTagAndDateResult")]
