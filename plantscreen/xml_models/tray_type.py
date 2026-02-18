from typing import List, Optional
from pydantic_xml import BaseXmlModel, attr, element


class TRectangleShape(BaseXmlModel, tag='TRectangleShape'):
    name: str = attr()
    left: int = attr()
    top: int = attr()
    right: int = attr()
    bottom: int = attr()


class TMultiShapes(BaseXmlModel, tag='TMultiShapes'):
    rectangles: Optional[List[TRectangleShape]] = element(tag='TRectangleShape')


class TLineShapes(BaseXmlModel, tag='TLineShapes'):
    # Add fields if TLineShapes has children in your real XML
    pass


class TAnyShapes(BaseXmlModel, tag='TAnyShapes'):
    width: float = attr()
    height: float = attr()
    xratio: float = attr()
    yratio: float = attr()
    ps: float = attr()
    psx: float = attr()
    psy: float = attr()
    t_line_shapes: Optional[TLineShapes] = element(tag='TLineShapes')
    t_multi_shapes: Optional[TMultiShapes] = element(tag='TMultiShapes')
