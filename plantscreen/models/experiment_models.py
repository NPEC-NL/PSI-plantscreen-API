from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class ExperimentIDs:
    """"List experiments"""
    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        """"Convert json to

        Return
            List[int]"""
        if obj.get("json_experiment_id_result") is None:
            return []
        _ids = [int(y.get("experiment_id")) for y in obj.get("json_experiment_id_result")]
        return _ids


@dataclass
class OwnerID:
    """List experiment owner ids"""
    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        """"Convert json to

        Return
            List[int]"""
        if obj.get("json_owner_id_result") is None:
            return []
        return [y.get('owner_id') for y in obj.get("json_owner_id_result")]
