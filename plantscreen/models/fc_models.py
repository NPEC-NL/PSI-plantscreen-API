from dataclasses import dataclass
from typing import List
from typing import Any
import json

# FcImaging baseclass
@dataclass
class FcImaging:
    ActionID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: int
    MeasureDate: str
    MeasureHeight: int
    MeasureID: int
    RoundID: int
    TrayBarcode: str
    TrayID: int
    TrayProfileID: int
    ProtocolPath: str
    TarPath: str

    @staticmethod
    def from_dict(obj: Any) -> 'FcImaging':
        return FcImaging(
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
            ProtocolPath=obj.get("ProtocolPath"),
            TarPath=obj.get("TarPath")
        )

# FcMeasure baseclass
@dataclass
class FcMeasure:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'FcMeasure':
        return FcMeasure(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )

# FcMask baseclass
@dataclass
class FcMask:
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MaskIsLeaf: bool
    MeasureAngle: int
    MeasureDate: str
    MeasureID: int
    PlantMaskPath: str
    RoundID: int
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'FcMask':
        return FcMask(
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MaskIsLeaf=obj.get("MaskIsLeaf"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            PlantMaskPath=obj.get("PlantMaskPath"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )

# FcParam baseclass
@dataclass
class FcParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str

    @staticmethod
    def from_dict(obj: Any) -> 'FcParam':
        return FcParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit"),
        )
    
# FcAnalyse baseclass
@dataclass
class FcAnalyse:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: int
    MeasureID: int
    ParameterID: int
    ParameterImagePath: str
    ParameterName: str
    RoundID: int
    TrayBarcode: str
    TrayID: int
        

    @staticmethod
    def from_dict(obj: Any) -> 'FcAnalyse':
        return FcAnalyse(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            ParameterID=obj.get("ParameterID"),
            ParameterImagePath=obj.get("ParameterImagePath"),
            ParameterName=obj.get("ParameterName"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")

        )
    
# FcPlant baseclass
@dataclass
class FcPlant:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: int
    MeasureID: int
    ParameterID: int
    ParameterName: str
    ParameterValue: int
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'FcPlant':
        return FcPlant(
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

# FcLeaf baseclass
@dataclass
class FcLeaf:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    LeafIndex: int
    MeasureAngle: int
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
    def from_dict(obj: Any) -> 'FcLeaf':
        return FcLeaf(
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

# Flourcam image by measurement ID
@dataclass
class FcImagingMeasure:
    FcImaging: FcImaging

    @staticmethod
    def from_dict(obj: Any) -> 'FcImaging':
        return FcImaging.from_dict(obj.get("JsonFcImagingByIDResult"))
    

# Fluorcam image for tray
@dataclass
class FcImagingWrapper:
    FcImaging: FcImaging

    @staticmethod
    def from_dict(obj: Any) -> 'FcImaging':
        return [FcImaging.from_dict(y) for y in obj.get("JsonFcImagingResult")]    
    
# Fluorcam extended data by measurement ID
@dataclass
class FcImagingExtendedDataMeasure:
    FcMeasure: FcMeasure

    @staticmethod
    def from_dict(obj: Any) -> 'FcMeasure':
        return FcMeasure.from_dict(obj.get("JsonFcMeasureExtendedDataByIDResult"))

# Fluorcam extended data for tray
@dataclass
class FcImagingExtendedData:
    FcMeasure: FcMeasure

    @staticmethod
    def from_dict(obj: Any) -> 'FcMeasure':
        return FcMeasure.from_dict(obj.get("JsonFcMeasureExtendedDataResult"))

# Fluorcam mask by measurement ID
@dataclass
class FcPlantMaskMeasure:
    FcMask: FcMask

    @staticmethod
    def from_dict(obj: Any) -> 'FcMask':
        if obj.get("JsonFcPlantMaskByMeasureIDResult") is None:
                   return None
        return FcMask.from_dict(obj.get("JsonFcPlantMaskByMeasureIDResult"))

# Fluorcam mask for tray
@dataclass
class FcPlantMask:
    FcMask: FcMask

    @staticmethod
    def from_dict(obj: Any) -> 'FcMask':
        return [FcMask.from_dict(y) for y in obj.get("JsonFcPlantMaskResult")]    

# Fluorcam parameter by parm ID
@dataclass
class FcParamWrapper:
    FcParam: FcParam

    @staticmethod
    def from_dict(obj: Any) -> 'FcParam':
        return FcParam.from_dict(obj.get("JsonFcParamResult"))
    
# Fluorcam parameters by analysis ID
@dataclass
class IFcParamUsedAnalyse:
    FcParam: FcParam

    @staticmethod
    def from_dict(obj: Any) -> 'FcParam':
        return [FcParam.from_dict(y) for y in obj.get("JsonFcUsedParamByAnalyseIDResult")] 

# Fluorcam paramaters for tray
@dataclass
class FcParamUsed:
    FcParam: FcParam

    @staticmethod
    def from_dict(obj: Any) -> 'FcParam':
        return [FcParam.from_dict(y) for y in obj.get("JsonFcUsedParamResult")] 

# Fluorcam image parameters by analysis ID
@dataclass
class FcParamImageAnalyse:
    FcAnalyse: FcAnalyse
    
    @staticmethod
    def from_dict(obj: Any) -> 'FcAnalyse':
        if obj.get("JsonFcUsedParamByAnalyseIDResult") is None:
            return []
        return [FcAnalyse.from_dict(y) for y in obj.get("JsonFcUsedParamByAnalyseIDResult")] 
    
# Fluorcam image parameters for tray
@dataclass
class FcParamImage:
    FcAnalyse: FcAnalyse

    @staticmethod
    def from_dict(obj: Any) -> 'FcAnalyse':
        return [FcAnalyse.from_dict(y) for y in obj.get("JsonFcParameterImageResult")] 

# Fluorcam plant parameter by analysis ID
@dataclass
class FcPlantParamAnalyse:
    FcPlant: FcPlant

    @staticmethod
    def from_dict(obj: Any) -> 'FcPlant':
        return [FcPlant.from_dict(y) for y in obj.get("JsonFcPlantParamByAnalyseIDResult")] 

# Fluorcam plant parameter for tray
@dataclass
class FcPlantParam:
    FcPlant: FcPlant

    @staticmethod
    def from_dict(obj: Any) -> 'FcPlant':
        return [FcPlant.from_dict(y) for y in obj.get("JsonFcPlantParamResult")] 
    
# FluorCam Leaf Parameter Values by Analyse ID
@dataclass
class FcLeafParamAnalyse:
    FcLeaf: FcLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'FcLeaf':
        return [FcLeaf.from_dict(y) for y in obj.get("JsonFcLeafParamByAnalyseIDResult")] 
    
# Fluorcam leaf parameter for tray
@dataclass
class FcLeafParam:
    FcLeaf: FcLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'FcLeaf':
        return [FcLeaf.from_dict(y) for y in obj.get("JsonFcLeafParamResult")] 
    