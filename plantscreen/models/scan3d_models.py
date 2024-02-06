from __future__ import annotations
from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Scan3dImage:
    """Scan3dImage baseclass"""
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
    scan_3d_model_path: str

    @staticmethod
    def from_dict(obj: Any) -> Scan3dImage:
        return Scan3dImage(
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
            scan_3d_model_path=obj.get("Scan3DModelPath")
        )


@dataclass
class Scan3dExtended:
    """Scan3dExtended baseclass"""
    device_id: int
    extended_data: str
    measure_date: str
    measure_id: int
    round_id: int
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> Scan3dExtended:
        return Scan3dExtended(
            device_id=obj.get("DeviceID"),
            extended_data=obj.get("ExtendedData"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            round_id=obj.get("RoundID"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class Scan3dAnalyze:
    """Scan3dAnalyze baseclass"""
    analyse_id: int
    analysed_model_path: str
    device_id: int
    device_pid: str
    experiment_id: int
    measure_date: str
    measure_id: int
    plant_barcode: str
    plant_id: int
    round_id: int
    tray_barcode: str
    tray_id: int

    @staticmethod
    def from_dict(obj: Any) -> Scan3dAnalyze:
        return Scan3dAnalyze(
            analyse_id=obj.get("AnalyseID"),
            analysed_model_path=obj.get("AnalysedModelPath"),
            device_id=obj.get("DeviceID"),
            device_pid=obj.get("DevicePID"),
            experiment_id=obj.get("ExperimentID"),
            measure_date=obj.get("MeasureDate"),
            measure_id=obj.get("MeasureID"),
            plant_barcode=obj.get("PlantBarcode"),
            plant_id=obj.get("PlantID"),
            round_id=obj.get("RoundID"),
            tray_barcode=obj.get("TrayBarcode"),
            tray_id=obj.get("TrayID")
        )


@dataclass
class Scan3dParam:
    """Scan3dParam baseclass"""
    parameter_id: int
    parameter_name: str
    parameter_unit: str

    @staticmethod
    def from_dict(obj: Any) -> Scan3dParam:
        return Scan3dParam(
            parameter_id=obj.get("ParameterID"),
            parameter_name=obj.get("ParameterName"),
            parameter_unit=obj.get("ParameterUnit")
        )


@dataclass
class Scan3dPlant:
    """Scan3dPlant baseclass"""
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
    def from_dict(obj: Any) -> Scan3dPlant:
        return Scan3dPlant(
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
class Scan3dLeaf:
    """Scan3dLeaf baseclass"""
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
    def from_dict(obj: Any) -> Scan3dLeaf:
        return Scan3dLeaf(
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
class Scan3dImagingMeasure:
    """3D Imaging by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> Scan3dImage:
        if obj.get("JsonScan3dImagingByIDResult") is None:
            return None
        return Scan3dImage.from_dict(obj.get("JsonScan3dImagingByIDResult"))


class Scan3d:
    """3D Imaging for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dImage]:
        if obj.get("JsonScan3dImagingResult") is None:
            return []
        return [Scan3dImage.from_dict(y) for y in obj.get("JsonScan3dImagingResult")]


@dataclass
class Scan3dImagingExtendedDataMeasure:
    """3D Extended Data by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> Scan3dExtended:
        if obj.get("JsonScan3DMeasureExtendedDataByIDResult") is None:
            return None
        return Scan3dExtended.from_dict(obj.get("JsonScan3DMeasureExtendedDataByIDResult"))


@dataclass
class Scan3dImagingExtendedData:
    """3D Extended Data for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> Scan3dExtended:
        if obj.get("JsonScan3dMeasureExtendedDataResult") is None:
            return None
        return Scan3dExtended.from_dict(obj.get("JsonScan3dMeasureExtendedDataResult"))


class Scan3dAnalyzedModelMeasure:
    """3D Analyzed Model by Measure ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dAnalyze]:
        if obj.get("JsonScan3dAnalyzedModelByMeasureIDResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelByMeasureIDResult")]


class Scan3dAnalysedModelAnalyse:
    """3D Analyzed Model by Analyse IDss"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dAnalyze]:
        if obj.get("JsonScan3dAnalyzedModelByAnalyseIDResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelByAnalyseIDResult")]


class Scan3dAnalyzedModel:
    """3D Analyzed Model for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dAnalyze]:
        if obj.get("JsonScan3dAnalyzedModelResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelResult")]


@dataclass
class Scan3dParamWrapper:
    """3D Parameter by ID"""

    @staticmethod
    def from_dict(obj: Any) -> Scan3dParam:
        if obj.get("JsonScan3dParamResult") is None:
            return None
        return Scan3dParam.from_dict(obj.get("JsonScan3dParamResult"))


class Scan3dParamUsedAnalyse:
    """3D Used Parameters by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dParam]:
        if obj.get("JsonScan3dUsedParamByAnalyseIDResult") is None:
            return []
        return [Scan3dParam.from_dict(y) for y in obj.get("JsonScan3dUsedParamByAnalyseIDResult")]


class Scan3dParamUsed:
    """3D Used Parameters for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dParam]:
        if obj.get("JsonScan3dUsedParamResult") is None:
            return []
        return [Scan3dParam.from_dict(y) for y in obj.get("JsonScan3dUsedParamResult")]


class Scan3dPlantParamAnalyse:
    """3D Plant Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dPlant]:
        if obj.get("JsonScan3dPlantParamByAnalyseIDResult") is None:
            return []
        return [Scan3dPlant.from_dict(y) for y in obj.get("JsonScan3dPlantParamByAnalyseIDResult")]


class Scan3dPlantParam:
    """3D Plant Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dPlant]:
        if obj.get("JsonScan3dPlantParamResult") is None:
            return []
        return [Scan3dPlant.from_dict(y) for y in obj.get("JsonScan3dPlantParamResult")]


class Scan3dLeafParamAnalyse:
    """3D Local Leaf Parameter Values by Analyse ID"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dLeaf]:
        if obj.get("JsonScan3dLeafParamByAnalyseIDResult") is None:
            return []
        return [Scan3dLeaf.from_dict(y) for y in obj.get("JsonScan3dLeafParamByAnalyseIDResult")]


class Scan3dLeafParam:
    """3D Local Leaf Parameter Values for Tray"""

    @staticmethod
    def from_dict(obj: Any) -> List[Scan3dLeaf]:
        if obj.get("JsonScan3dLeafParamResult") is None:
            return []
        return [Scan3dLeaf.from_dict(y) for y in obj.get("JsonScan3dLeafParamResult")]
