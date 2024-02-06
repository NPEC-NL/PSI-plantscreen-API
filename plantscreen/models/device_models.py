from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Device:
    """Device baseclass"""
    device_caption: str
    device_config: str
    device_family: str
    device_id: int
    device_name: str
    devicep_id: str
    device_type: str
    device_validity_end: str
    device_validity_start: str
    profile_id: int

    @staticmethod
    def from_dict(obj: Any) -> Device:
        return Device(
            device_caption=obj.get("DeviceCaption"),
            device_config=obj.get("DeviceConfig"),
            device_family=obj.get("DeviceFamily"),
            device_id=obj.get("DeviceID"),
            device_name=obj.get("DeviceName"),
            devicep_id=obj.get("DevicePID"),
            device_type=obj.get("DeviceType"),
            device_validity_end=obj.get("DeviceValidityEnd"),
            device_validity_start=obj.get("DeviceValidityStart"),
            profile_id=obj.get("ProfileID")
        )


@dataclass
class DeviceWrapper:
    """Device by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Device:
        if obj.get("JsonDeviceResult") is None:
            return None
        return Device.from_dict(obj.get("JsonDeviceResult"))


@dataclass
class DeviceActive:
    """List active devices"""

    @staticmethod
    def from_dict(obj: Any) -> List[Device]:
        if obj.get("JsonDeviceActiveResult") is None:
            return []
        return [Device.from_dict(y) for y in obj.get("JsonDeviceActiveResult")]


@dataclass
class DeviceProfile:
    """Device by profile ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Device]:
        if obj.get("JsonDeviceByProfileIDResult") is None:
            return []
        return [Device.from_dict(y) for y in obj.get("JsonDeviceByProfileIDResult")]
