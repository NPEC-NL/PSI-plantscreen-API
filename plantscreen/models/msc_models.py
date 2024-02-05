from dataclasses import dataclass
from typing import List
from typing import Any
import json

# MscImage baseclass
@dataclass
class MscImage:
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
    def from_dict(obj: Any) -> 'MscImage':
        return MscImage(
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
    
# MscExtended baseclass
@dataclass
class MscExtended:
    DeviceID: int
    ExtendedData: str
    MeasureDate: str
    MeasureID: int
    RoundID: int
    TrayID: int

    @staticmethod
    def from_dict(obj: Any) -> 'MscExtended':
        return MscExtended(
            DeviceID=obj.get("DeviceID"),
            ExtendedData=obj.get("ExtendedData"),
            MeasureDate=obj.get("MeasureDate"),
            MeasureID=obj.get("MeasureID"),
            RoundID=obj.get("RoundID"),
            TrayID=obj.get("TrayID")
        )
    
# MscMask baseclass
@dataclass
class MscMask:
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
    def from_dict(obj: Any) -> 'MscMask':
        return MscMask(
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
    
# MscParam baseclass
@dataclass
class MscParam:
    ParameterID: int
    ParameterName: str
    ParameterUnit: str


    @staticmethod
    def from_dict(obj: Any) -> 'MscParam':
        return MscParam(
            ParameterID=obj.get("ParameterID"),
            ParameterName=obj.get("ParameterName"),
            ParameterUnit=obj.get("ParameterUnit")
        )
    
# MscParamImage baseclass
@dataclass
class MscParamImage:
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
    def from_dict(obj: Any) -> 'MscParamImage':
        return MscParamImage(
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
    
# MscPlant baseclass
@dataclass
class MscPlant:
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
    def from_dict(obj: Any) -> 'MscPlant':
        return MscPlant(
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

# MscLeaf baseclass
@dataclass
class MscLeaf:
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
    def from_dict(obj: Any) -> 'MscLeaf':
        return MscLeaf(
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

# MscLight baseclass
@dataclass
class MscLight:
    ChannelID: int
    LightSetCaption: str
    LightSetID: int
    LightSetPidName: str
    LightSetValid: bool

    @staticmethod
    def from_dict(obj: Any) -> 'MscLight':
        return MscLight(
            ChannelID=obj.get("ChannelID"),
            LightSetCaption=obj.get("LightSetCaption"),
            LightSetID=obj.get("LightSetID"),
            LightSetPidName=obj.get("LightSetPidName"),
            LightSetValid=obj.get("LightSetValid")
        )

# MscCalibrate baseclass
@dataclass
class MscCalibrate:
    CalibrationDate: str
    CalibrationID: int
    CalibrationImagePath: str
    CameraExposure: int
    CameraGain: int
    LightSetID: int

    @staticmethod
    def from_dict(obj: Any) -> 'MscCalibrate':
        return MscCalibrate(
            CalibrationDate=obj.get("CalibrationDate"),
            CalibrationID=obj.get("CalibrationID"),
            CalibrationImagePath=obj.get("CalibrationImagePath"),
            CameraExposure=obj.get("CameraExposure"),
            CameraGain=obj.get("CameraGain"),
            LightSetID=obj.get("LightSetID")
        )

# MscCaliLight baseclass
@dataclass
class MscCaliLight:
    CalibrationID: int
    CalibrationLightID: int
    CalibrationLightLevel: int
    LightCaption: str
    LightID: int
    LightSetID: int

    @staticmethod
    def from_dict(obj: Any) -> 'MscCaliLight':
        return MscCaliLight(
            CalibrationID=obj.get("CalibrationID"),
            CalibrationLightID=obj.get("CalibrationLightID"),
            CalibrationLightLevel=obj.get("CalibrationLightLevel"),
            LightCaption=obj.get("LightCaption"),
            LightID=obj.get("LightID"),
            LightSetID=obj.get("LightSetID")
        )


# Multispectral Imaging by measurement ID
@dataclass
class MscImagingMeasure:
    MscImage: MscImage

    @staticmethod
    def from_dict(obj: Any) -> 'MscImage':
        if obj.get("JsonMscImagingByIDResult") is None:
            return None
        return [MscImage.from_dict(y) for y in obj.get("JsonMscImagingByIDResult")] 
    
# Multispectral imaging for tray
@dataclass
class MscImaging:
    MscImage: MscImage

    @staticmethod
    def from_dict(obj: Any) -> 'MscImage':
        if obj.get("JsonMscImagingResult") is None:
            return None
        return [MscImage.from_dict(y) for y in obj.get("JsonMscImagingResult")] 
    
# Multispectral extended by measurement ID
class MscImagingExtendedDataMeasure:
    MscExtended: MscExtended

    @staticmethod
    def from_dict(obj: Any) -> 'MscExtended':
        if obj.get("JsonMscMeasureExtendedDataByIDResult") is None:
            return None
        return MscExtended.from_dict(obj.get("JsonMscMeasureExtendedDataByIDResult"))
    
# Multispectral extended for tray
class MscImagingExtendedData:
    MscExtended: MscExtended

    @staticmethod
    def from_dict(obj: Any) -> 'MscExtended':
        if obj.get("JsonMscMeasureExtendedDataResult") is None:
            return None
        return MscExtended.from_dict(obj.get("JsonMscMeasureExtendedDataResult"))
    
# Multispectral mask by measurement ID
class MscPlantMaskMeasure:
    MscMask: MscMask

    @staticmethod
    def from_dict(obj: Any) -> 'MscMask':
        if obj.get("JsonMscPlantMaskByMeasureIDResult") is None:
            return None
        return MscMask.from_dict(obj.get("JsonMscPlantMaskByMeasureIDResult"))

# Multispectral mask for tray
@dataclass
class MscPlantMask:
    MscMask: MscMask

    @staticmethod
    def from_dict(obj: Any) -> 'MscMask':
        if obj.get("JsonMscPlantMaskResult") is None:
            return None
        return [MscMask.from_dict(y) for y in obj.get("JsonMscPlantMaskResult")] 
    
# Multispectral parameter by param ID
class MscParamWrapper:
    MscParam: MscParam

    @staticmethod
    def from_dict(obj: Any) -> 'MscParam':
        if obj.get("JsonMscParamResult") is None:
            return None
        return MscParam.from_dict(obj.get("JsonMscParamResult"))
    
# Multispectral parameter by analysis ID
class MscParamUsedAnalyse:
    MscParam: MscParam

    @staticmethod
    def from_dict(obj: Any) -> 'MscParam':
        if obj.get("JsonMscUsedParamByAnalyseIDResult") is None:
            return None
        return [MscParam.from_dict(y) for y in obj.get("JsonMscUsedParamByAnalyseIDResult")] 

# Multispectral parameter for tray
class MscParamUsed:
    MscParam: MscParam

    @staticmethod
    def from_dict(obj: Any) -> 'MscParam':
        if obj.get("JsonMscUsedParamResult") is None:
            return None
        return [MscParam.from_dict(y) for y in obj.get("JsonMscUsedParamResult")] 
    
# Multispectral parameter image by analysis ID
class MscParamImageAnalyse:
    MscParamImage: MscParamImage

    @staticmethod
    def from_dict(obj: Any) -> 'MscParamImage':
        if obj.get("JsonMscParameterImageByAnalyseIDResult") is None:
            return None
        return MscParamImage.from_dict(obj.get("JsonMscParameterImageByAnalyseIDResult"))

# Multispectral parameter image for tray
class MscParamImageWrapper:
    MscParamImage: MscParamImage

    @staticmethod
    def from_dict(obj: Any) -> 'MscParamImage':
        if obj.get("JsonMscParameterImageResult") is None:
            return None
        return [MscParamImage.from_dict(y) for y in obj.get("JsonMscParameterImageResult")] 
    
# Multispectral plant parameter by analysis ID
class MscPlantParamAnalyse:
    MscPlant: MscPlant

    @staticmethod
    def from_dict(obj: Any) -> 'MscPlant':
        if obj.get("JsonMscPlantParamByAnalyseIDResult") is None:
            return None
        return [MscPlant.from_dict(y) for y in obj.get("JsonMscPlantParamByAnalyseIDResult")] 
    
# Multispectral plant parameter for tray
class MscPlantParam:
    MscPlant: MscPlant

    @staticmethod
    def from_dict(obj: Any) -> 'MscPlant':
        if obj.get("JsonMscPlantParamResult") is None:
            return None
        return [MscPlant.from_dict(y) for y in obj.get("JsonMscPlantParamResult")] 
    
# Multispectral leaf parameter by analysis ID
class MscLeafParamAnalyse:
    MscLeaf: MscLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'MscLeaf':
        if obj.get("JsonMscLeafParamByAnalyseIDResult") is None:
            return None
        return [MscLeaf.from_dict(y) for y in obj.get("JsonMscLeafParamByAnalyseIDResult")]         

# Multispectral leaf parameter for tray
class MscLeafParam:
    MscLeaf: MscLeaf

    @staticmethod
    def from_dict(obj: Any) -> 'MscLeaf':
        if obj.get("JsonMscLeafParamResult") is None:
            return None
        return [MscLeaf.from_dict(y) for y in obj.get("JsonMscLeafParamResult")]     

# Multispectral light by ID
class MscLightSet:
    MscLight: MscLight

    @staticmethod
    def from_dict(obj: Any) -> 'MscLight':
        if obj.get("JsonMscLightSetResult") is None:
            return None
        return MscLight.from_dict(obj.get("JsonMscLightSetResult"))
    
# Multispectral light for tray
class MscLightSetUsed:
    MscLight: MscLight

    @staticmethod
    def from_dict(obj: Any) -> 'MscLight':
        if obj.get("JsonMscLightSetUsedResult") is None:
            return None
        return [MscLight.from_dict(y) for y in obj.get("JsonMscLightSetUsedResult")] 
    
# Multispectral calibration by ID 
class MscCalibration:
    MscCalibrate: MscCalibrate

    @staticmethod
    def from_dict(obj: Any) -> 'MscCalibrate':
        if obj.get("JsonMscCalibrationResult") is None:
            return None
        return MscCalibrate.from_dict(obj.get("JsonMscCalibrationResult"))
    
# Multispectral calibration by lightset ID
class MscCalibrationLightSet:
    MscCalibrate: MscCalibrate

    @staticmethod
    def from_dict(obj: Any) -> 'MscCalibrate':
        if obj.get("JsonMscCalibrationByLightSetIDResult") is None:
            return None
        return [MscCalibrate.from_dict(y) for y in obj.get("JsonMscCalibrationByLightSetIDResult")] 
    
# Multispectral calibration light by ID TODO

    
# List multispectral calibration light settings
class MscCalibrationLight:
    MscCaliLight: MscCaliLight

    @staticmethod
    def from_dict(obj: Any) -> 'MscCaliLight':
        if obj.get("JsonMscCalibrationLightResult") is None:
            return None
        return [MscCaliLight.from_dict(y) for y in obj.get("JsonMscCalibrationLightResult")] 
     