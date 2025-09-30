#!/usr/bin/python3

"""
Serialization and deserialization using
XML as an alternative format to JSON.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Take a Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML
    and save it to the given filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error writing XML: {e}")


def deserialize_from_xml(filename):
    """
    Take a filename as its parameter,
    read the XML data from that file,
    and return a deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text

        return data

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return {}

    except Exception as e:
        print(f"Error reading XML: {e}")
        return {}
