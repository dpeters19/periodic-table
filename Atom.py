class Atom:
    def __init__(self, name, symbol, atomic_number, atomic_weight, density, molar_volume, valence, electronegativity,
                 electron_affinity, atomic_radius, covalent_radius, van_der_waals_radius, half_life, ionization_energy=[]):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
        self.density = density
        self.molar_volume = molar_volume
        self.valence = valence
        self.electronegativity = electronegativity
        self.electron_affinity = electron_affinity
        self.atomic_radius = atomic_radius
        self.covalent_radius = covalent_radius
        self.van_der_waals_radius = van_der_waals_radius
        self.half_life = half_life
        # self.known_isotopes = []
        # self.stable_isotopes = []
        self.ionization_energy = ionization_energy
