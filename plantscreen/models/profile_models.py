from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Profile baseclass
@dataclass
class Profile:
    ProfileActive: bool
    ProfileID: int
    ProfileInfo: str
    ProfileName: str
    SystemHwConfig: str


    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        return Profile(
            ProfileActive=obj.get("ProfileActive"),
            ProfileID=obj.get("ProfileID"),
            ProfileInfo=obj.get("ProfileInfo"),
            ProfileName=obj.get("ProfileName"),
            SystemHwConfig=obj.get("SystemHwConfig")
        )

# List system profiles
@dataclass
class ProfileID:
    IDs: int

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileID':
        if obj.get("JsonSystemProfileIDResult") is None:
            return []
        _IDs = [int(y.get("ProfileID")) for y in obj.get("JsonSystemProfileIDResult")]
        return ProfileID(_IDs)

# system profile by ID
@dataclass
class ProfileWrapper:
    Profile: Profile

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        if obj.get("JsonSystemProfileResult") is None:
            return []
        return Profile.from_dict(obj.get("JsonSystemProfileResult"))
    
# List active system profiles
@dataclass
class ProfileActive:
    Profile: Profile

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        if obj.get("JsonSystemProfileActiveResult") is None:
            return None
        return Profile.from_dict(obj.get("JsonSystemProfileActiveResult"))