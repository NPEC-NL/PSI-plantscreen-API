from dataclasses import dataclass
from typing import List
from typing import Any
import json

# DeviceID baseclass
@dataclass
class DeviceID:
    SpectrumDeviceID: int

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceID':
        return DeviceID(
            SpectrumDeviceID=obj.get("SpectrumDeviceID")
        )

# SpectrumDevice baseclass
@dataclass
class SpectrumDevice:
    SpectrumDeviceID: int
    SpectrumDeviceSerial: str
    SpectrumDeviceWavelengthsJSON: str

    @staticmethod
    def from_dict(obj: Any) -> 'SpectrumDevice':
        return SpectrumDevice(
            SpectrumDeviceID=obj.get("SpectrumDeviceID"),
            SpectrumDeviceSerial=obj.get("SpectrumDeviceSerial"),
            SpectrumDeviceWavelengthsJSON=obj.get("SpectrumDeviceWavelengthsJSON")
        )

# SpectrumValues baseclass
@dataclass
class SpectrumValues:
    SpectrumDeviceID: int
    SpectrumPath: str
    SpectrumRecordDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'SpectrumValues':
        return SpectrumValues(
            SpectrumDeviceID=obj.get("SpectrumDeviceID"),
            SpectrumPath=obj.get("SpectrumPath"),
            SpectrumRecordDate=obj.get("SpectrumRecordDate")
        )

# Spectrum Device IDs
@dataclass
class getSpectrumDeviceID:
    DeviceID: DeviceID

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceID':
        if obj.get("JsonSpectrumDeviceIDResult") is None:
            return None
        return [DeviceID.from_dict(y) for y in obj.get("JsonSpectrumDeviceIDResult")] 

# Spectrum Device by ID
@dataclass
class getSpectrumDevice:
    SpectrumDevice: SpectrumDevice

    @staticmethod
    def from_dict(obj: Any) -> 'SpectrumDevice':
        if obj.get("JsonSpectrumDeviceResult") is None:
            return None
        return SpectrumDevice.from_dict(obj.get("JsonSpectrumDeviceResult"))

# Spectrum Values
@dataclass
class getSpectrumValuesDateDevice:
    SpectrumValues: SpectrumValues

    @staticmethod
    def from_dict(obj: Any) -> 'SpectrumValues':
        if obj.get("JsonSpectrumValuesResult") is None:
            return None
        return [SpectrumValues.from_dict(y) for y in obj.get("JsonSpectrumValuesResult")] 


