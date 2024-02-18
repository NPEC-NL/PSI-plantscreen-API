from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class ProfileIDs:
    """"List experiments"""
    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        """"Convert json to

        Return:
            List[int]"""
        _ids = [int(y.get("profile_id")) for y in obj.get("json_system_profile_id_result")]
        return _ids
