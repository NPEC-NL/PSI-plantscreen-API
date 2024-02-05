from dataclasses import dataclass
from typing import List
from typing import Any
import json

# HcImaging baseclass
@dataclass
class HcImaging:
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
    CalibrationDarkContentPath: str
    CalibrationDarkHeaderPath: str
    CalibrationWhiteContentPath: str
    CalibrationWhiteHeaderPath: str
    DataContentPath: str
    DataHeaderPath: str

    @staticmethod
    def from_dict(obj: Any) -> 'HcImaging':
        return HcImaging(
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
            CalibrationDarkContentPath=obj.get("CalibrationDarkContentPath"),
            CalibrationDarkHeaderPath=obj.get("CalibrationDarkHeaderPath"),
            CalibrationWhiteContentPath=obj.get("CalibrationWhiteContentPath"),
            CalibrationWhiteHeaderPath=obj.get("CalibrationWhiteHeaderPath"),
            DataContentPath=obj.get("DataContentPath"),
            DataHeaderPath=obj.get("DataHeaderPath")
        )
    
# HcMeasure baseclass
@dataclass
class HcMeasure:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'HcMeasure':
        return HcMeasure(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )
    
# HcRgb baseclass
@dataclass
class HcRgb:
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: float
    MeasureID: int
    RgbImagePath: str
    RoundID: int
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'HcRgb':
        return HcRgb(
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
            ExperimentID=obj.get("ExperimentID"),
            MeasureAngle=obj.get("MeasureAngle"),
            MeasureID=obj.get("MeasureID"),
            RgbImagePath=obj.get("RgbImagePath"),
            RoundID=obj.get("RoundID"),
            TrayBarcode=obj.get("TrayBarcode"),
            TrayID=obj.get("TrayID")
        )
    
# HcMask baseclass
@dataclass
class HcMask:
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MaskIsLeaf: bool
    MeasureAngle: float
    MeasureDate: str
    MeasureID: int
    PlantMaskPath: str
    RoundID: int
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'HcMask':
        return HcMask(
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
    
# HcParam baseclass
@dataclass
class HcParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str

    @staticmethod
    def from_dict(obj: Any) -> 'HcParam':
        return HcParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit")
        )

# HcImage baseclass
@dataclass
class HcImage:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: float
    MeasureID: int
    ParameterID: int
    ParameterImagePath: str
    ParameterName: str
    RoundID: int
    TrayBarcode: str
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'HcImage':
        return HcImage(
            AnalyseID=obj.get("AnalyseID"),
            DeviceID=obj.get("DeviceID"),
            DevicePID=obj.get("DevicePID"),
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

# HcPlant baseclass
@dataclass
class HcPlant:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    MeasureAngle: float
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
    def from_dict(obj: Any) -> 'HcPlant':
        return HcPlant(
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

# HcLeaf baseclass
@dataclass
class HcLeaf:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
    LeafIndex: int
    MeasureAngle: float
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
    def from_dict(obj: Any) -> 'HcLeaf':
        return HcLeaf(
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


# Hyperspectral image by measurement ID
@dataclass
class HcImagingMeasure:
    HcImaging: HcImaging

    @staticmethod
    def from_dict(obj: Any) -> 'HcImaging':
        if obj.get("JsonHcImagingByIDResult") is None:
            return None
        
        return HcImaging.from_dict(obj.get("JsonHcImagingByIDResult"))
    
# Hyperspectral image for tray
@dataclass
class HcImagingWrapper:
    HcImaging: HcImaging

    @staticmethod
    def from_dict(obj: Any) -> 'HcImaging':
        if obj.get("JsonHcImagingResult") is None:
            return []
        
        return [HcImaging.from_dict(y) for y in obj.get("JsonHcImagingResult")] 

# Hyperspectral extended by measurement ID
@dataclass
class HcImagingExtendedDataMeasure:
    HcMeasure: HcMeasure

    @staticmethod
    def from_dict(obj: Any) -> 'HcMeasure':
        if obj.get("JsonHcMeasureExtendedDataByIDResult") is None:
            return None
        
        return HcMeasure.from_dict(obj.get("JsonHcMeasureExtendedDataByIDResult"))

# Hyperspectral extended for tray
@dataclass
class HcImagingExtendedData:
    HcMeasure: HcMeasure

    @staticmethod
    def from_dict(obj: Any) -> 'HcMeasure':
        if obj.get("JsonHcMeasureExtendedDataResult") is None:
            return None
        
        return HcMeasure.from_dict(obj.get("JsonHcMeasureExtendedDataResult"))    

# Hyperspectral rgb image by measurement ID
@dataclass
class HcRgbImageMeasure:
    HcRgb: HcRgb

    @staticmethod
    def from_dict(obj: Any) -> 'HcRgb':
        if obj.get("JsonHcRgbImageByMeasureIDResult") is None:
            return None
        
        return HcRgb.from_dict(obj.get("JsonHcRgbImageByMeasureIDResult"))    
    
# Hyperspectral rgb image for tray
@dataclass
class HcRgbImage:
    HcRgb: HcRgb

    @staticmethod
    def from_dict(obj: Any) -> 'HcRgb':
        if obj.get("JsonHcRgbImageResult") is None:
            return []
        
        return [HcRgb.from_dict(y) for y in obj.get("JsonHcRgbImageResult")] 
    
# Hyperspectral plant mask by measurement ID
@dataclass
class HcPlantMaskMeasure:
    HcMask: HcMask

    @staticmethod
    def from_dict(obj: Any) -> 'HcMask':
        if obj.get("JsonHcPlantMaskByMeasureIDResult") is None:
            return None
        
        return HcMask.from_dict(obj.get("JsonHcPlantMaskByMeasureIDResult"))    
    
# Hyperspectral plant mask for tray
@dataclass
class HcPlantMask:
    HcMask: HcMask

    @staticmethod
    def from_dict(obj: Any) -> 'HcMask':
        if obj.get("JsonHcPlantMaskResult") is None:
            return []
        
        return [HcMask.from_dict(y) for y in obj.get("JsonHcPlantMaskResult")] 
    
# Hyperspectral parameter by parm ID
@dataclass
class HcParamWrapper:
    HcParam: HcParam

    @staticmethod
    def from_dict(obj: Any) -> 'HcParam':
        if obj.get("JsonHcParamResult") is None:
            return None
        
        return HcParam.from_dict(obj.get("JsonHcParamResult"))    
    
# Hyperspectral parameters by analysis ID
@dataclass
class HcParamUsedAnalyse:
    HcParam: HcParam

    @staticmethod
    def from_dict(obj: Any) -> 'HcParam':
        if obj.get("JsonHcUsedParamByAnalyseIDResult") is None:
            return []
        
        return [HcParam.from_dict(y) for y in obj.get("JsonHcUsedParamByAnalyseIDResult")] 

# Hyperspectral parameters for tray
@dataclass
class HcParamUsed:
    HcParam: HcParam

    @staticmethod
    def from_dict(obj: Any) -> 'HcParam':
        if obj.get("JsonHcUsedParamResult") is None:
            return []
        
        return [HcParam.from_dict(y) for y in obj.get("JsonHcUsedParamResult")] 
    
# Hyperspectral image parameters by analysis ID
@dataclass
class HcParamImageAnalyse:
    HcImage: HcImage

    @staticmethod
    def from_dict(obj: Any) -> 'HcImage':
        if obj.get("JsonHcParameterImageByAnalyseIDResult") is None:
            return None
        
        return HcImage.from_dict(obj.get("JsonHcParameterImageByAnalyseIDResult"))    

# Hyperspectral image parameters for tray
@dataclass
class HcParamImage:
    HcImage: HcImage

    @staticmethod
    def from_dict(obj: Any) -> 'HcImage':
        if obj.get("JsonHcParameterImageResult") is None:
            return []
        
        return [HcImage.from_dict(y) for y in obj.get("JsonHcParameterImageResult")]         

# Hyperspectral plant parameter by analysis ID
@dataclass
class HcPlantParamAnalyse:
    HcPlant: HcPlant

    @staticmethod
    def from_dict(obj: Any) -> 'HcPlant':
        if obj.get("JsonHcPlantParamByAnalyseIDResult") is None:
            return []
        
        return [HcPlant.from_dict(y) for y in obj.get("JsonHcPlantParamByAnalyseIDResult")]    

# Hyperspectral plant parameter for tray
@dataclass
class HcPlantParam:
    HcPlant: HcPlant

    @staticmethod
    def from_dict(obj: Any) -> 'HcPlant':
        if obj.get("JsonHcPlantParamResult") is None:
            return []
        
        return [HcPlant.from_dict(y) for y in obj.get("JsonHcPlantParamResult")]    

# Hyperspectral leaf parameter by analysis ID
@dataclass
class HcLeafParamAnalyse:
    HcLeaf: HcLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'HcLeaf':
        if obj.get("JsonHcLeafParamByAnalyseIDResult") is None:
            return []
        
        return [HcLeaf.from_dict(y) for y in obj.get("JsonHcLeafParamByAnalyseIDResult")]   

# Hyperspectral leaf parameter for tray
@dataclass
class HcLeafParam:
    HcLeaf: HcLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'HcLeaf':
        if obj.get("JsonHcLeafParamsResult") is None:
            return []
        
        return [HcLeaf.from_dict(y) for y in obj.get("JsonHcLeafParamsResult")]   