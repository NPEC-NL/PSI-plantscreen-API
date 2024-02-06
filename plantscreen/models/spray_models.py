from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Spray:
    """Spray baseclass"""
    action_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    liquid_amount: int
    liquid_name: str
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int
    spray_action_date: str
    spray_action_id: int
    spray_time: int
    tray_area: str
    tray_barcode: str
    tray_id: int
    tray_profile_id: int

    @staticmethod
    def from_dict(obj: Any) -> Spray:
        return Spray(
            action_id=obj.get("ActionID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            liquid_amount=obj.get("LiquidAmount"),
            liquid_name=obj.get("LiquidName"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID"),
            spray_action_date=obj.get("SprayActionDate"),
            spray_action_id=obj.get("SprayActionID"),
            spray_time=obj.get("SprayTime"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_profile_id=obj.get("TrayProfileID")
        )


@dataclass
class SprayAction:
    """Spray Action for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Spray]:
        if obj.get("JsonSprayActionResult") is None:
            return []
        return [Spray.from_dict(y) for y in obj.get("JsonSprayActionResult")]
