from dataclasses import dataclass
from typing import List
from typing import Any
import json


# Device baseclass
@dataclass
class Device:
    DeviceCaption: str
    DeviceConfig: str
    DeviceFamily: str
    DeviceID: int
    DeviceName: str
    DevicePID: str
    DeviceType: str
    DeviceValidityEnd: str
    DeviceValidityStart: str
    ProfileID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Device':
        return Device(
            DeviceCaption=obj.get("DeviceCaption"),
            DeviceConfig=obj.get("DeviceConfig"),
            DeviceFamily=obj.get("DeviceFamily"),
            DeviceID=obj.get("DeviceID"),
            DeviceName=obj.get("DeviceName"),
            DevicePID=obj.get("DevicePID"),
            DeviceType=obj.get("DeviceType"),
            DeviceValidityEnd=obj.get("DeviceValidityEnd"),
            DeviceValidityStart=obj.get("DeviceValidityStart"),
            ProfileID=obj.get("ProfileID")
        )
    
# Device by ID
@dataclass
class DeviceWrapper:
    Device: Device

    @staticmethod
    def from_dict(obj: Any) -> 'Device':
        if obj.get("JsonDeviceResult") is None:
            return None
        return Device.from_dict(obj.get("JsonDeviceResult"))

# List active devices
@dataclass
class DeviceActive:
    Device: Device

    @staticmethod
    def from_dict(obj: Any) -> 'Device':
        if obj.get("JsonDeviceActiveResult") is None:
            return []
        return [Device.from_dict(y) for y in obj.get("JsonDeviceActiveResult")]

# Device by profile ID
@dataclass
class DeviceProfile:
    Device: Device

    @staticmethod
    def from_dict(obj: Any) -> 'Device':
        if obj.get("JsonDeviceByProfileIDResult") is None:
            return []
        return [Device.from_dict(y) for y in obj.get("JsonDeviceByProfileIDResult")]
