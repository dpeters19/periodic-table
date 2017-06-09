import json

import Atom


def build_elements():
    """
    Builds a list of elements from a JSON file
    Args:

    Returns:
        list(Atom.Atom)
    """
    json_elements = []
    object_elements = []

    with open("Elements.json", "r") as element_data:
        datums = json.load(element_data)
        for item in datums:
            json_elements.append(item)

    for item in json_elements:
        object_elements.append(Atom.Atom(item['name'], item['symbol'], item['atomic_number'], item['atomic_weight'],
                                         item['density'], item['molar_volume'], item['valence'],
                                         item['electronegativity'], item['electron_affinity'], item['atomic_radius'],
                                         item['covalent_radius'], item['van_der_waals_radius'], item['half_life'], 
                                         item['ionization_energy']))

    return object_elements
