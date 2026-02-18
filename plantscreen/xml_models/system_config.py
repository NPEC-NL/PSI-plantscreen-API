from typing import List, Optional
from pydantic_xml import BaseXmlModel, attr, element


class TrayStack(BaseXmlModel, tag='TrayStack'):
    row_count: int = element(tag='RowCount')
    row_capacity: int = element(tag='RowCapacity')


class Commands(BaseXmlModel, tag='Commands'):
    set_light: bool = element(tag='SetLight')
    tray_load: bool = element(tag='TrayLoad')
    tray_swap: bool = element(tag='TraySwap')
    tray_unload: bool = element(tag='TrayUnload')
    measure: bool = element(tag='Measure')


class Light(BaseXmlModel, tag='Light'):
    caption: Optional[str] = attr(default=None)
    value: Optional[str] = None  # Text content

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'value' not in kwargs and '_text' in kwargs:
            self.value = kwargs['_text']


class Lights(BaseXmlModel, tag='Lights'):
    lights: List[Light] = element(tag='Light')


class AxisZ(BaseXmlModel, tag='AxisZ'):
    height_visible: Optional[bool] = attr(name='heightVisible', default=None)
    value: Optional[bool] = None  # Text content

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Accept text content as value
        if 'value' not in kwargs and '_text' in kwargs:
            # Accept 'true'/'false' as bool
            text = kwargs['_text'].strip().lower()
            if text == 'true':
                self.value = True
            elif text == 'false':
                self.value = False
            else:
                self.value = None


class PID(BaseXmlModel, tag='PID'):
    name: str = attr()
    caption: str = attr()
    view: str = element(tag='View')
    turntable: bool = element(tag='Turntable')
    axis_z: AxisZ = element(tag='AxisZ')


class Pids(BaseXmlModel, tag='Pids'):
    pids: List[PID] = element(tag='PID')


class Analyse(BaseXmlModel, tag='Analyse'):
    pass


class Configuration(BaseXmlModel, tag='Configuration'):
    tray_stack: TrayStack = element(tag='TrayStack')
    adapt_chamber: bool = element(tag='AdaptChamber')
    height_measurement: bool = element(tag='HeightMeasurement')
    commands: Commands = element(tag='Commands')
    lights: Lights = element(tag='Lights')
    pids: Pids = element(tag='Pids')
    analyse: Optional[Analyse] = element(tag='Analyse')
