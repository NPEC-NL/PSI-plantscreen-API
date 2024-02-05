from dataclasses import dataclass
from typing import List
from typing import Any
import json

# IrImage baseclass
@dataclass
class IrImage:
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
    ImagePath: str
    

    @staticmethod
    def from_dict(obj: Any) -> 'IrImage':
        return IrImage(
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
            ImagePath=obj.get("ImagePath")
        )

# IrExtended baseclass
@dataclass
class IrExtended:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int
    

    @staticmethod
    def from_dict(obj: Any) -> 'IrExtended':
        return IrExtended(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )

# IrMask baseclass
@dataclass
class IrMask:
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
    def from_dict(obj: Any) -> 'IrMask':
        return IrMask(
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

# IrParam baseclass
@dataclass
class IrParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str


    @staticmethod
    def from_dict(obj: Any) -> 'IrParam':
        return IrParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit")
        )
    
# IrPlant baseclass
@dataclass
class IrPlant:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: int
    MeasureID: int
    ParameterAvg: float
    ParameterID: int
    ParameterMax: float
    ParameterMedian: float
    ParameterMin: float
    ParameterName: str
    ParameterStddev: float
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'IrPlant':
        return IrPlant(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            ParameterAvg=obj.get("ParameterAvg"),
            ParameterID=obj.get("ParameterID"),
            ParameterMax=obj.get("ParameterMax"),
            ParameterMedian=obj.get("ParameterMedian"),
            ParameterMin=obj.get("ParameterMin"),
            ParameterName=obj.get("ParameterName"),
            ParameterStddev=obj.get("ParameterStddev"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )

# IrLeaf baseclass
@dataclass
class IrLeaf:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    LeafIndex: int
    MeasureAngle: int
    MeasureID: int
    ParameterAvg: float
    ParameterID: int
    ParameterMax: float
    ParameterMedian: float
    ParameterMin: float
    ParameterName: str
    ParameterStddev: float
    PlantBarcode: str
    PlantID: int
    PlantName: str
    RoundID: int
    TrayArea: str
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'IrLeaf':
        return IrLeaf(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            LeafIndex=obj.get("LeafIndex"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            ParameterAvg=obj.get("ParameterAvg"),
            ParameterID=obj.get("ParameterID"),
            ParameterMax=obj.get("ParameterMax"),
            ParameterMedian=obj.get("ParameterMedian"),
            ParameterMin=obj.get("ParameterMin"),
            ParameterName=obj.get("ParameterName"),
            ParameterStddev=obj.get("ParameterStddev"),
            PlantBarcode=obj.get("PlantBarcode"),
            PlantID=obj.get("PlantID"),
            PlantName=obj.get("PlantName"),
            RoundID=obj.get("RoundID"),
            TrayArea=obj.get("TrayArea"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )


# Thermal image by measurement ID
@dataclass
class IrImagingMeasure:
    IrImage: IrImage

    @staticmethod
    def from_dict(obj: Any) -> 'IrImage':
        if obj.get("JsonIrImagingByIDResult") is None:
            return None
        
        return IrImage.from_dict(obj.get("JsonIrImagingByIDResult"))

# Thermal image for tray ID
@dataclass
class IrImaging:
    IrImage: IrImage

    @staticmethod
    def from_dict(obj: Any) -> 'IrImage':
        if obj.get("JsonIrImagingResult") is None:
            return None
        
        return [IrImage.from_dict(y) for y in obj.get("JsonIrImagingResult")] 

# Thermal extended by measurement ID
@dataclass
class IrImagingExtendedDataMeasure:
    IrExtended: IrExtended

    @staticmethod
    def from_dict(obj: Any) -> 'IrExtended':
        if obj.get("JsonIrMeasureExtendedDataByIDResult") is None:
            return None
        
        return IrExtended.from_dict(obj.get("JsonIrMeasureExtendedDataByIDResult"))

# Thermal extended for tray
@dataclass
class IrImagingExtendedData:
    IrExtended: IrExtended

    @staticmethod
    def from_dict(obj: Any) -> 'IrExtended':
        if obj.get("JsonIrMeasureExtendedDataResult") is None:
            return None
        
        return IrExtended.from_dict(obj.get("JsonIrMeasureExtendedDataResult"))

# Thermal mask by measurement ID
@dataclass
class IrPlantMaskMeasure:
    IrMask: IrMask

    @staticmethod
    def from_dict(obj: Any) -> 'IrMask':
        if obj.get("JsonIrPlantMaskByMeasureIDResult") is None:
            return None
        
        return IrMask.from_dict(obj.get("JsonIrPlantMaskByMeasureIDResult"))

# Thermal mask for tray
@dataclass
class IrPlantMask:
    IrMask: IrMask

    @staticmethod
    def from_dict(obj: Any) -> 'IrMask':
        if obj.get("JsonIrPlantMaskResult") is None:
            return None
        
        return [IrMask.from_dict(y) for y in obj.get("JsonIrPlantMaskResult")] 

# Thermal mask image by measurement ID
@dataclass
class IrPlantMaskImageMeasure:
    IrImage: IrImage

    @staticmethod
    def from_dict(obj: Any) -> 'IrImage':
        if obj.get("JsonIrPlantMaskImageByMeasureIDResult") is None:
            return None
        
        return IrImage.from_dict(obj.get("JsonIrPlantMaskImageByMeasureIDResult"))

# Thermal mask image for tray
@dataclass
class IrPlantMaskImage:
    IrImage: IrImage

    @staticmethod
    def from_dict(obj: Any) -> 'IrImage':
        if obj.get("JsonIrPlantMaskImageResult") is None:
            return None
        
        return [IrImage.from_dict(y) for y in obj.get("JsonIrPlantMaskImageResult")] 

# Thermal parameter by param ID
@dataclass
class IrParamWrappper:
    IrParam: IrParam

    @staticmethod
    def from_dict(obj: Any) -> 'IrParam':
        if obj.get("JsonIrParamResult") is None:
            return None
        
        return IrParam.from_dict(obj.get("JsonIrParamResult"))

# Thermal parameter by analysis ID
@dataclass
class IrParamUsedAnalyse:
    IrParam: IrParam

    @staticmethod
    def from_dict(obj: Any) -> 'IrParam':
        if obj.get("JsonIrUsedParamByAnalyseIDResult") is None:
            return None
        
        return [IrParam.from_dict(y) for y in obj.get("JsonIrUsedParamByAnalyseIDResult")] 

# Thermal parameter for tray
@dataclass
class IrParamUsed:
    IrParam: IrParam

    @staticmethod
    def from_dict(obj: Any) -> 'IrParam':
        if obj.get("JsonIrUsedParamResult") is None:
            return None
        
        return [IrParam.from_dict(y) for y in obj.get("JsonIrUsedParamResult")] 

# Thermal Statistic Plant Parameter Values by Analyse ID
@dataclass
class IrPlantParamAnalyse:
    IrPlant: IrPlant

    @staticmethod
    def from_dict(obj: Any) -> 'IrPlant':
        if obj.get("JsonIrPlantParamByAnalyseIDResult") is None:
            return None
        
        return [IrPlant.from_dict(y) for y in obj.get("JsonIrPlantParamByAnalyseIDResult")] 

# Thermal Statistic Plant Parameter Values for Tray
@dataclass
class IrPlantParam:
    IrPlant: IrPlant

    @staticmethod
    def from_dict(obj: Any) -> 'IrPlant':
        if obj.get("JsonIrPlantParamResult") is None:
            return None
        
        return [IrPlant.from_dict(y) for y in obj.get("JsonIrPlantParamResult")] 

# Thermal Statistic Leaf Parameter Values by Analyse ID
@dataclass
class IrLeafParamAnalyse:
    IrLeaf: IrLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'IrLeaf':
        if obj.get("JsonIrLeafParamByAnalyseIDResult") is None:
            return None
        
        return [IrLeaf.from_dict(y) for y in obj.get("JsonIrLeafParamByAnalyseIDResult")] 

# Thermal Statistic Leaf Parameter Values for Tray
@dataclass
class IrLeafParam:
    IrLeaf: IrLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'IrLeaf':
        if obj.get("JsonIrLeafParamResult") is None:
            return None
        
        return [IrLeaf.from_dict(y) for y in obj.get("JsonIrLeafParamResult")] 
