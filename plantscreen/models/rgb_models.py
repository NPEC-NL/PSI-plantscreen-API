from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class RgbImage:
    """RgbImage baseclass"""
    action_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_date: str
    measure_height: float
    measure_id: int
    round_id: int
    tray_barcode: str
    tray_id: int
    tray_profile_id: int
    image_path: str

    @staticmethod
    def from_dict(obj: Any) -> RgbImage:
        return RgbImage(
            action_id=obj.get("ActionID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_date=obj.get("MeasureDate"),
            measure_height=obj.get("MeasureHeight"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_profile_id=obj.get("TrayProfileID"),
            image_path=obj.get("ImagePath")
        )


@dataclass
class RgbExtended:
    """RgbExtended baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> RgbExtended:
        return RgbExtended(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class RgbMask:
    """RgbMask baseclass"""
    device_id: int
    device_pid: str
    experiment_id: int
    mask_is_leaf: bool
    measure_angle: float
    measure_date: str
    measure_id: int
    plant_mask_path: str
    round_id: int
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> RgbMask:
        return RgbMask(
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            mask_is_leaf=obj.get("MaskIsLeaf"),
            measure_angle=obj.get("MeasureAngle"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            plant_mask_path=obj.get("PlantMaskPath"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class RgbGreen:
    """RgbGreen baseclass"""
    action_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_date: str
    measure_height: float
    measure_id: int
    round_id: int
    tray_barcode: str
    tray_id: int
    tray_profile_id: int
    greening_picture_path: str

    @staticmethod
    def from_dict(obj: Any) -> RgbGreen:
        return RgbGreen(
            action_id=obj.get("ActionID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_date=obj.get("MeasureDate"),
            measure_height=obj.get("MeasureHeight"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID"),
            tray_profile_id=obj.get("TrayProfileID"),
            greening_picture_path=obj.get("GreeningPicturePath")
        )


@dataclass
class RgbParam:
    """RgbParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> RgbParam:
        return RgbParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit")
        )


@dataclass
class RgbPlant:
    """RgbPlant baseclass"""
    analyse_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_id: int
    parameter_id: int
    parameter_name: str
    parameter_value: float
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int
    tray_area: str
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> RgbPlant:
        return RgbPlant(
            analyse_id=obj.get("AnalyseID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_value=obj.get("ParameterValue"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class RgbLeaf:
    """RgbLeaf baseclass"""
    analyse_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    leaf_index: int
    measure_angle: float
    measure_id: int
    parameter_id: int
    parameter_name: str
    parameter_value: float
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int
    tray_area: str
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> RgbLeaf:
        return RgbLeaf(
            analyse_id=obj.get("AnalyseID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            leaf_index=obj.get("LeafIndex"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_value=obj.get("ParameterValue"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class RgbImagingMeasure:
    """RGB image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> RgbImage:
        if obj.get("JsonRgbImagingByIDResult") is None:
            return None
        return RgbImage.from_dict(obj.get("JsonRgbImagingByIDResult"))


@dataclass
class RgbImaging:
    """RGB Imaging for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbImage]:
        if obj.get("JsonRgbImagingResult") is None:
            return []
        return [RgbImage.from_dict(y) for y in obj.get("JsonRgbImagingResult")]


class RgbImagingExtendedDataMeasure:
    """RGB Extended Data by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> RgbExtended:
        if obj.get("JsonRgbMeasureExtendedDataByIDResult") is None:
            return None
        return RgbExtended.from_dict(obj.get("JsonRgbMeasureExtendedDataByIDResult"))


class RgbImagingExtendedData:
    """RGB Extended Data for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> RgbExtended:
        if obj.get("JsonRgbMeasureExtendedDataResult") is None:
            return None
        return RgbExtended.from_dict(obj.get("JsonRgbMeasureExtendedDataResult"))


class RgbPlantMaskMeasure:
    """RGB Plant Mask by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> RgbMask:
        if obj.get("JsonRgbPlantMaskByMeasureIDResult") is None:
            return None
        return RgbMask.from_dict(obj.get("JsonRgbPlantMaskByMeasureIDResult"))


@dataclass
class RgbPlantMask:
    """RGB Plant Mask for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbMask]:
        if obj.get("JsonRgbPlantMaskResult") is None:
            return []
        return [RgbMask.from_dict(y) for y in obj.get("JsonRgbPlantMaskResult")]


class RgbGreeningMaskImageMeasure:
    """RGB Greening Mask Image by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> RgbGreen:
        if obj.get("JsonRgbGreeningMaskImageByMeasureIDResult") is None:
            return None
        return RgbGreen.from_dict(obj.get("JsonRgbGreeningMaskImageByMeasureIDResult"))


class RgbGreeningMaskImage:
    """RGB Greening Mask Image for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbGreen]:
        if obj.get("JsonRgbGreeningMaskImageResult") is None:
            return []
        return [RgbGreen.from_dict(y) for y in obj.get("JsonRgbGreeningMaskImageResult")]


class RgbParamWrapper:
    """RGB Parameter by ID"""

    @staticmethod
    def from_dict(obj: Any) -> RgbParam:
        if obj.get("JsonRgbParamResult") is None:
            return None
        return RgbParam.from_dict(obj.get("JsonRgbParamResult"))


class RgbParamUsedAnalyse:
    """RGB Used Parameters by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbParam]:
        if obj.get("JsonRgbUsedParamByAnalyseIDResult") is None:
            return []
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamByAnalyseIDResult")]


class RgbParamUsed:
    """RGB Used Parameters for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbParam]:
        if obj.get("JsonRgbcUsedParamsResult") is None:
            return []
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbcUsedParamsResult")]


class RgbParamColorUsedAnalyse:
    """RGB Used Color Parameters by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbParam]:
        if obj.get("JsonRgbUsedParamColorByAnalyseIDResult") is None:
            return []
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamColorByAnalyseIDResult")]


class RgbParamColorUsed:
    """RGB Used Color Parameters for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbParam]:
        if obj.get("JsonRgbUsedParamColorResult") is None:
            return []
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamColorResult")]


class RgbPlantParamAnalyse:
    """RGB Plant Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbPlant]:
        if obj.get("JsonRgbPlantParamByAnalyseIDResult") is None:
            return []
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamByAnalyseIDResult")]


class RgbPlantParam:
    """RGB Plant Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbPlant]:
        if obj.get("JsonRgbPlantParamResult") is None:
            return []
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamResult")]


class RgbPlantParamColorAnalyse:
    """RGB Color Plant Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbPlant]:
        if obj.get("JsonRgbPlantParamColorByAnalyseIDResult") is None:
            return []
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamColorByAnalyseIDResult")]


class RgbPlantParamColor:
    """RGB Color Plant Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbPlant]:
        if obj.get("JsonRgbPlantParamColorResult") is None:
            return []
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamColorResult")]


class RgbLeafParamAnalyse:
    """RGB Leaf Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbLeaf]:
        if obj.get("JsonRgbLeafParamByAnalyseIDResult") is None:
            return []
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamByAnalyseIDResult")]


class RgbLeafParam:
    """RGB Leaf Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbLeaf]:
        if obj.get("JsonRgbLeafParamResult") is None:
            return []
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamResult")]


class RgbLeafParamColorAnalyse:
    """RGB Color Leaf Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbLeaf]:
        if obj.get("JsonRgbLeafParamColorByAnalyseIDResult") is None:
            return []
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamColorByAnalyseIDResult")]


class RgbLeafParamColor:
    """RGB Color Leaf Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[RgbLeaf]:
        if obj.get("JsonRgbLeafParamColorResult") is None:
            return []
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamColorResult")]
