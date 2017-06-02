import json
import Atom
import Isotope
import re
import simple_api_wrapper
import os

query = simple_api_wrapper.query_wolfram

elements = []

def strip_non_numbers(string):
    return re.sub(r'[^\d\.]', "", string)


def convert_to_years(string):
    number = float(strip_non_numbers(string))
    conversion_table = {"billion": 1_000_000, "million": 1_000_000, "thousand": 1_000,
                        'days': 0.0027397260273972603, 'hours':  0.00011415525114155251,
                        'minutes': 1.9025875190258753e-06, 'seconds': 3.1709791983764586e-08,
                        "ms": 3.170979198376459e-11}

    for key in conversion_table.keys():
        if key in string:
            number *= conversion_table[key]
    return number

for x in range(110, 119):
    x = str(x)
    name = query("element " + x)

    # Catch invalid appid right away
    if name == 'Error 1: Invalid appid':
        print("Invalid appid")
        break
    name = name.title()
    print("Downloading", name)
    print("0%")
    print(str(100//13) + "%")
    symbol = query("symbol of element" + x)
    print(str(200 // 13) + "%")
    atomic_number = int(x)
    print(str(300 // 13) + "%")
    atomic_weight = query("atomic weight of element " + x)
    print(str(400 // 13) + "%")
    density = query("density of element " + x)
    print(str(500 // 13) + "%")
    molar_volume = query("molar volume of element " + x)
    print(str(600 // 13) + "%")
    valence = query("valence of element " + x)
    print(str(700 // 13) + "%")
    electronegativity = query("electronegativity of element " + x)
    print(str(800 // 13) + "%")
    electron_affinity = query("electron affinity of element " + x)
    print(str(900 // 13) + "%")
    atomic_radius = query("atomic radius of element " + x)
    print(str(1000 // 13) + "%")
    covalent_radius = query("covalent radius of element " + x)
    print(str(1100 // 13) + "%")
    van_der_waals_radius = query("van der waals radius of element " + x)
    print(str(1200 // 13) + "%")
    half_life = query("half life of element " + x)
    print(str(1300 // 13) + "%")

    #Processing values

    name = name.title()
    atomic_weight = float(strip_non_numbers(atomic_weight))
    if density == "No short answer available":
        density = -1
    else:
        density = float(re.sub('×\d{1,}\^', 'e', re.sub('[^0-9×^\-\.]', "", density)))
    if molar_volume == "No short answer available":
        molar_volume = -1
    else:
        molar_volume = float(strip_non_numbers(molar_volume))
    if valence == "No short answer available":
        valence = -1
    else:
        valence = int(valence)
    if electronegativity == "No short answer available":
        electronegativity = -1
    if electron_affinity == "No short answer available":
        electron_affinity = -1
    else:
        electron_affinity = float(strip_non_numbers(electron_affinity))
    if atomic_radius == "No short answer available":
        atomic_radius = -1
    else:
        atomic_radius = int(strip_non_numbers(atomic_radius))
    if covalent_radius == "No short answer available":
        covalent_radius = -1
    else:
        covalent_radius = int(strip_non_numbers(covalent_radius))
    if van_der_waals_radius == "No short answer available":
        van_der_waals_radius = -1
    else:
        van_der_waals_radius = int(strip_non_numbers(van_der_waals_radius))
    if half_life == "{}":
        half_life = -1
    else:
        half_life = float(convert_to_years(half_life))

    elements.append(Atom.Atom(name, symbol, atomic_number, atomic_weight, density, molar_volume, valence,
                              electronegativity, electron_affinity, atomic_radius, covalent_radius,
                              van_der_waals_radius, half_life))
    print("Downloaded", elements[-1].name)
    with open('Elements.json', 'a') as file:
        # TODO manually place closing bracket
        file.write("\n")
        file.write(json.dumps(elements[-1].__dict__))
        file.write(",")
        print("Saved", elements[-1].name)