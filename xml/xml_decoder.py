from typing import List, Type
from pydantic_xml import BaseXmlModel
import xml.etree.ElementTree as ET
from copy import copy


from plantscreen.xml_models.dataset import DataSet
from plantscreen.xml_models.configuration import Configuration
from plantscreen.xml_models.group_timing import GroupTiming
from plantscreen.xml_models.protocol import Protocol
from plantscreen.xml_models.system_config import (
    Configuration as SystemConfiguration,
)
from plantscreen.xml_models.tray_type import TAnyShapes


def parse_xml(xml: str) -> BaseXmlModel:
    """
    Parse XML string into the appropriate BaseXmlModel subclass based on
    the root tag.
    Args:
        xml (str): The XML string to parse.
    Returns:
        BaseXmlModel: An instance of the appropriate BaseXmlModel subclass.
    """
    xml_models = {
        'Protocol': [Protocol],
        'Configuration': [Configuration, SystemConfiguration],
        'GroupTiming': [GroupTiming],
        'DataSet': [DataSet],
        'TAnyShapes': [TAnyShapes]
    }
    root_tag = ET.fromstring(xml).tag
    model_classes: List[Type[BaseXmlModel]] = xml_models.get(root_tag, [])
    if not model_classes:
        raise ValueError(f"No model found for root tag '{root_tag}'")
    last_exc = None
    for model_cls in model_classes:
        try:
            return model_cls.from_xml(xml)
        except Exception as exc:
            last_exc = exc
            continue
    raise ValueError(
        f"No model could parse XML for root tag '{root_tag}'. "
        f"Last error: {last_exc}"
    )


def _dictify(xml_tree, root=True):
    """"
    Help function to convert an XML object to a dictionary,
    called recursively to convert the entire tree

    Args:
            xml_tree  (xml ElementTree): xml element tree
            root (bool): prossing root node of child node
        Return:
            dictionary """
    if root:
        return {xml_tree.tag: _dictify(xml_tree, False)}
    dictionary = copy(xml_tree.attrib)
    if xml_tree.text and xml_tree.text.strip() != "":
        dictionary["_text"] = xml_tree.text
    for x in xml_tree.findall("./*"):
        if x.tag not in dictionary:
            dictionary[x.tag] = []
        dictionary[x.tag].append(_dictify(x, False))
    return dictionary


def xml_to_dict(protocol_xml: str) -> dict:
    """"
    Convert a XML to a dictionary, backup if the dataclass does not work

    Args:
            protocol_xml (str): xml string

        Return:
            dictionary """
    tree = ET.fromstring(protocol_xml)
    xmldict = _dictify(tree)
    return xmldict
