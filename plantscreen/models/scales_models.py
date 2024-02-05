from dataclasses import dataclass
from typing import List
from typing import Any
import json

# ScalesMeasure baseclass
@dataclass
class ScalesMeasure:
    ActionID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureDate: str
    MeasureID: int
    PlantBarcode: str
    PlantID: int
    PlantName: str
    PlantWeight: float
    RoundID: int
    TrayBarcode: str
    TrayID: int
    TrayArea: str
    TrayProfileID: int
    Watered: bool

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMeasure':
        return ScalesMeasure(
            ActionID=obj.get("ActionID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            PlantWeight=obj.get("PlantWeight"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayArea=obj.get("TrayArea"),
            TrayProfileID=obj.get("TrayProfileID"),
            Watered=obj.get("Watered")
        )
    
# ScalesMeasure2 baseclass
@dataclass
class ScalesMeasure2:
    ActionID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureDate: str
    MeasureID: int
    PlantBarcode: str
    PlantID: int
    PlantName: str
    PlantWeight: float
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int
    TrayProfileID: int
    Watered: bool

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMeasure2':
        return ScalesMeasure2(
            ActionID=obj.get("ActionID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            PlantWeight=obj.get("PlantWeight"),
            RoundID=obj.get("RoundID"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayProfileID=obj.get("TrayProfileID"),
            Watered=obj.get("Watered")
        )

# ScalesPlant baseclass
@dataclass
class ScalesPlant:
    PlantBarcode: str
    PlantID: int
    PlantName: str
    ReferenceWeightDate: str
    ReferenceWeightValue: float

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesPlant':
        return ScalesPlant(
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            ReferenceWeightDate=obj.get("ReferenceWeightDate"),
            ReferenceWeightValue=obj.get("ReferenceWeightValue")
        )

# Scales Data by Measure ID
@dataclass
class ScalesPlantWeightMeasure:
    ScalesMeasure: ScalesMeasure

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMeasure':
        if obj.get("JsonScalesMeasureByIDResult") is None:
            return None
        return ScalesMeasure.from_dict(obj.get("JsonScalesMeasureByIDResult"))

# Scales Measure for Tray
@dataclass
class ScalesPlantWeight:
    ScalesMeasure2: ScalesMeasure2

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMeasure2':
        if obj.get("JsonScalesMeasureResult") is None:
            return []
        return [ScalesMeasure2.from_dict(y) for y in obj.get("JsonScalesMeasureResult")] 
    
# Plant Weight Reference by Plant ID
@dataclass
class ScalesWeightReferencePlant:
    ScalesPlant: ScalesPlant

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesPlant':
        if obj.get("JsonPlantWeightReferenceByPlantIDResult") is None:
            return None
        return ScalesPlant.from_dict(obj.get("JsonPlantWeightReferenceByPlantIDResult"))

# Plant Weight Reference by Tray ID
@dataclass
class ScalesWeightReferenceTray:
    ScalesPlant: ScalesPlant

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesPlant':
        if obj.get("JsonPlantWeightReferenceByTrayIDResult") is None:
            return []
        return [ScalesPlant.from_dict(y) for y in obj.get("JsonPlantWeightReferenceByTrayIDResult")] 

# Plant Weight Reference by Tray ID to Date
@dataclass
class ScalesWeightReferenceToDateTray:
    ScalesPlant: ScalesPlant

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesPlant':
        if obj.get("JsonPlantWeightReferenceByTrayIDToDateResult") is None:
            return []
        return [ScalesPlant.from_dict(y) for y in obj.get("JsonPlantWeightReferenceByTrayIDToDateResult")] 