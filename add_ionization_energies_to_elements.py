import csv
import json
import build_elements
import Atom


elements = build_elements.build_elements()

element_energies = []

with open("ionization_energies.csv") as ionization_energies:
    reader = csv.reader(ionization_energies)
    # Skip header row
    next(reader, None)
    for black_row in reader:
        grey_row = []
        white_row = []

        for item in black_row:
            if item == "":
                continue
            else:
                grey_row.append(item)


        for x in range(len(grey_row)):
            # Skip element symbol and number
            if x <= 1:
                continue
            else:
                white_row.append(float(grey_row[x]))
        element_energies.append(white_row)


for x in range(len(elements)):
    try:
        copy = elements[x]
        elements[x] = Atom.Atom(copy.name, copy.symbol, copy.atomic_number, copy.atomic_weight, copy.density,
                                copy.molar_volume, copy.valence, copy.electronegativity, copy.electron_affinity,
                                copy.atomic_radius, copy.covalent_radius, copy.van_der_waals_radius, copy.half_life,
                                element_energies[x])
    except IndexError:
        break

print(elements[0].ionization_energy)

with open("Elements_With_Iions.json", "w") as elements_file:
    for element in elements:
        elements_file.write("\n")
        elements_file.write(json.dumps(element.__dict__))
        elements_file.write(",")
        print("Saved", element.name)