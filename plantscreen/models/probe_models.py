from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Probe:
    """Probe baseclass"""
    probe_family: str
    probe_id: int
    probe_name: str
    probe_placement: str
    probe_unit: str
    probe_variable: str

    @staticmethod
    def from_dict(obj: Any) -> Probe:
        return Probe(
            probe_family=obj.get("ProbeFamily"),
            probe_id=obj.get("ProbeID"),
            probe_name=obj.get("ProbeName"),
            probe_placement=obj.get("ProbePlacement"),
            probe_unit=obj.get("ProbeUnit"),
            probe_variable=obj.get("ProbeVariable")
        )


@dataclass
class ProbeValue:
    """ProbeValue baseclass"""
    probe_id: int
    probe_name: str
    probe_unit: str
    probe_value: float
    record_date: int

    @staticmethod
    def from_dict(obj: Any) -> ProbeValue:
        return ProbeValue(
            probe_id=obj.get("ProbeID"),
            probe_name=obj.get("ProbeName"),
            probe_unit=obj.get("ProbeUnit"),
            probe_value=obj.get("ProbeValue"),
            record_date=obj.get("RecordDate")
        )


@dataclass
class ProbeWrapper:
    """List of environment sensors (all used probes)"""

    @staticmethod
    def from_dict(obj: Any) -> List[Probe]:
        if obj.get("JsonProbeResult") is None:
            return []
        return [Probe.from_dict(y) for y in obj.get("JsonProbeResult")]


@dataclass
class ProbeValuesDate:
    """List probevalues in period"""

    @staticmethod
    def from_dict(obj: Any) -> List[ProbeValue]:
        if obj.get("JsonProbeValueByDateResult") is None:
            return []
        return [ProbeValue.from_dict(y) for y in obj.get("JsonProbeValueByDateResult")]


@dataclass
class ProbeValueDateProbe:
    """Environment Probe Value by ID and Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[ProbeValue]:
        if obj.get("JsonProbeValueByIDAndDateResult") is None:
            return []
        return [ProbeValue.from_dict(y) for y in obj.get("JsonProbeValueByIDAndDateResult")]
