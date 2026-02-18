from pydantic_xml import BaseXmlModel, attr, element
from typing import List, Optional


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


class Analyse(BaseXmlModel, tag='Analyse'):
    mask_erosion_level: int = element(tag='MaskErosionLevel')


class Prescription(BaseXmlModel, tag='Prescription'):
    id: int = attr()
    name: str = attr()
    ir1: IR1 = element(tag='IR1')
    analyse: Analyse = element(tag='Analyse')


class Batch(BaseXmlModel, tag='Batch'):
    name: str = attr()
    pid: int = attr()
    date: str = attr()


class Tray(BaseXmlModel, tag='Tray'):
    sid: str = attr()
    id: int = attr()
    pid: int = attr()


class Measure(BaseXmlModel, tag='Measure'):
    adapt_time: str = element(tag='AdaptTime')
    prescription: Prescription = element(tag='Prescription')
    batches: Optional[List[Batch]] = element(tag='Batch')
    trays: Optional[List[Tray]] = element(tag='Tray')


class Protocol(BaseXmlModel, tag='Protocol'):
    set_lights: List[SetLight] = element(tag='SetLight')
    tray_load: Optional[TrayLoad] = element(tag='TrayLoad')
    measure: Optional[Measure] = element(tag='Measure')
