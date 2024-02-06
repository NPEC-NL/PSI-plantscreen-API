from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class IrImage:
    """IrImage baseclass"""
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
    def from_dict(obj: Any) -> IrImage:
        return IrImage(
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
class IrExtended:
    """IrExtended baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> IrExtended:
        return IrExtended(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class IrMask:
    """IrMask baseclass"""
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
    def from_dict(obj: Any) -> IrMask:
        return IrMask(
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
class IrParam:
    """IrParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> IrParam:
        return IrParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit")
        )


@dataclass
class IrPlant:
    """IrPlant baseclass"""
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
    def from_dict(obj: Any) -> IrPlant:
        return IrPlant(
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
class IrLeaf:
    """IrLeaf baseclass"""
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
    def from_dict(obj: Any) -> IrLeaf:
        return IrLeaf(
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
class IrImagingMeasure:
    """Thermal image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> IrImage:
        if obj.get("JsonIrImagingByIDResult") is None:
            return None
        return IrImage.from_dict(obj.get("JsonIrImagingByIDResult"))


@dataclass
class IrImaging:
    """Thermal image for tray ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrImage]:
        if obj.get("JsonIrImagingResult") is None:
            return []
        return [IrImage.from_dict(y) for y in obj.get("JsonIrImagingResult")]


@dataclass
class IrImagingExtendedDataMeasure:
    """Thermal extended by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> IrExtended:
        if obj.get("JsonIrMeasureExtendedDataByIDResult") is None:
            return None
        return IrExtended.from_dict(obj.get("JsonIrMeasureExtendedDataByIDResult"))


@dataclass
class IrImagingExtendedData:
    """Thermal extended for tray"""

    @staticmethod
    def from_dict(obj: Any) -> IrExtended:
        if obj.get("JsonIrMeasureExtendedDataResult") is None:
            return None
        return IrExtended.from_dict(obj.get("JsonIrMeasureExtendedDataResult"))


@dataclass
class IrPlantMaskMeasure:
    """Thermal mask by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> IrMask:
        if obj.get("JsonIrPlantMaskByMeasureIDResult") is None:
            return None
        return IrMask.from_dict(obj.get("JsonIrPlantMaskByMeasureIDResult"))


@dataclass
class IrPlantMask:
    """Thermal mask for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrMask]:
        if obj.get("JsonIrPlantMaskResult") is None:
            return []
        return [IrMask.from_dict(y) for y in obj.get("JsonIrPlantMaskResult")]


@dataclass
class IrPlantMaskImageMeasure:
    """Thermal mask image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> IrImage:
        if obj.get("JsonIrPlantMaskImageByMeasureIDResult") is None:
            return None
        return IrImage.from_dict(obj.get("JsonIrPlantMaskImageByMeasureIDResult"))


@dataclass
class IrPlantMaskImage:
    """Thermal mask image for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrImage]:
        if obj.get("JsonIrPlantMaskImageResult") is None:
            return []
        return [IrImage.from_dict(y) for y in obj.get("JsonIrPlantMaskImageResult")]


@dataclass
class IrParamWrappper:
    """Thermal parameter by param ID"""

    @staticmethod
    def from_dict(obj: Any) -> IrParam:
        if obj.get("JsonIrParamResult") is None:
            return None
        return IrParam.from_dict(obj.get("JsonIrParamResult"))


@dataclass
class IrParamUsedAnalyse:
    """Thermal parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrParam]:
        if obj.get("JsonIrUsedParamByAnalyseIDResult") is None:
            return []
        return [IrParam.from_dict(y) for y in obj.get("JsonIrUsedParamByAnalyseIDResult")]


@dataclass
class IrParamUsed:
    """Thermal parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrParam]:
        if obj.get("JsonIrUsedParamResult") is None:
            return []
        return [IrParam.from_dict(y) for y in obj.get("JsonIrUsedParamResult")]


@dataclass
class IrPlantParamAnalyse:
    """Thermal Statistic Plant Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrPlant]:
        if obj.get("JsonIrPlantParamByAnalyseIDResult") is None:
            return []
        return [IrPlant.from_dict(y) for y in obj.get("JsonIrPlantParamByAnalyseIDResult")]


@dataclass
class IrPlantParam:
    """Thermal Statistic Plant Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrPlant]:
        if obj.get("JsonIrPlantParamResult") is None:
            return []
        return [IrPlant.from_dict(y) for y in obj.get("JsonIrPlantParamResult")]


@dataclass
class IrLeafParamAnalyse:
    """Thermal Statistic Leaf Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrLeaf]:
        if obj.get("JsonIrLeafParamByAnalyseIDResult") is None:
            return []
        return [IrLeaf.from_dict(y) for y in obj.get("JsonIrLeafParamByAnalyseIDResult")]


@dataclass
class IrLeafParam:
    """Thermal Statistic Leaf Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[IrLeaf]:
        if obj.get("JsonIrLeafParamResult") is None:
            return []
        return [IrLeaf.from_dict(y) for y in obj.get("JsonIrLeafParamResult")]
