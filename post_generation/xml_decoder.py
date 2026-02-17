"""Decoder for the xml returns"""
from io import BytesIO
import xml.etree.ElementTree as ET
from copy import copy


def dictify(xml_tree, root=True):
    """"
    Help function to convert an XML object to a dictionary, called recursively to convert the entire tree

    Args:
        xml_tree  (xml ElementTree): xml element tree
        root (bool): processing root node of child node
    Return:
        dictionary
    """
    if root:
        return {xml_tree.tag: dictify(xml_tree, False)}
    dictionary = copy(xml_tree.attrib)
    if xml_tree.text and xml_tree.text.strip() != "":
        dictionary["_text"] = xml_tree.text
    for x in xml_tree.findall("./*"):
        if x.tag not in dictionary:
            dictionary[x.tag] = []
        dictionary[x.tag].append(dictify(x, False))
    return dictionary


def protocolxml_to_dict(protocol_xml: str) -> dict:
    """"
    Convert a protocol XML to a dictionary, no dataclass as there is to much variation

    Args:
        protocol_xml (str): xml string
    Return:
        dictionary """
    tree = ET.fromstring(protocol_xml)
    xmldict = dictify(tree)
    measure_dict = xmldict['Protocol']['Measure'][0]
    return measure_dict
