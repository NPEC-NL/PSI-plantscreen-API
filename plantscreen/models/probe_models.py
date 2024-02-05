from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Probe baseclass
@dataclass
class Probe:
    ProbeFamily: str
    ProbeID: int
    ProbeName: str
    ProbePlacement: str
    ProbeUnit: str
    ProbeVariable: str

    @staticmethod
    def from_dict(obj: Any) -> 'Probe':
        return Probe(
            ProbeFamily=obj.get("ProbeFamily"),
            ProbeID=obj.get("ProbeID"),
            ProbeName=obj.get("ProbeName"),
            ProbePlacement=obj.get("ProbePlacement"),
            ProbeUnit=obj.get("ProbeUnit"),
            ProbeVariable=obj.get("ProbeVariable")
        )

# ProbeValue baseclass
@dataclass
class ProbeValue:
    ProbeID: int
    ProbeName: str
    ProbeUnit: str
    ProbeValue: float
    RecordDate: int

    @staticmethod
    def from_dict(obj: Any) -> 'ProbeValue':
        return ProbeValue(
            ProbeID=obj.get("ProbeID"),
            ProbeName=obj.get("ProbeName"),
            ProbeUnit=obj.get("ProbeUnit"),
            ProbeValue=obj.get("ProbeValue"),
            RecordDate=obj.get("RecordDate")
        )
    
# List of environment sensors (all used probes)
@dataclass
class ProbeWrapper:
    Probe: List[Probe]

    @staticmethod
    def from_dict(obj: Any) -> 'Probe':
        return [Probe.from_dict(y) for y in obj.get("JsonProbeResult")]

# List probevalues in period
@dataclass
class ProbeValuesDate:
    ProbeValues: List[ProbeValue]

    @staticmethod
    def from_dict(obj: Any) -> 'ProbeValuesDate':
        return [ProbeValue.from_dict(y) for y in obj.get("JsonProbeValueByDateResult")]
    
# Environment Probe Value by ID and Date
@dataclass
class ProbeValueDateProbe:
    ProbeValue: ProbeValue

    @staticmethod
    def from_dict(obj: Any) -> 'ProbeValueDateProbe':
        return [ProbeValue.from_dict(y) for y in obj.get("JsonProbeValueByIDAndDateResult")] 