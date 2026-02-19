from pydantic_xml import BaseXmlModel, attr, element
from typing import List, Optional


class Frame(BaseXmlModel, tag='Frame'):
    angle: Optional[int] = attr(default=None)


class Light(BaseXmlModel, tag='Light'):
    name: str = attr()
    value: int = attr()


class SetLight(BaseXmlModel, tag='SetLight'):
    lights: List[Light] = element(tag='Light')


class TrayLoad(BaseXmlModel, tag='TrayLoad'):
    row: int = attr(name='row')
    count: int = attr()


class ProtocolInner(BaseXmlModel, tag='Protocol'):
    name: Optional[str] = attr(default=None)
    value: Optional[str] = None  # Text content

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Assign text content if present
        if 'value' not in kwargs and '_text' in kwargs:
            self.value = kwargs['_text']


class Offset(BaseXmlModel, tag='Offset'):
    value: int = element(tag='Offset')


class Delay(BaseXmlModel, tag='Delay'):
    value: str = element(tag='Delay')


class IR1(BaseXmlModel, tag='IR1'):
    height: str = attr()
    offset: int = element(tag='Offset')
    protocol: ProtocolInner = element(tag='Protocol')
    delay: str = element(tag='Delay')


class PlantMask(BaseXmlModel, tag='PlantMask'):
    formula: Optional[str] = element(tag='Formula', default=None)
    threshold: Optional[float] = element(tag='Threshold', default=None)
    median_filter_size: Optional[int] = element(
        tag='MedianFilterSize', default=None
    )
    min_size: Optional[int] = element(tag='MinSize', default=None)
    min_hole_size: Optional[int] = element(tag='MinHoleSize', default=None)
    crop_objects_on_borders: Optional[bool] = element(
        tag='CropObjectsOnBorders', default=None
    )
    crop_objects_on_borders_min_preserve_size: Optional[int] = element(
        tag='CropObjectsOnBordersMinPreserveSize', default=None
    )
    use_reflection_reduction: Optional[bool] = element(
        tag='UseReflectionReduction', default=None
    )
    skip_bad_exposed_points: Optional[bool] = element(
        tag='SkipBadExposedPoints', default=None
    )


class RGBS(BaseXmlModel, tag='RGBS'):
    height: Optional[str] = attr(default=None)
    offset: Optional[int] = element(tag='Offset', default=None)
    frame: Optional['Frame'] = element(tag='Frame', default=None)
    delay: Optional[str] = element(tag='Delay', default=None)
    plant_mask: Optional[PlantMask] = element(tag='PlantMask', default=None)


class Rgb(BaseXmlModel, tag='Rgb'):
    red: Optional[int] = element(tag='Red', default=None)
    green: Optional[int] = element(tag='Green', default=None)
    blue: Optional[int] = element(tag='Blue', default=None)
    brighten_multiplier: Optional[int] = element(
        tag='BrightenMultiplier', default=None
    )


class Parameters(BaseXmlModel, tag='Parameters'):
    parameter: Optional[str] = element(tag='Parameter', default=None)


class Values(BaseXmlModel, tag='Values'):
    wl_surrounding: Optional[int] = element(tag='WlSurrounding', default=None)
    min_valid_pixels_percentage: Optional[int] = element(
        tag='MinValidPixelsPercentage', default=None
    )


class SWIR(BaseXmlModel, tag='SWIR'):
    height: Optional[str] = attr(default=None)
    offset: Optional[int] = element(tag='Offset', default=None)
    delay: Optional[str] = element(tag='Delay', default=None)
    rgb: Optional[Rgb] = element(tag='Rgb', default=None)
    parameters: Optional[Parameters] = element(tag='Parameters', default=None)
    values: Optional[Values] = element(tag='Values', default=None)


class Analyse(BaseXmlModel, tag='Analyse'):
    mask_erosion_level: Optional[int] = element(
        tag='MaskErosionLevel', default=None
    )
    rgbs: Optional['RGBS'] = element(tag='RGBS', default=None)
    swir: Optional['SWIR'] = element(tag='SWIR', default=None)


class Prescription(BaseXmlModel, tag='Prescription'):
    id: Optional[int] = attr(default=None)
    name: Optional[str] = attr(default=None)
    ir1: Optional[IR1] = element(tag='IR1', default=None)
    rgbs: Optional[RGBS] = element(tag='RGBS', default=None)
    swir: Optional[SWIR] = element(tag='SWIR', default=None)
    analyse: Optional[Analyse] = element(tag='Analyse', default=None)


class Batch(BaseXmlModel, tag='Batch'):
    name: str = attr()
    pid: int = attr()
    date: str = attr()


class Tray(BaseXmlModel, tag='Tray'):
    sid: str = attr()
    id: int = attr()
    pid: int = attr()


class Measure(BaseXmlModel, tag='Measure'):
    adapt_time: Optional[str] = element(tag='AdaptTime', default=None)
    prescription: Optional[Prescription] = element(
        tag='Prescription', default=None
    )
    batches: Optional[List[Batch]] = element(tag='Batch')
    trays: Optional[List[Tray]] = element(tag='Tray')


class Protocol(BaseXmlModel, tag='Protocol'):
    set_lights: Optional[List[SetLight]] = element(
        tag='SetLight', default=None
    )
    tray_load: Optional[TrayLoad] = element(tag='TrayLoad', default=None)
    measure: Optional[Measure] = element(tag='Measure')
