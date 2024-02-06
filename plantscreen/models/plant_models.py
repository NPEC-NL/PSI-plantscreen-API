from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Plant:
    """Plant baseclass"""
    plant_barcode: str
    plant_id: int
    plant_info: str
    plant_name: str
    tray_area: str

    @staticmethod
    def from_dict(obj: Any) -> Plant:
        return Plant(
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_info=obj.get("PlantInfo"),
            plant_name=obj.get("PlantName"),
            tray_area=obj.get("TrayArea")
        )


@dataclass
class PlantHeight:
    """PlantHeight baseclass"""
    experiment_id: int
    height_date: str
    height_value: str
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int

    @staticmethod
    def from_dict(obj: Any) -> PlantHeight:
        return PlantHeight(
            experiment_id=obj.get("ExperimentID"),
            height_date=obj.get("HeightDate"),
            height_value=obj.get("HeightValue"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID")
        )


@dataclass
class Leaf:
    """Leaf baseclass"""
    leaf_index: int
    plant_barcode: str
    plant_id: int
    plant_name: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> Leaf:
        return Leaf(
            leaf_index=obj.get("LeafIndex"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class PlantWrapper:
    """List plants by plant ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Plant]:
        if obj.get("JsonPlantResult") is None:
            return []
        return [Plant.from_dict(y) for y in obj.get("JsonPlantResult")]


@dataclass
class PlantTray:
    """List plants by tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Plant]:
        if obj.get("JsonPlantByTrayIDResult") is None:
            return []
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayIDResult")]


@dataclass
class PlantTrayProfileTray:
    """List plants by trayID during period"""

    @staticmethod
    def from_dict(obj: Any) -> List[Plant]:
        if obj.get("JsonPlantByTrayIDAndDatesResult") is None:
            return []
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayIDAndDatesResult")]


@dataclass
class PlantTrayProfile:
    """List plants by tray profile ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Plant]:
        if obj.get("JsonPlantByTrayProfileIDResult") is None:
            return []
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayProfileIDResult")]


@dataclass
class PlantHeightRound:
    """List plant height during round"""

    @staticmethod
    def from_dict(obj: Any) -> List[PlantHeight]:
        if obj.get("JsonPlantHeightByRoundIDResult") is None:
            return []
        return [PlantHeight.from_dict(y) for y in obj.get("JsonPlantHeightByRoundIDResult")]


@dataclass
class PlantLeaf:
    """List plant leaves by plant and tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Leaf]:
        if obj.get("JsonPlantLeavesByPlantAndTrayIDResult") is None:
            return []
        return [Leaf.from_dict(y) for y in obj.get("JsonPlantLeavesByPlantAndTrayIDResult")]
