from dataclasses import dataclass
from typing import List
from typing import Any
import json

# Scan3dImage baseclass
@dataclass
class Scan3dImage:
    ActionID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: float
    MeasureDate: str
    MeasureHeight: float
    MeasureID: int
    RoundID: int
    TrayBarcode: str
    TrayID: int
    TrayProfileID: int
    Scan3DModelPath: str

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dImage':
        return Scan3dImage(
            ActionID=obj.get("ActionID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureHeight=obj.get("MeasureHeight"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID"),
            TrayProfileID=obj.get("TrayProfileID"),
            Scan3DModelPath=obj.get("Scan3DModelPath")
        )

# Scan3dExtended baseclass
@dataclass
class Scan3dExtended:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dExtended':
        return Scan3dExtended(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )  

# Scan3dAnalyze baseclass
@dataclass
class Scan3dAnalyze:
    AnalyseID: int
    AnalysedModelPath: str
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureDate: str
    MeasureID: int
    PlantBarcode: str
    PlantID: int
    RoundID: int
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dAnalyze':
        return Scan3dAnalyze(
            AnalyseID=obj.get("AnalyseID"),
            AnalysedModelPath=obj.get("AnalysedModelPath"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )
    
# Scan3dParam baseclass
@dataclass
class Scan3dParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str


    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dParam':
        return Scan3dParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit")
        )

# Scan3dPlant baseclass
@dataclass
class Scan3dPlant:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: float
    MeasureID: int
    ParameterID: int
    ParameterName: str
    ParameterValue: float
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dPlant':
        return Scan3dPlant(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterValue=obj.get("ParameterValue"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )  
    
# Scan3dLeaf baseclass
@dataclass
class Scan3dLeaf:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    LeafIndex: int
    MeasureAngle: float
    MeasureID: int
    ParameterID: int
    ParameterName: str
    ParameterValue: float
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dLeaf':
        return Scan3dLeaf(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            LeafIndex=obj.get("LeafIndex"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterValue=obj.get("ParameterValue"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )
    
# 3D Imaging by Measure ID
@dataclass
class Scan3dImagingMeasure:
    Scan3dImage: Scan3dImage

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dImage':
        if obj.get("JsonScan3dImagingByIDResult") is None:
            return None
        return Scan3dImage.from_dict(obj.get("JsonScan3dImagingByIDResult"))

# 3D Imaging for Tray
class Scan3d:
    Scan3dImage: Scan3dImage

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dImage':
        if obj.get("JsonScan3dImagingResult") is None:
            return []
        return [Scan3dImage.from_dict(y) for y in obj.get("JsonScan3dImagingResult")] 

# 3D Extended Data by Measure ID
@dataclass
class Scan3dImagingExtendedDataMeasure:
    Scan3dExtended: Scan3dExtended

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dExtended':
        if obj.get("JsonScan3DMeasureExtendedDataByIDResult") is None:
            return None
        return Scan3dExtended.from_dict(obj.get("JsonScan3DMeasureExtendedDataByIDResult"))
    
# 3D Extended Data for Tray
@dataclass
class Scan3dImagingExtendedData:
    Scan3dExtended: Scan3dExtended

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dExtended':
        if obj.get("JsonScan3dMeasureExtendedDataResult") is None:
            return None
        return Scan3dExtended.from_dict(obj.get("JsonScan3dMeasureExtendedDataResult"))
    
# 3D Analyzed Model by Measure ID
class Scan3dAnalyzedModelMeasure:
    Scan3dAnalyze: Scan3dAnalyze

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dAnalyze':
        if obj.get("JsonScan3dAnalyzedModelByMeasureIDResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelByMeasureIDResult")] 

# 3D Analyzed Model by Analyse ID
class Scan3dAnalysedModelAnalyse:
    Scan3dAnalyze: Scan3dAnalyze 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dAnalyze':
        if obj.get("JsonScan3dAnalyzedModelByAnalyseIDResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelByAnalyseIDResult")] 

# 3D Analyzed Model for Tray
class Scan3dAnalyzedModel:
    Scan3dAnalyze: Scan3dAnalyze 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dAnalyze':
        if obj.get("JsonScan3dAnalyzedModelResult") is None:
            return []
        return [Scan3dAnalyze.from_dict(y) for y in obj.get("JsonScan3dAnalyzedModelResult")] 

# 3D Parameter by ID
@dataclass
class Scan3dParamWrapper:
    Scan3dParam: Scan3dParam

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dParam':
        if obj.get("JsonScan3dParamResult") is None:
            return None
        return Scan3dParam.from_dict(obj.get("JsonScan3dParamResult"))
    
# 3D Used Parameters by Analyse ID
class Scan3dParamUsedAnalyse:
    Scan3dParam: Scan3dParam 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dParam':
        if obj.get("JsonScan3dUsedParamByAnalyseIDResult") is None:
            return []
        return [Scan3dParam.from_dict(y) for y in obj.get("JsonScan3dUsedParamByAnalyseIDResult")] 

# 3D Used Parameters for Tray
class Scan3dParamUsed:
    Scan3dParam: Scan3dParam 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dParam':
        if obj.get("JsonScan3dUsedParamResult") is None:
            return []
        return [Scan3dParam.from_dict(y) for y in obj.get("JsonScan3dUsedParamResult")] 

# 3D Plant Parameter Values by Analyse ID
class Scan3dPlantParamAnalyse:
    Scan3dPlant: Scan3dPlant 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dPlant':
        if obj.get("JsonScan3dPlantParamByAnalyseIDResult") is None:
            return []
        return [Scan3dPlant.from_dict(y) for y in obj.get("JsonScan3dPlantParamByAnalyseIDResult")] 

# 3D Plant Parameter Values for Tray
class Scan3dPlantParam:
    Scan3dPlant: Scan3dPlant 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dPlant':
        if obj.get("JsonScan3dPlantParamResult") is None:
            return []
        return [Scan3dPlant.from_dict(y) for y in obj.get("JsonScan3dPlantParamResult")] 
    
# 3D Local Leaf Parameter Values by Analyse ID
class Scan3dLeafParamAnalyse:
    Scan3dLeaf: Scan3dLeaf 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dLeaf':
        if obj.get("JsonScan3dLeafParamByAnalyseIDResult") is None:
            return []
        return [Scan3dLeaf.from_dict(y) for y in obj.get("JsonScan3dLeafParamByAnalyseIDResult")] 

# 3D Local Leaf Parameter Values for Tray
class Scan3dLeafParam:
    Scan3dLeaf: Scan3dLeaf 

    @staticmethod
    def from_dict(obj: Any) -> 'Scan3dLeaf':
        if obj.get("JsonScan3dLeafParamResult") is None:
            return []
        return [Scan3dLeaf.from_dict(y) for y in obj.get("JsonScan3dLeafParamResult")] 















