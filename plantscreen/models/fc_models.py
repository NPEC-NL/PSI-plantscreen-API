from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class FcImaging:
    """FcImaging baseclass"""
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
    protocol_path: str
    tar_path: str

    @staticmethod
    def from_dict(obj: Any) -> FcImaging:
        return FcImaging(
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
            protocol_path=obj.get("ProtocolPath"),
            tar_path=obj.get("TarPath")
        )


@dataclass
class FcMeasure:
    """FcMeasure baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> FcMeasure:
        return FcMeasure(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class FcMask:
    """FcMask baseclass"""
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
    def from_dict(obj: Any) -> FcMask:
        return FcMask(
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
class FcParam:
    """FcParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> FcParam:
        return FcParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit"),
        )


@dataclass
class FcAnalyse:
    """FcAnalyse baseclass"""
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
    def from_dict(obj: Any) -> FcAnalyse:
        return FcAnalyse(
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
class FcPlant:
    """FcPlant baseclass"""
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
    def from_dict(obj: Any) -> FcPlant:
        return FcPlant(
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
class FcLeaf:
    """FcLeaf baseclass"""
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
    def from_dict(obj: Any) -> FcLeaf:
        return FcLeaf(
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
class FcImagingMeasure:
    """Flourcam image by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> FcImaging:
        if obj.get("JsonFcImagingByIDResult") is None:
            return None
        return FcImaging.from_dict(obj.get("JsonFcImagingByIDResult"))


@dataclass
class FcImagingWrapper:
    """Fluorcam image for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcImaging]:
        if obj.get("JsonFcImagingResult") is None:
            return []
        return [FcImaging.from_dict(y) for y in obj.get("JsonFcImagingResult")]


@dataclass
class FcImagingExtendedDataMeasure:
    """Fluorcam extended data by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> FcMeasure:
        if obj.get("JsonFcMeasureExtendedDataByIDResult") is None:
            return None
        return FcMeasure.from_dict(obj.get("JsonFcMeasureExtendedDataByIDResult"))


@dataclass
class FcImagingExtendedData:
    """Fluorcam extended data for tray"""

    @staticmethod
    def from_dict(obj: Any) -> FcMeasure:
        if obj.get("JsonFcMeasureExtendedDataResult") is None:
            return None
        return FcMeasure.from_dict(obj.get("JsonFcMeasureExtendedDataResult"))


@dataclass
class FcPlantMaskMeasure:
    """Fluorcam mask by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> FcMask:
        if obj.get("JsonFcPlantMaskByMeasureIDResult") is None:
            return None
        return FcMask.from_dict(obj.get("JsonFcPlantMaskByMeasureIDResult"))


@dataclass
class FcPlantMask:
    """Fluorcam mask for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcMask]:
        if obj.get("JsonFcPlantMaskResult") is None:
            return []
        return [FcMask.from_dict(y) for y in obj.get("JsonFcPlantMaskResult")]


@dataclass
class FcParamWrapper:
    """Fluorcam parameter by parm ID"""

    @staticmethod
    def from_dict(obj: Any) -> FcParam:
        if obj.get("JsonFcParamResult") is None:
            return None
        return FcParam.from_dict(obj.get("JsonFcParamResult"))


@dataclass
class FcParamUsedAnalyse:
    """Fluorcam parameters by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcParam]:
        if obj.get("JsonFcUsedParamByAnalyseIDResult") is None:
            return []
        return [FcParam.from_dict(y) for y in obj.get("JsonFcUsedParamByAnalyseIDResult")]


@dataclass
class FcParamUsed:
    """Fluorcam paramaters for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcParam]:
        if obj.get("JsonFcUsedParamResult") is None:
            return []
        return [FcParam.from_dict(y) for y in obj.get("JsonFcUsedParamResult")]


@dataclass
class FcParamImageAnalyse:
    """Fluorcam image parameters by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcAnalyse]:
        if obj.get("JsonFcUsedParamByAnalyseIDResult") is None:
            return []
        return [FcAnalyse.from_dict(y) for y in obj.get("JsonFcUsedParamByAnalyseIDResult")]


@dataclass
class FcParamImage:
    """Fluorcam image parameters for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcAnalyse]:
        if obj.get("JsonFcParameterImageResult") is None:
            return []
        return [FcAnalyse.from_dict(y) for y in obj.get("JsonFcParameterImageResult")]


@dataclass
class FcPlantParamAnalyse:
    """Fluorcam plant parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcPlant]:
        if obj.get("JsonFcPlantParamByAnalyseIDResult") is None:
            return []
        return [FcPlant.from_dict(y) for y in obj.get("JsonFcPlantParamByAnalyseIDResult")]


@dataclass
class FcPlantParam:
    """Fluorcam plant parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcPlant]:
        if obj.get("JsonFcPlantParamResult") is None:
            return []
        return [FcPlant.from_dict(y) for y in obj.get("JsonFcPlantParamResult")]


@dataclass
class FcLeafParamAnalyse:
    """FluorCam Leaf Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcLeaf]:
        if obj.get("JsonFcLeafParamByAnalyseIDResult") is None:
            return []
        return [FcLeaf.from_dict(y) for y in obj.get("JsonFcLeafParamByAnalyseIDResult")]


@dataclass
class FcLeafParam:
    """Fluorcam leaf parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[FcLeaf]:
        if obj.get("JsonFcLeafParamResult") is None:
            return []
        return [FcLeaf.from_dict(y) for y in obj.get("JsonFcLeafParamResult")]
