from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class DeviceID:
    """DeviceID baseclass"""
    spectrum_device_id: int

    @staticmethod
    def from_dict(obj: Any) -> DeviceID:
        return DeviceID(
            spectrum_device_id=obj.get("SpectrumDeviceID")
        )


@dataclass
class SpectrumDevice:
    """SpectrumDevice baseclass"""
    spectrum_device_id: int
    spectrum_device_serial: str
    spectrum_device_wavelengths_json: str

    @staticmethod
    def from_dict(obj: Any) -> SpectrumDevice:
        return SpectrumDevice(
            spectrum_device_id=obj.get("SpectrumDeviceID"),
            spectrum_device_serial=obj.get("SpectrumDeviceSerial"),
            spectrum_device_wavelengths_json=obj.get("SpectrumDeviceWavelengthsJSON")
        )


@dataclass
class SpectrumValues:
    """SpectrumValues baseclass"""
    spectrum_device_id: int
    spectrum_path: str
    spectrum_record_date: str

    @staticmethod
    def from_dict(obj: Any) -> SpectrumValues:
        return SpectrumValues(
            spectrum_device_id=obj.get("SpectrumDeviceID"),
            spectrum_path=obj.get("SpectrumPath"),
            spectrum_record_date=obj.get("SpectrumRecordDate")
        )


@dataclass
class SpectrumDeviceID:
    """Spectrum Device IDs"""

    @staticmethod
    def from_dict(obj: Any) -> List[DeviceID]:
        if obj.get("JsonSpectrumDeviceIDResult") is None:
            return []
        return [DeviceID.from_dict(y) for y in obj.get("JsonSpectrumDeviceIDResult")]


@dataclass
class SpectrumDeviceWrapper:
    """Spectrum Device by ID"""

    @staticmethod
    def from_dict(obj: Any) -> SpectrumDevice:
        if obj.get("JsonSpectrumDeviceResult") is None:
            return None
        return SpectrumDevice.from_dict(obj.get("JsonSpectrumDeviceResult"))


@dataclass
class SpectrumValuesDateDevice:
    """Spectrum Values"""

    @staticmethod
    def from_dict(obj: Any) -> List[SpectrumValues]:
        if obj.get("JsonSpectrumValuesResult") is None:
            return []
        return [SpectrumValues.from_dict(y) for y in obj.get("JsonSpectrumValuesResult")]
