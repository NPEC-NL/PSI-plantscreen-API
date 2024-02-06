from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Tray:
    """Tray baseclass"""
    tray_barcode: str
    tray_id: int
    tray_info: str
    tray_status: str
    tray_status_changed: str
    tray_type_id: int

    @staticmethod
    def from_dict(obj: Any) -> Tray:
        return Tray(
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_info=obj.get("TrayInfo"),
            tray_status=obj.get("TrayStatus"),
            tray_status_changed=obj.get("TrayStatusChanged"),
            tray_type_id=obj.get("TrayTypeID")
        )


@dataclass
class TrayInfo:
    """TrayInfo baseclass"""
    type_id: int
    type_info: str
    type_mask_bottom: str
    type_mask_side: str
    type_mask_top: str
    type_mask_under_side: str
    type_name: str
    type_size_x: int
    type_size_y: int
    type_size_z: int

    @staticmethod
    def from_dict(obj: Any) -> TrayInfo:
        return TrayInfo(
            type_id=obj.get("TypeID"),
            type_info=obj.get("TypeInfo"),
            type_mask_bottom=obj.get("TypeMaskBottom"),
            type_mask_side=obj.get("TypeMaskSide"),
            type_mask_top=obj.get("TypeMaskTop"),
            type_mask_under_side=obj.get("TypeMaskUnderSide"),
            type_name=obj.get("TypeName"),
            type_size_x=obj.get("TypeSizeX"),
            type_size_y=obj.get("TypeSizeY"),
            type_size_z=obj.get("TypeSizeZ")
        )


@dataclass
class TrayProfile:
    """TrayProfile baseclass"""
    profile_date_start: str
    profile_date_stop: str
    profile_id: int
    profile_name: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> TrayProfile:
        return TrayProfile(
            profile_date_start=obj.get("ProfileDateStart"),
            profile_date_stop=obj.get("ProfileDateStop"),
            profile_id=obj.get("ProfileID"),
            profile_name=obj.get("ProfileName"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class ScalesMapping:
    """ScalesMapping baseclass"""
    map_area: str
    map_column: int
    map_row: int
    tray_type_id: int

    @staticmethod
    def from_dict(obj: Any) -> ScalesMapping:
        return ScalesMapping(
            map_area=obj.get("MapArea"),
            map_column=obj.get("MapColumn"),
            map_row=obj.get("MapRow"),
            tray_type_id=obj.get("TrayTypeID")
        )


@dataclass
class TrayWrapper:
    """Tray by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Tray:
        if obj.get("JsonTrayResult") is None:
            return None
        return Tray.from_dict(obj.get("JsonTrayResult"))


@dataclass
class TrayRound:
    """List trays in round ID"""

    @staticmethod
    def from_dict(obj: Any) -> List(Tray):
        if obj.get("JsonTrayByRoundIDResult") is None:
            return []
        return [Tray.from_dict(y) for y in obj.get("JsonTrayByRoundIDResult")]


@dataclass
class TrayType:
    """Tray type by tray type ID"""

    @staticmethod
    def from_dict(obj: Any) -> TrayInfo:
        if obj.get("JsonTrayTypeResult") is None:
            return None
        return TrayInfo.from_dict(obj.get("JsonTrayTypeResult"))


@dataclass
class TrayTypeTray:
    """Tray type by tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> TrayInfo:
        if obj.get("JsonTrayTypeByTrayIDResult") is None:
            return None
        return TrayInfo.from_dict(obj.get("JsonTrayTypeByTrayIDResult"))


@dataclass
class TrayTypeTrayProfile:
    """Tray type by profile ID"""

    @staticmethod
    def from_dict(obj: Any) -> TrayInfo:
        if obj.get("JsonTrayTypeByTrayProfileIDResult") is None:
            return None
        return TrayInfo.from_dict(obj.get("JsonTrayTypeByTrayProfileIDResult"))


@dataclass
class TrayProfileWrapper:
    """Trayprofile by profile ID"""

    @staticmethod
    def from_dict(obj: Any) -> TrayProfile:
        if obj.get("JsonTrayProfileResult") is None:
            return None
        return TrayProfile.from_dict(obj.get("JsonTrayProfileResult"))


@dataclass
class TrayProfileTray:
    """List trays by trayprofile"""

    @staticmethod
    def from_dict(obj: Any) -> List[TrayProfile]:
        if obj.get("JsonTrayProfileByTrayIDResult") is None:
            return []
        return [TrayProfile.from_dict(y) for y in obj.get("JsonTrayProfileByTrayIDResult")]


@dataclass
class TrayProfileUsedTray:
    """Trayprofile of tray during period"""

    @staticmethod
    def from_dict(obj: Any) -> List[TrayProfile]:
        if obj.get("JsonUsedTrayProfileByTrayIDResult") is None:
            return []
        return [TrayProfile.from_dict(y) for y in obj.get("JsonUsedTrayProfileByTrayIDResult")]


@dataclass
class TrayProfileToDateTray:
    """Trayprofile of tray on date"""

    @staticmethod
    def from_dict(obj: Any) -> TrayProfile:
        if obj.get("JsonTrayProfileByTrayIDToDateResult") is None:
            return None
        return TrayProfile.from_dict(obj.get("JsonTrayProfileByTrayIDToDateResult"))


@dataclass
class ScalesMappingTray:
    """Scalesmap by tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[ScalesMapping]:
        if obj.get("JsonScalesMappingByTrayIDResult") is None:
            return []
        return [ScalesMapping.from_dict(y) for y in obj.get("JsonScalesMappingByTrayIDResult")]
