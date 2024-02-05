from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Version baseclass
@dataclass
class Version:
    ApiVersion: str
    DatabaseVersion: int

    @staticmethod
    def from_dict(obj: Any) -> 'Version':
        return Version(
            ApiVersion=obj.get("ApiVersion"),
            DatabaseVersion=obj.get("DatabaseVersion")
        )
    

# Version Info
@dataclass
class VersionInfo:
    Version: Version

    @staticmethod
    def from_dict(obj: Any) -> 'Version':
        if obj.get("JsonVersionInfoResult") is None:
            return None
        return Version.from_dict(obj.get("JsonVersionInfoResult"))
