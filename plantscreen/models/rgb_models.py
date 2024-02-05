from dataclasses import dataclass
from typing import List
from typing import Any
import json

# RgbImage baseclass
@dataclass
class RgbImage:
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
    def from_dict(obj: Any) -> 'RgbImage':
        return RgbImage(
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
    
# RgbExtended baseclass
@dataclass
class RgbExtended:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'RgbExtended':
        return RgbExtended(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )

# RgbMask baseclass
@dataclass
class RgbMask:
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
    def from_dict(obj: Any) -> 'RgbMask':
        return RgbMask(
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
    
# RgbGreen baseclass
@dataclass
class RgbGreen:
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
    GreeningPicturePath: str

    @staticmethod
    def from_dict(obj: Any) -> 'RgbGreen':
        return RgbGreen(
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
            GreeningPicturePath=obj.get("GreeningPicturePath")
        )

# RgbParam baseclass
@dataclass
class RgbParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str


    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        return RgbParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit")
        )

# RgbPlant baseclass
@dataclass
class RgbPlant:
    AnalyseID: int
    DeviceID: int
    DevicePID: str
    ExperimentID: int
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
    def from_dict(obj: Any) -> 'RgbPlant':
        return RgbPlant(
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

# RgbLeaf baseclass
@dataclass
class RgbLeaf:
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
    def from_dict(obj: Any) -> 'RgbLeaf':
        return RgbLeaf(
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

# RGB image by measurement ID
@dataclass
class RgbImagingMeasure:
    RgbImage: RgbImage

    @staticmethod
    def from_dict(obj: Any) -> 'RgbImage':
        if obj.get("JsonRgbImagingByIDResult") is None:
            return None
        return RgbImage.from_dict(obj.get("JsonRgbImagingByIDResult"))

# RGB Imaging for Tray
@dataclass
class RgbImaging:
    RgbImage: RgbImage

    @staticmethod
    def from_dict(obj: Any) -> 'RgbImage':
        if obj.get("JsonRgbImagingResult") is None:
            return None
        return [RgbImage.from_dict(y) for y in obj.get("JsonRgbImagingResult")] 
    
# RGB Extended Data by Measure ID
class RgbImagingExtendedDataMeasure:
    RgbExtended: RgbExtended

    @staticmethod
    def from_dict(obj: Any) -> 'RgbExtended':
        if obj.get("JsonRgbMeasureExtendedDataByIDResult") is None:
            return None
        return RgbExtended.from_dict(obj.get("JsonRgbMeasureExtendedDataByIDResult"))
    
# RGB Extended Data for Tray
class RgbImagingExtendedData:
    RgbExtended: RgbExtended

    @staticmethod
    def from_dict(obj: Any) -> 'RgbExtended':
        if obj.get("JsonRgbMeasureExtendedDataResult") is None:
            return None
        return RgbExtended.from_dict(obj.get("JsonRgbMeasureExtendedDataResult"))
    
# RGB Plant Mask by Measure ID
class RgbPlantMaskMeasure:
    RgbMask: RgbMask

    @staticmethod
    def from_dict(obj: Any) -> 'RgbMask':
        if obj.get("JsonRgbPlantMaskByMeasureIDResult") is None:
            return None
        return RgbMask.from_dict(obj.get("JsonRgbPlantMaskByMeasureIDResult"))
    
# RGB Plant Mask for Tray
@dataclass
class RgbPlantMask:
    RgbMask: RgbMask

    @staticmethod
    def from_dict(obj: Any) -> 'RgbMask':
        if obj.get("JsonRgbPlantMaskResult") is None:
            return None
        return [RgbMask.from_dict(y) for y in obj.get("JsonRgbPlantMaskResult")] 


# RGB Greening Mask Image by Measure ID
class RgbGreeningMaskImageMeasure:
    RgbGreen: RgbGreen

    @staticmethod
    def from_dict(obj: Any) -> 'RgbGreen':
        if obj.get("JsonRgbGreeningMaskImageByMeasureIDResult") is None:
            return None
        return RgbGreen.from_dict(obj.get("JsonRgbGreeningMaskImageByMeasureIDResult"))

# RGB Greening Mask Image for Tray
class RgbGreeningMaskImage:
    RgbGreen: RgbGreen

    @staticmethod
    def from_dict(obj: Any) -> 'RgbGreen':
        if obj.get("JsonRgbGreeningMaskImageResult") is None:
            return None
        return [RgbGreen.from_dict(y) for y in obj.get("JsonRgbGreeningMaskImageResult")] 

# RGB Parameter by ID
class RgbParamWrapper:
    RgbParam: RgbParam

    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        if obj.get("JsonRgbParamResult") is None:
            return None
        return RgbParam.from_dict(obj.get("JsonRgbParamResult"))
    
# RGB Used Parameters by Analyse ID
class RgbParamUsedAnalyse:
    RgbParam: RgbParam

    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        if obj.get("JsonRgbUsedParamByAnalyseIDResult") is None:
            return None
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamByAnalyseIDResult")] 
    
# RGB Used Parameters for Tray
class RgbParamUsed:
    RgbParam: RgbParam

    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        if obj.get("JsonRgbcUsedParamsResult") is None:
            return None
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbcUsedParamsResult")] 

# RGB Used Color Parameters by Analyse ID
class RgbParamColorUsedAnalyse:
    RgbParam: RgbParam

    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        if obj.get("JsonRgbUsedParamColorByAnalyseIDResult") is None:
            return None
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamColorByAnalyseIDResult")]     

# RGB Used Color Parameters for Tray
class RgbParamColorUsed:
    RgbParam: RgbParam

    @staticmethod
    def from_dict(obj: Any) -> 'RgbParam':
        if obj.get("JsonRgbUsedParamColorResult") is None:
            return None
        return [RgbParam.from_dict(y) for y in obj.get("JsonRgbUsedParamColorResult")]     

# RGB Plant Parameter Values by Analyse ID
class RgbPlantParamAnalyse:
    RgbPlant: RgbPlant

    @staticmethod
    def from_dict(obj: Any) -> 'RgbPlant':
        if obj.get("JsonRgbPlantParamByAnalyseIDResult") is None:
            return None
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamByAnalyseIDResult")]     

# RGB Plant Parameter Values for Tray
class RgbPlantParam:
    RgbPlant: RgbPlant

    @staticmethod
    def from_dict(obj: Any) -> 'RgbPlant':
        if obj.get("JsonRgbPlantParamResult") is None:
            return None
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamResult")]     

# RGB Color Plant Parameter Values by Analyse ID
class RgbPlantParamColorAnalyse:
    RgbPlant: RgbPlant

    @staticmethod
    def from_dict(obj: Any) -> 'RgbPlant':
        if obj.get("JsonRgbPlantParamColorByAnalyseIDResult") is None:
            return None
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamColorByAnalyseIDResult")]     
    
# RGB Color Plant Parameter Values for Tray
class RgbPlantParamColor:
    RgbPlant: RgbPlant

    @staticmethod
    def from_dict(obj: Any) -> 'RgbPlant':
        if obj.get("JsonRgbPlantParamColorResult") is None:
            return None
        return [RgbPlant.from_dict(y) for y in obj.get("JsonRgbPlantParamColorResult")]     

# RGB Leaf Parameter Values by Analyse ID
class RgbLeafParamAnalyse:
    RgbLeaf: RgbLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'RgbLeaf':
        if obj.get("JsonRgbLeafParamByAnalyseIDResult") is None:
            return None
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamByAnalyseIDResult")]   
    
# RGB Leaf Parameter Values for Tray
class RgbLeafParam:
    RgbLeaf: RgbLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'RgbLeaf':
        if obj.get("JsonRgbLeafParamResult") is None:
            return None
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamResult")]   
    
# RGB Color Leaf Parameter Values by Analyse ID
class RgbLeafParamColorAnalyse:
    RgbLeaf: RgbLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'RgbLeaf':
        if obj.get("JsonRgbLeafParamColorByAnalyseIDResult") is None:
            return None
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamColorByAnalyseIDResult")]   

# RGB Color Leaf Parameter Values for Tray
class RgbLeafParamColor:
    RgbLeaf: RgbLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'RgbLeaf':
        if obj.get("JsonRgbLeafParamColorResult") is None:
            return None
        return [RgbLeaf.from_dict(y) for y in obj.get("JsonRgbLeafParamColorResult")]   

