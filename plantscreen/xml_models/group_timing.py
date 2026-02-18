from pydantic_xml import BaseXmlModel, attr, element


class GroupTiming(BaseXmlModel, tag='GroupTiming'):
    type: str = attr()
    datetime: str = element(tag='DateTime')
