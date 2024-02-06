from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class BufferHistory:
    """BufferHistory baseclass"""
    buffer_occasion: str
    buffer_state_date: str
    buffer_state_id: int
    buffer_state_path: str

    @staticmethod
    def from_dict(obj: Any) -> BufferHistory:
        return BufferHistory(
            buffer_occasion=obj.get("BufferOccasion"),
            buffer_state_date=obj.get("BufferStateDate"),
            buffer_state_id=obj.get("BufferStateID"),
            buffer_state_path=obj.get("BufferStatePath")
        )


@dataclass
class BufferHistoryWrapper:
    """Buffer History"""

    @staticmethod
    def from_dict(obj: Any) -> BufferHistory:
        if obj.get("JsonBufferHistoryResult") is None:
            return None
        return BufferHistory.from_dict(obj.get("JsonBufferHistoryResult"))


@dataclass
class BufferHistoryDate:
    """Buffer History by Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[BufferHistory]:
        if obj.get("JsonBufferHistoryByDateResult") is None:
            return []
        return [BufferHistory.from_dict(y) for y in obj.get("JsonBufferHistoryByDateResult")]
