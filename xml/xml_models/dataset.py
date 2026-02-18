from typing import List
from pydantic_xml import BaseXmlModel, attr, element


class Item(BaseXmlModel, tag='Item'):
    name: str = attr()
    type: str = attr()
    unit: str = attr()
    value: float = None  # Text content

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'value' not in kwargs and '_text' in kwargs:
            self.value = float(kwargs['_text'])


class DataSet(BaseXmlModel, tag='DataSet'):
    items: List[Item] = element(tag='Item')
