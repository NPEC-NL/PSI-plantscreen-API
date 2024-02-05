from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Plant baseclass
@dataclass
class Plant:
    PlantBarcode: str
    PlantID: int
    PlantInfo: str
    PlantName: str
    TrayArea: str

    @staticmethod
    def from_dict(obj: Any) -> 'Plant':
        return Plant(
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantInfo=obj.get("PlantInfo"),
            PlantName=obj.get("PlantName"),
            TrayArea=obj.get("TrayArea")
        )
    
# PlantHeight baseclass
@dataclass
class PlantHeight:
    ExperimentID: int
    HeightDate: str
    HeightValue: int
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int

    @staticmethod
    def from_dict(obj: Any) -> 'PlantHeight':
        return PlantHeight(
            ExperimentID=obj.get("ExperimentID"),
            HeightDate=obj.get("HeightDate"),
            HeightValue=obj.get("HeightValue"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID")
        )
    
# Leaf baseclass
@dataclass
class Leaf:
    LeafIndex: int
    PlantBarcode: str
    PlantID: int
    PlantName: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Leaf':
        return Leaf(
            LeafIndex=obj.get("LeafIndex"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            TrayID=obj.get("TrayID")
        )
    

# Device by ID
@dataclass
class PlantWrapper:
    Plant: Plant

    @staticmethod
    def from_dict(obj: Any) -> 'Plant':
        return [Plant.from_dict(y) for y in obj.get("JsonPlantResult")]    
    
# List plants by tray ID
@dataclass
class PlantTray:
    Plant: Plant

    @staticmethod
    def from_dict(obj: Any) -> 'Plant':
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayIDResult")]    

# List plants by trayID during period
@dataclass
class PlantTrayProfileTray:
    Plant: Plant

    @staticmethod
    def from_dict(obj: Any) -> 'Plant':
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayIDAndDatesResult")]    
    
# List plants by tray profile ID
@dataclass
class PlantTrayProfile:
    Plant: Plant

    @staticmethod
    def from_dict(obj: Any) -> 'Plant':
        return [Plant.from_dict(y) for y in obj.get("JsonPlantByTrayProfileIDResult")]    
        
# List plant height during round
@dataclass
class PlantHeightRound:
    PlantHeight: PlantHeight

    @staticmethod
    def from_dict(obj: Any) -> 'PlantHeight':
        return [PlantHeight.from_dict(y) for y in obj.get("JsonPlantHeightByRoundIDResult")]  
    
# List plant leaves by plant and tray ID
@dataclass
class PlantLeaf:
    Leaves: Leaf

    @staticmethod
    def from_dict(obj: Any) -> 'Leaf':
        return [Leaf.from_dict(y) for y in obj.get("JsonPlantLeavesByPlantAndTrayIDResult")]  




