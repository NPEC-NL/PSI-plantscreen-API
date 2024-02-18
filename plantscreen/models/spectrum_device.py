from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class SpectrumDeviceIDs:
    """"List experiments"""
    @staticmethod
    def from_dict(obj: Any) -> List[int]:
        """"Convert json to

        Return:
            List[int]"""
        _ids = [int(y.get("spectrum_device_id")) for y in obj.get("json_spectrum_device_id_result")]
        return _ids
