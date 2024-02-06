from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class ScalesMeasure:
    """ScalesMeasure baseclass"""
    action_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_date: str
    measure_id: int
    plant_barcode: str
    plant_id: int
    plant_name: str
    plant_weight: float
    round_id: int
    tray_barcode: str
    tray_id: int
    tray_area: str
    tray_profile_id: int
    watered: bool

    @staticmethod
    def from_dict(obj: Any) -> ScalesMeasure:
        return ScalesMeasure(
            action_id=obj.get("ActionID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            plant_weight=obj.get("PlantWeight"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_area=obj.get("TrayArea"),
            tray_profile_id=obj.get("TrayProfileID"),
            watered=obj.get("Watered")
        )


@dataclass
class ScalesMeasure2:
    """ScalesMeasure2 baseclass"""
    action_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_date: str
    measure_id: int
    plant_barcode: str
    plant_id: int
    plant_name: str
    plant_weight: float
    round_id: int
    tray_area: str
    tray_barcode: str
    tray_id: int
    tray_profile_id: int
    watered: bool

    @staticmethod
    def from_dict(obj: Any) -> ScalesMeasure2:
        return ScalesMeasure2(
            action_id=obj.get("ActionID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            plant_weight=obj.get("PlantWeight"),
            round_id=obj.get("RoundID"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_profile_id=obj.get("TrayProfileID"),
            watered=obj.get("Watered")
        )


@dataclass
class ScalesPlant:
    """ScalesPlant baseclass"""
    plant_barcode: str
    plant_id: int
    plant_name: str
    reference_weight_date: str
    reference_weight_value: float

    @staticmethod
    def from_dict(obj: Any) -> ScalesPlant:
        return ScalesPlant(
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            reference_weight_date=obj.get("ReferenceWeightDate"),
            reference_weight_value=obj.get("ReferenceWeightValue")
        )


@dataclass
class ScalesPlantWeightMeasure:
    """Scales Data by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> ScalesMeasure:
        if obj.get("JsonScalesMeasureByIDResult") is None:
            return None
        return ScalesMeasure.from_dict(obj.get("JsonScalesMeasureByIDResult"))


@dataclass
class ScalesPlantWeight:
    """Scales Measure for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[ScalesMeasure2]:
        if obj.get("JsonScalesMeasureResult") is None:
            return []
        return [ScalesMeasure2.from_dict(y) for y in obj.get("JsonScalesMeasureResult")]


@dataclass
class ScalesWeightReferencePlant:
    """Plant Weight Reference by Plant ID"""

    @staticmethod
    def from_dict(obj: Any) -> ScalesPlant:
        if obj.get("JsonPlantWeightReferenceByPlantIDResult") is None:
            return None
        return ScalesPlant.from_dict(obj.get("JsonPlantWeightReferenceByPlantIDResult"))


@dataclass
class ScalesWeightReferenceTray:
    """Plant Weight Reference by Tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[ScalesPlant]:
        if obj.get("JsonPlantWeightReferenceByTrayIDResult") is None:
            return []
        return [ScalesPlant.from_dict(y) for y in obj.get("JsonPlantWeightReferenceByTrayIDResult")]


@dataclass
class ScalesWeightReferenceToDateTray:
    """Plant Weight Reference by Tray ID to Date"""

    @staticmethod
    def from_dict(obj: Any) -> List[ScalesPlant]:
        if obj.get("JsonPlantWeightReferenceByTrayIDToDateResult") is None:
            return []
        return [ScalesPlant.from_dict(y) for y in obj.get("JsonPlantWeightReferenceByTrayIDToDateResult")]
