from typing import List
from pydantic_xml import BaseXmlModel, element


class Item(BaseXmlModel, tag='Item'):
    z: int = element(tag='Z')
    x_shift: int = element(tag='XShift')
    y_shift: int = element(tag='YShift')


class CenterShift(BaseXmlModel, tag='CenterShift'):
    items: List[Item] = element(tag='Item')


class Configuration(BaseXmlModel, tag='Configuration'):
    windowing_mode: int = element(tag='WindowingMode')
    extract_lines: int = element(tag='ExtractLines')
    focus: int = element(tag='Focus')
    width: int = element(tag='Width')
    height: int = element(tag='Height')
    default_z: int = element(tag='DefaultZ')
    mask_center_x: int = element(tag='MaskCenterX')
    mask_center_y: int = element(tag='MaskCenterY')
    barrel: float = element(tag='Barrel')
    mask_rotation: float = element(tag='MaskRotation')
    z_conversion: int = element(tag='ZConversion')
    ratio_coefficient: float = element(tag='RatioCoefficient')
    backward_fec: bool = element(tag='BackwardFEC')
    fixed_x: bool = element(tag='FixedX')
    fixed_x_px_mm_ratio: float = element(tag='FixedXPxMmRatio')
    fixed_y: bool = element(tag='FixedY')
    fixed_y_px_mm_ratio: float = element(tag='FixedYPxMmRatio')
    center_shift: CenterShift = element(tag='CenterShift')
    scan_lines: int = element(tag='ScanLines')
    position_start: int = element(tag='PositionStart')
    position_end: int = element(tag='PositionEnd')
    scan_speed: int = element(tag='ScanSpeed')
    move_speed: int = element(tag='MoveSpeed')
    scan_axis: str = element(tag='ScanAxis')
    heating_temp_diff: float = element(tag='HeatingTempDiff')
    heating_time: int = element(tag='HeatingTime')
