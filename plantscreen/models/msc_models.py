from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class MscImage:
    """MscImage baseclass"""
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
    def from_dict(obj: Any) -> MscImage:
        return MscImage(
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
class MscExtended:
    """MscExtended baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> MscExtended:
        return MscExtended(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class MscMask:
    """MscMask baseclass"""
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
    def from_dict(obj: Any) -> MscMask:
        return MscMask(
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
class MscParam:
    """MscParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> MscParam:
        return MscParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit")
        )


@dataclass
class MscParamImage:
    """MscParamImage baseclass"""
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
    def from_dict(obj: Any) -> MscParamImage:
        return MscParamImage(
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
class MscPlant:
    """MscPlant baseclass"""
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
    def from_dict(obj: Any) -> MscPlant:
        return MscPlant(
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
class MscLeaf:
    """MscLeaf baseclass"""
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
    def from_dict(obj: Any) -> MscLeaf:
        return MscLeaf(
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
class MscLight:
    """MscLight baseclass"""
    channel_id: int
    light_set_caption: str
    light_set_id: int
    light_set_pid_name: str
    light_set_valid: bool

    @staticmethod
    def from_dict(obj: Any) -> MscLight:
        return MscLight(
            channel_id=obj.get("ChannelID"),
            light_set_caption=obj.get("LightSetCaption"),
            light_set_id=obj.get("LightSetID"),
            light_set_pid_name=obj.get("LightSetPidName"),
            light_set_valid=obj.get("LightSetValid")
        )


@dataclass
class MscCalibrate:
    """MscCalibrate baseclass"""
    calibration_date: str
    calibration_id: int
    calibration_image_path: str
    camera_exposure: int
    camera_gain: int
    light_set_id: int

    @staticmethod
    def from_dict(obj: Any) -> MscCalibrate:
        return MscCalibrate(
            calibration_date=obj.get("CalibrationDate"),
            calibration_id=obj.get("CalibrationID"),
            calibration_image_path=obj.get("CalibrationImagePath"),
            camera_exposure=obj.get("CameraExposure"),
            camera_gain=obj.get("CameraGain"),
            light_set_id=obj.get("LightSetID")
        )


@dataclass
class MscCaliLight:
    """MscCaliLight baseclass"""
    calibration_id: int
    calibration_light_id: int
    calibration_light_level: int
    light_caption: str
    light_id: int
    light_set_id: int

    @staticmethod
    def from_dict(obj: Any) -> MscCaliLight:
        return MscCaliLight(
            calibration_id=obj.get("CalibrationID"),
            calibration_light_id=obj.get("CalibrationLightID"),
            calibration_light_level=obj.get("CalibrationLightLevel"),
            light_caption=obj.get("LightCaption"),
            light_id=obj.get("LightID"),
            light_set_id=obj.get("LightSetID")
        )


@dataclass
class MscImagingMeasure:
    """Multispectral Imaging by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscImage]:
        if obj.get("JsonMscImagingByIDResult") is None:
            return []
        return [MscImage.from_dict(y) for y in obj.get("JsonMscImagingByIDResult")]


@dataclass
class MscImaging:
    """Multispectral imaging for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscImage]:
        if obj.get("JsonMscImagingResult") is None:
            return []
        return [MscImage.from_dict(y) for y in obj.get("JsonMscImagingResult")]


class MscImagingExtendedDataMeasure:
    """Multispectral extended by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscExtended:
        if obj.get("JsonMscMeasureExtendedDataByIDResult") is None:
            return None
        return MscExtended.from_dict(obj.get("JsonMscMeasureExtendedDataByIDResult"))


class MscImagingExtendedData:
    """Multispectral extended for tray"""

    @staticmethod
    def from_dict(obj: Any) -> MscExtended:
        if obj.get("JsonMscMeasureExtendedDataResult") is None:
            return None
        return MscExtended.from_dict(obj.get("JsonMscMeasureExtendedDataResult"))


class MscPlantMaskMeasure:
    """Multispectral mask by measurement ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscMask:
        if obj.get("JsonMscPlantMaskByMeasureIDResult") is None:
            return None
        return MscMask.from_dict(obj.get("JsonMscPlantMaskByMeasureIDResult"))


@dataclass
class MscPlantMask:
    """Multispectral mask for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscMask]:
        if obj.get("JsonMscPlantMaskResult") is None:
            return []
        return [MscMask.from_dict(y) for y in obj.get("JsonMscPlantMaskResult")]


class MscParamWrapper:
    """Multispectral parameter by param ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscParam:
        if obj.get("JsonMscParamResult") is None:
            return None
        return MscParam.from_dict(obj.get("JsonMscParamResult"))


class MscParamUsedAnalyse:
    """Multispectral parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscParam]:
        if obj.get("JsonMscUsedParamByAnalyseIDResult") is None:
            return []
        return [MscParam.from_dict(y) for y in obj.get("JsonMscUsedParamByAnalyseIDResult")]


class MscParamUsed:
    """Multispectral parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscParam]:
        if obj.get("JsonMscUsedParamResult") is None:
            return []
        return [MscParam.from_dict(y) for y in obj.get("JsonMscUsedParamResult")]


class MscParamImageAnalyse:
    """Multispectral parameter image by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscParamImage:
        if obj.get("JsonMscParameterImageByAnalyseIDResult") is None:
            return None
        return MscParamImage.from_dict(obj.get("JsonMscParameterImageByAnalyseIDResult"))


class MscParamImageWrapper:
    """Multispectral parameter image for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscParamImage]:
        if obj.get("JsonMscParameterImageResult") is None:
            return []
        return [MscParamImage.from_dict(y) for y in obj.get("JsonMscParameterImageResult")]


class MscPlantParamAnalyse:
    """Multispectral plant parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscPlant]:
        if obj.get("JsonMscPlantParamByAnalyseIDResult") is None:
            return []
        return [MscPlant.from_dict(y) for y in obj.get("JsonMscPlantParamByAnalyseIDResult")]


class MscPlantParam:
    """Multispectral plant parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscPlant]:
        if obj.get("JsonMscPlantParamResult") is None:
            return []
        return [MscPlant.from_dict(y) for y in obj.get("JsonMscPlantParamResult")]


class MscLeafParamAnalyse:
    """Multispectral leaf parameter by analysis ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscLeaf]:
        if obj.get("JsonMscLeafParamByAnalyseIDResult") is None:
            return []
        return [MscLeaf.from_dict(y) for y in obj.get("JsonMscLeafParamByAnalyseIDResult")]


class MscLeafParam:
    """Multispectral leaf parameter for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscLeaf]:
        if obj.get("JsonMscLeafParamResult") is None:
            return []
        return [MscLeaf.from_dict(y) for y in obj.get("JsonMscLeafParamResult")]


class MscLightSet:
    """Multispectral light by ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscLight:
        if obj.get("JsonMscLightSetResult") is None:
            return None
        return MscLight.from_dict(obj.get("JsonMscLightSetResult"))


class MscLightSetUsed:
    """Multispectral light for tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscLight]:
        if obj.get("JsonMscLightSetUsedResult") is None:
            return []
        return [MscLight.from_dict(y) for y in obj.get("JsonMscLightSetUsedResult")]


class MscCalibration:
    """Multispectral calibration by ID"""

    @staticmethod
    def from_dict(obj: Any) -> MscCalibrate:
        if obj.get("JsonMscCalibrationResult") is None:
            return None
        return MscCalibrate.from_dict(obj.get("JsonMscCalibrationResult"))


class MscCalibrationLightSet:
    """Multispectral calibration by lightset ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscCalibrate]:
        if obj.get("JsonMscCalibrationByLightSetIDResult") is None:
            return []
        return [MscCalibrate.from_dict(y) for y in obj.get("JsonMscCalibrationByLightSetIDResult")]


# Multispectral calibration light by ID TODO


class MscCalibrationLight:
    """List multispectral calibration light settings"""

    @staticmethod
    def from_dict(obj: Any) -> List[MscCaliLight]:
        if obj.get("JsonMscCalibrationLightResult") is None:
            return []
        return [MscCaliLight.from_dict(y) for y in obj.get("JsonMscCalibrationLightResult")]
