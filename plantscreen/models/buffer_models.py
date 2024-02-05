from dataclasses import dataclass
from typing import List
from typing import Any
import json

# BufferHistory baseclass
@dataclass
class BufferHistory:
    BufferOccasion: str
    BufferStateDate: str
    BufferStateID: int
    BufferStatePath: str

    @staticmethod
    def from_dict(obj: Any) -> 'BufferHistory':
        return BufferHistory(
            BufferOccasion=obj.get("BufferOccasion"),
            BufferStateDate=obj.get("BufferStateDate"),
            BufferStateID=obj.get("BufferStateID"),
            BufferStatePath=obj.get("BufferStatePath")
        )

# Buffer History
@dataclass
class getBufferHistory:
    BufferHistory: BufferHistory

    @staticmethod
    def from_dict(obj: Any) -> 'BufferHistory':
        if obj.get("JsonBufferHistoryResult") is None:
            return None
        return BufferHistory.from_dict(obj.get("JsonBufferHistoryResult"))

# Buffer History by Date
@dataclass
class getBufferHistoryDate:
    BufferHistory: BufferHistory

    @staticmethod
    def from_dict(obj: Any) -> 'BufferHistory':
        if obj.get("JsonBufferHistoryByDateResult") is None:
            return None
        return [BufferHistory.from_dict(y) for y in obj.get("JsonBufferHistoryByDateResult")] 
    