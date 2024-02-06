from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class HcImaging:
    """HcImaging baseclass"""
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
    calibration_dark_content_path: str
    calibration_dark_header_path: str
    calibration_white_content_path: str
    calibration_white_header_path: str
    data_content_path: str
    data_header_path: str

    @staticmethod
    def from_dict(obj: Any) -> HcImaging:
        return HcImaging(
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
            calibration_dark_content_path=obj.get("CalibrationDarkContentPath"),
            calibration_dark_header_path=obj.get("CalibrationDarkHeaderPath"),
            calibration_white_content_path=obj.get("CalibrationWhiteContentPath"),
            calibration_white_header_path=obj.get("CalibrationWhiteHeaderPath"),
            data_content_path=obj.get("DataContentPath"),
            data_header_path=obj.get("DataHeaderPath")
        )


@dataclass
class HcMeasure:
    """HcMeasure baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> HcMeasure:
        return HcMeasure(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class HcRgb:
    """HcRgb baseclass"""
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_id: int
    rgb_image_path: str
    round_id: int
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> HcRgb:
        return HcRgb(
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            rgb_image_path=obj.get("RgbImagePath"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class HcMask:
    """HcMask baseclass"""
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
    def from_dict(obj: Any) -> HcMask:
        return HcMask(
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
class HcParam:
    """HcParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> HcParam:
        return HcParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit")
        )


@dataclass
class HcImage:
    """HcImage baseclass"""
    analyse_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_id: int
    parameter_id: int
    parameter_image_path: str
    parameter_name: str
    round_id: int
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> HcImage:
        return HcImage(
            analyse_id=obj.get("AnalyseID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            parameter_id=obj.get("ParameterID"),
            parameter_image_path=obj.get("ParameterImagePath"),
            parameter_name=obj.get("ParameterName"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class HcPlant:
    """HcPlant baseclass"""
    analyse_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    measure_angle: float
    measure_id: int
    parameter_avg: float
    parameter_id: int
    parameter_max: float
    parameter_median: float
    parameter_min: float
    parameter_name: str
    parameter_stddev: float
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int
    tray_area: str
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> HcPlant:
        return HcPlant(
            analyse_id=obj.get("AnalyseID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            parameter_avg=obj.get("ParameterAvg"),
            parameter_id=obj.get("ParameterID"),
            parameter_max=obj.get("ParameterMax"),
            parameter_median=obj.get("ParameterMedian"),
            parameter_min=obj.get("ParameterMin"),
            parameter_name=obj.get("ParameterName"),
            parameter_stddev=obj.get("ParameterStddev"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class HcLeaf:
    """HcLeaf baseclass"""
    analyse_id: int
    device_id: int
    device_pid: str
    experiment_id: int
    leaf_index: int
    measure_angle: float
    measure_id: int
    parameter_avg: float
    parameter_id: int
    parameter_max: float
    parameter_median: float
    parameter_min: float
    parameter_name: str
    parameter_stddev: float
    plant_barcode: str
    plant_id: int
    plant_name: str
    round_id: int
    tray_area: str
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> HcLeaf:
        return HcLeaf(
            analyse_id=obj.get("AnalyseID"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            leaf_index=obj.get("LeafIndex"),
            measure_angle=obj.get("MeasureAngle"),
            measure_id=obj.get("MeasureID"),
            parameter_avg=obj.get("ParameterAvg"),
            parameter_id=obj.get("ParameterID"),
            parameter_max=obj.get("ParameterMax"),
            parameter_median=obj.get("ParameterMedian"),
            parameter_min=obj.get("ParameterMin"),
            parameter_name=obj.get("ParameterName"),
            parameter_stddev=obj.get("ParameterStddev"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            plant_name=obj.get("PlantName"),
            round_id=obj.get("RoundID"),
            tray_area=obj.get("TrayArea"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class HcImagingMeasure:
    """Hyperspectral image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcImaging:
        if obj.get("JsonHcImagingByIDResult") is None:
            return None
        return HcImaging.from_dict(obj.get("JsonHcImagingByIDResult"))


@dataclass
class HcImagingWrapper:
    """Hyperspectral image for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcImaging]:
        if obj.get("JsonHcImagingResult") is None:
            return []
        return [HcImaging.from_dict(y) for y in obj.get("JsonHcImagingResult")]


@dataclass
class HcImagingExtendedDataMeasure:
    """Hyperspectral extended by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcMeasure:
        if obj.get("JsonHcMeasureExtendedDataByIDResult") is None:
            return None
        return HcMeasure.from_dict(obj.get("JsonHcMeasureExtendedDataByIDResult"))


@dataclass
class HcImagingExtendedData:
    """Hyperspectral extended for tray"""

    @staticmethod
    def from_dict(obj: Any) -> HcMeasure:
        if obj.get("JsonHcMeasureExtendedDataResult") is None:
            return None
        return HcMeasure.from_dict(obj.get("JsonHcMeasureExtendedDataResult"))


@dataclass
class HcRgbImageMeasure:
    """Hyperspectral rgb image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcRgb:
        if obj.get("JsonHcRgbImageByMeasureIDResult") is None:
            return None
        return HcRgb.from_dict(obj.get("JsonHcRgbImageByMeasureIDResult"))


@dataclass
class HcRgbImage:
    """Hyperspectral rgb image for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcRgb]:
        if obj.get("JsonHcRgbImageResult") is None:
            return []
        return [HcRgb.from_dict(y) for y in obj.get("JsonHcRgbImageResult")]


@dataclass
class HcPlantMaskMeasure:
    """Hyperspectral plant mask by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcMask:
        if obj.get("JsonHcPlantMaskByMeasureIDResult") is None:
            return None
        return HcMask.from_dict(obj.get("JsonHcPlantMaskByMeasureIDResult"))


@dataclass
class HcPlantMask:
    """Hyperspectral plant mask for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcMask]:
        if obj.get("JsonHcPlantMaskResult") is None:
            return []
        return [HcMask.from_dict(y) for y in obj.get("JsonHcPlantMaskResult")]


@dataclass
class HcParamWrapper:
    """Hyperspectral parameter by parm ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcParam:
        if obj.get("JsonHcParamResult") is None:
            return None
        return HcParam.from_dict(obj.get("JsonHcParamResult"))


@dataclass
class HcParamUsedAnalyse:
    """Hyperspectral parameters by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcParam]:
        if obj.get("JsonHcUsedParamByAnalyseIDResult") is None:
            return []
        return [HcParam.from_dict(y) for y in obj.get("JsonHcUsedParamByAnalyseIDResult")]


@dataclass
class HcParamUsed:
    """Hyperspectral parameters for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcParam]:
        if obj.get("JsonHcUsedParamResult") is None:
            return []
        return [HcParam.from_dict(y) for y in obj.get("JsonHcUsedParamResult")]


@dataclass
class HcParamImageAnalyse:
    """Hyperspectral image parameters by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> HcImage:
        if obj.get("JsonHcParameterImageByAnalyseIDResult") is None:
            return None
        return HcImage.from_dict(obj.get("JsonHcParameterImageByAnalyseIDResult"))


@dataclass
class HcParamImage:
    """Hyperspectral image parameters for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcImage]:
        if obj.get("JsonHcParameterImageResult") is None:
            return []
        return [HcImage.from_dict(y) for y in obj.get("JsonHcParameterImageResult")]


@dataclass
class HcPlantParamAnalyse:
    """Hyperspectral plant parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcPlant]:
        if obj.get("JsonHcPlantParamByAnalyseIDResult") is None:
            return []
        return [HcPlant.from_dict(y) for y in obj.get("JsonHcPlantParamByAnalyseIDResult")]


@dataclass
class HcPlantParam:
    """Hyperspectral plant parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcPlant]:
        if obj.get("JsonHcPlantParamResult") is None:
            return []
        return [HcPlant.from_dict(y) for y in obj.get("JsonHcPlantParamResult")]


@dataclass
class HcLeafParamAnalyse:
    """Hyperspectral leaf parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[HcLeaf]:
        if obj.get("JsonHcLeafParamByAnalyseIDResult") is None:
            return []
        return [HcLeaf.from_dict(y) for y in obj.get("JsonHcLeafParamByAnalyseIDResult")]


@dataclass
class HcLeafParam:
    """Hyperspectral leaf parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> 'HcLeaf':
        if obj.get("JsonHcLeafParamsResult") is None:
            return []
        return [HcLeaf.from_dict(y) for y in obj.get("JsonHcLeafParamsResult")]
