from dataclasses import dataclass
from typing import List
from typing import Any
import json


# Tray baseclass
@dataclass
class Tray:
    TrayBarcode: str
    TrayID: int
    TrayInfo: str
    TrayStatus: str
    TrayStatusChanged: str
    TrayTypeID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Tray':
        return Tray(
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayInfo=obj.get("TrayInfo"),
            TrayStatus=obj.get("TrayStatus"),
            TrayStatusChanged=obj.get("TrayStatusChanged"),
            TrayTypeID=obj.get("TrayTypeID")

        )
    
# TrayInfo baseclass
@dataclass
class TrayInfo:
    TypeID: int
    TypeInfo: str
    TypeMaskBottom: str
    TypeMaskSide: str
    TypeMaskTop: str
    TypeMaskUnderSide: str
    TypeName: str
    TypeSizeX: int
    TypeSizeY: int
    TypeSizeZ: int

    @staticmethod
    def from_dict(obj: Any) -> 'TrayInfo':
        return TrayInfo(
            TypeID=obj.get("TypeID"),
            TypeInfo=obj.get("TypeInfo"),
            TypeMaskBottom=obj.get("TypeMaskBottom"),
            TypeMaskSide=obj.get("TypeMaskSide"),
            TypeMaskTop=obj.get("TypeMaskTop"),   
            TypeMaskUnderSide=obj.get("TypeMaskUnderSide"),   
            TypeName=obj.get("TypeName"),
            TypeSizeX=obj.get("TypeSizeX"),
            TypeSizeY=obj.get("TypeSizeY"),
            TypeSizeZ=obj.get("TypeSizeZ")
        )

# TrayProfile baseclass
@dataclass
class TrayProfile:
    ProfileDateStart: str
    ProfileDateStop: str
    ProfileID: int
    ProfileName: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'TrayProfile':
        if obj is None:
            return None
        return TrayProfile(
            ProfileDateStart=obj.get("ProfileDateStart"),
            ProfileDateStop=obj.get("ProfileDateStop"),
            ProfileID=obj.get("ProfileID"),
            ProfileName=obj.get("ProfileName"),
            TrayID=obj.get("TrayID")
        )

# ScalesMapping baseclass
@dataclass
class ScalesMapping:
    MapArea: str
    MapColumn: int
    MapRow: int
    TrayTypeID: int

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMapping':
        return ScalesMapping(
            MapArea=obj.get("MapArea"),
            MapColumn=obj.get("MapColumn"),
            MapRow=obj.get("MapRow"),
            TrayTypeID=obj.get("TrayTypeID")
        )



# Tray by ID
@dataclass
class TrayWrapper:
    Tray: Tray

    @staticmethod
    def from_dict(obj: Any) -> 'Tray':
        return Tray.from_dict(obj.get("JsonTrayResult"))
    
# List trays in round ID
@dataclass
class TrayRound:
    Tray: Tray

    @staticmethod
    def from_dict(obj: Any) -> 'Tray':
        return [Tray.from_dict(y) for y in obj.get("JsonTrayByRoundIDResult")]

# Tray type by tray type ID
@dataclass
class TrayType:
    TrayInfo: TrayInfo

    @staticmethod
    def from_dict(obj: Any) -> 'TrayInfo':
        return TrayInfo.from_dict(obj.get("JsonTrayTypeResult"))
    
# Tray type by tray ID
@dataclass
class TrayTypeTray:
    TrayInfo: TrayInfo

    @staticmethod
    def from_dict(obj: Any) -> 'TrayInfo':
        return TrayInfo.from_dict(obj.get("JsonTrayTypeByTrayIDResult"))

# Tray type by profile ID
@dataclass
class TrayTypeTrayProfile:
    TrayInfo: TrayInfo

    @staticmethod
    def from_dict(obj: Any) -> 'TrayInfo':
        return TrayInfo.from_dict(obj.get("JsonTrayTypeByTrayProfileIDResult"))  

# Trayprofile by profile ID
@dataclass
class TrayProfileWrapper:
    TrayProfile: TrayProfile

    @staticmethod
    def from_dict(obj: Any) -> 'TrayProfile':
        return TrayProfile.from_dict(obj.get("JsonTrayProfileResult"))  

# List trays by trayprofile
@dataclass
class TrayProfileTray:
    TrayProfile: TrayProfile

    @staticmethod
    def from_dict(obj: Any) -> 'TrayProfile':
        return [TrayProfile.from_dict(y) for y in obj.get("JsonTrayProfileByTrayIDResult")]
    
# Trayprofile of tray during period
@dataclass
class TrayProfileUsedTray:
    TrayProfile: TrayProfile

    @staticmethod
    def from_dict(obj: Any) -> 'TrayProfile':
        return [TrayProfile.from_dict(y) for y in obj.get("JsonUsedTrayProfileByTrayIDResult")]
    

# Trayprofile of tray on date
@dataclass
class TrayProfileToDateTray:
    TrayProfile: TrayProfile
    
    @staticmethod
    def from_dict(obj: Any) -> 'TrayProfile':
        if obj.get("JsonTrayProfileByTrayIDToDateResult") is None:
            return None

        return  TrayProfile.from_dict(obj.get("JsonTrayProfileByTrayIDToDateResult"))  
    
# Scalesmap by tray ID
@dataclass
class ScalesMappingTray:
    ScalesMapping: ScalesMapping

    @staticmethod
    def from_dict(obj: Any) -> 'ScalesMapping':
        return  [ScalesMapping.from_dict(y) for y in obj.get("JsonScalesMappingByTrayIDResult")]
    