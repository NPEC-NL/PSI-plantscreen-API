from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Version:
    """Version baseclass"""
    api_version: str
    database_version: int

    @staticmethod
    def from_dict(obj: Any) -> Version:
        return Version(
            api_version=obj.get("ApiVersion"),
            database_version=obj.get("DatabaseVersion")
        )


@dataclass
class VersionInfo:
    """Version Info"""

    @staticmethod
    def from_dict(obj: Any) -> Version:
        if obj.get("JsonVersionInfoResult") is None:
            return None
        return Version.from_dict(obj.get("JsonVersionInfoResult"))
