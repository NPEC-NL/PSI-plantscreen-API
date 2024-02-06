from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Profile:
    """Profile baseclass"""
    profile_active: bool
    profile_id: int
    profile_info: str
    profile_name: str
    system_hw_config: str

    @staticmethod
    def from_dict(obj: Any) -> Profile:
        return Profile(
            profile_active=obj.get("ProfileActive"),
            profile_id=obj.get("ProfileID"),
            profile_info=obj.get("ProfileInfo"),
            profile_name=obj.get("ProfileName"),
            system_hw_config=obj.get("SystemHwConfig")
        )


@dataclass
class ProfileID:
    """List system profiles"""

    @staticmethod
    def from_dict(obj: Any) -> List[ProfileID]:
        if obj.get("JsonSystemProfileIDResult") is None:
            return []
        _ids = [int(y.get("ProfileID")) for y in obj.get("JsonSystemProfileIDResult")]
        return _ids


@dataclass
class ProfileWrapper:
    """System profile by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Profile:
        if obj.get("JsonSystemProfileResult") is None:
            return None
        return Profile.from_dict(obj.get("JsonSystemProfileResult"))


@dataclass
class ProfileActive:
    """List active system profiles"""

    @staticmethod
    def from_dict(obj: Any) -> Profile:
        if obj.get("JsonSystemProfileActiveResult") is None:
            return None
        return Profile.from_dict(obj.get("JsonSystemProfileActiveResult"))
