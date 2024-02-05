from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Spray baseclass
@dataclass
class Spray:
    ActionID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    LiquidAmount: int
    LiquidName: str
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    SprayActionDate: str
    SprayActionID: int
    SprayTime: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int
    TrayProfileID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Spray':
        return Spray(
            ActionID=obj.get("ActionID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            LiquidAmount=obj.get("LiquidAmount"),
            LiquidName=obj.get("LiquidName"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID"),
            SprayActionDate=obj.get("SprayActionDate"),
            SprayActionID=obj.get("SprayActionID"),
            SprayTime=obj.get("SprayTime"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayProfileID=obj.get("TrayProfileID")
        )

# Spray Action for Tray
@dataclass
class getSprayAction:
    Spray: Spray

    @staticmethod
    def from_dict(obj: Any) -> 'Spray':
        if obj.get("JsonSprayActionResult") is None:
            return None
        return [Spray.from_dict(y) for y in obj.get("JsonSprayActionResult")] 