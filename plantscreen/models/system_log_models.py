from dataclasses import dataclass
from typing import List
from typing import Any
import json

# SystemLog baseclass
@dataclass
class SystemLog:
    ExperimentID: int
    LogDate: str
    LogID: int
    LogTag: str
    LogText: str
    LogType: str
    RoundID: int
    TrayBarcode: str
    TrayID: int
    TrayProfileID: int

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        return SystemLog(
            ExperimentID=obj.get("ExperimentID"),
            LogDate=obj.get("LogDate"),
            LogID=obj.get("LogID"),
            LogTag=obj.get("LogTag"),
            LogText=obj.get("LogText"),
            LogType=obj.get("LogType"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayProfileID=obj.get("TrayProfileID")
        )

# SystemLogType baseclass
@dataclass
class SystemLogType:
    LogType: str

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLogType':
        return SystemLogType(
            LogType=obj.get("LogType")
        )

# SystemLogTag baseclass
@dataclass
class SystemLogTag:
    LogTag: str

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLogTag':
        return SystemLogTag(
            LogTag=obj.get("LogTag")
        )

# System Log by Round ID
@dataclass
class getSystemLogRound:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByRoundIDResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByRoundIDResult")] 

# System Log by Round ID and Date
@dataclass
class getSystemLogDateRound:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByRoundIDAndDateResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByRoundIDAndDateResult")] 

# System Log by Tray ID
@dataclass
class getSystemLogTray:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByTrayIDResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByTrayIDResult")] 

# System Log by Tray ID and Date
@dataclass
class getSystemLogDateTray:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByTrayIDAndDateResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByTrayIDAndDateResult")] 

# System Log Type 
@dataclass
class getSystemLogLogType:
    SystemLogType: SystemLogType

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLogType':
        if obj.get("JsonSystemLogTypeResult") is None:
            return None
        return [SystemLogType.from_dict(y) for y in obj.get("JsonSystemLogTypeResult")] 

# System Log by Log Type and Date
@dataclass
class getSystemLogDateLogType:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByLogTypeAndDateResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByLogTypeAndDateResult")] 

# System Log Tag
@dataclass
class getSystemLogLogTag:
    SystemLogTag: SystemLogTag

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLogTag':
        if obj.get("JsonSystemLogTagResult") is None:
            return None
        return [SystemLogTag.from_dict(y) for y in obj.get("JsonSystemLogTagResult")] 

# System Log by Log Tag and Date
@dataclass
class getSystemLogDateLogTag:
    SystemLog: SystemLog

    @staticmethod
    def from_dict(obj: Any) -> 'SystemLog':
        if obj.get("JsonSystemLogByLogTagAndDateResult") is None:
            return None
        return [SystemLog.from_dict(y) for y in obj.get("JsonSystemLogByLogTagAndDateResult")] 






