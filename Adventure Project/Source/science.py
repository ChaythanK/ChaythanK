alkali_metals = {
    "Lithium": (3, 7),
    "Sodium": (11, 23),
    "Potassium": (19, 39),
    "Rubidium": (37, 85),
    "Cesium": (55, 133),
    "Francium": (87, 223)
}

# Alkaline Earth Metals
alkaline_earth_metals = {
    "Beryllium": (4, 9),
    "Magnesium": (12, 24),
    "Calcium": (20, 40),
    "Strontium": (38, 88),
    "Barium": (56, 137),
    "Radium": (88, 226)
}

# Transition Metals
transition_metals = {
    "Scandium": (21, 45),
    "Titanium": (22, 48),
    "Vanadium": (23, 51),
    "Chromium": (24, 52),
    "Manganese": (25, 55),
    "Iron": (26, 56),
    "Cobalt": (27, 59),
    "Nickel": (28, 58),
    "Copper": (29, 63),
    "Zinc": (30, 64)
}

# Poor Metals
poor_metals = {
    "Aluminum": (13, 27),
    "Gallium": (31, 69),
    "Indium": (49, 115),
    "Tin": (50, 119),
    "Thallium": (81, 204),
    "Lead": (82, 207),
    "Bismuth": (83, 209)
}

# Metalloids
metalloids = {
    "Boron": (5, 11),
    "Silicon": (14, 28),
    "Germanium": (32, 74),
    "Arsenic": (33, 75),
    "Antimony": (51, 122),
    "Tellurium": (52, 128),
    "Polonium": (84, 209)
}

# Non-Metals (including Hydrogen)
non_metals = {
    "Hydrogen": (1, 1),
    "Carbon": (6, 12),
    "Nitrogen": (7, 14),
    "Oxygen": (8, 16),
    "Phosphorus": (15, 31),
    "Sulfur": (16, 32),
    "Selenium": (34, 79)
}

# Halogens
halogens = {
    "Fluorine": (9, 19),
    "Chlorine": (17, 35),
    "Bromine": (35, 80),
    "Iodine": (53, 127),
    "Astatine": (85, 210)
}

# Noble Gases
noble_gases = {
    "Helium": (2, 4),
    "Neon": (10, 20),
    "Argon": (18, 40),
    "Krypton": (36, 84),
    "Xenon": (54, 131),
    "Radon": (86, 222)
}

# Actinides
actinides = {
    "Thorium": (90, 232),
    "Protactinium": (91, 231),
    "Uranium": (92, 238),
    "Neptunium": (93, 237),
    "Plutonium": (94, 244),
    "Americium": (95, 243),
    "Curium": (96, 247),
    "Berkelium": (97, 247),
    "Californium": (98, 251),
    "Einsteinium": (99, 252),
    "Fermium": (100, 257)
}

# Lanthanides
lanthanides = {
    "Lanthanum": (57, 139),
    "Cerium": (58, 140),
    "Praseodymium": (59, 141),
    "Neodymium": (60, 144),
    "Promethium": (61, 145),
    "Samarium": (62, 150),
    "Europium": (63, 152),
    "Gadolinium": (64, 157),
    "Terbium": (65, 159),
    "Dysprosium": (66, 164),
    "Holmium": (67, 165),
    "Erbium": (68, 167),
    "Thulium": (69, 169),
    "Ytterbium": (70, 173),
    "Lutetium": (71, 175)
}

metals = [
    alkali_metals,
    alkaline_earth_metals,
    transition_metals,
    poor_metals,
    lanthanides
]
# List containing all the dictionaries
element_list = [
    metals,
    metalloids,
    non_metals,
    halogens,
    noble_gases,
    actinides,
]

def valence_electrons(E):
    shell = 0
    E = E.capitalize()
    for category in element_list:
        if E in category:
            for keys, values in category.items():
                if E == keys:
                    print("element qualites:", keys, values)
                    electrons = int(values[0])
                    while electrons > 0:
                        prev = electrons
                        shell += 1
                        electrons -= (2 * (shell ** 2))
                    print('valency:', electrons)
                    print('Valence Electrons:', prev)
                    print('latest shell:', shell)
                    if (-1 * electrons) < prev:
                        print(f'you must add {-1 * electrons} electrons to make the element {E} stable.')
                    elif (-1 * electrons) > prev:
                        print(f'you must take out {prev} electrons to make the element {E} stable.')
        elif category == metals:
            for sub_category in metals:
                if E in sub_category:
                    for keys, values in sub_category.items():
                        if E == keys:
                            print("element qualites:",keys, values)
                            electrons = int(values[0])
                            while electrons > 0:
                                prev = electrons
                                shell += 1
                                electrons -= (2 * (shell ** 2))
                            print('valency:', electrons)
                            print('Valence Electrons:', prev)
                            print('latest shell:',shell)
                            if  (-1*electrons) < prev:
                                print(f'you must add {-1*electrons} electrons to make the element {E} stable.')
                            elif  (-1*electrons) > prev:
                                print(f'you must take out {prev} electrons to make the element {E} stable.')


# Assume metals and non_metals are lists or sets containing the names of elements.

def ionic_bond(element1, element2):
    shell = 0
    can_form_ionic_bond = False
    element1 = element1.capitalize()
    element2 = element2.capitalize()
    for i in metals:
        if element1 in i and element2 in non_metals or element1 in i and element2 in halogens:
            can_form_ionic_bond = True
            host_metal = i
        elif element2 in i and element1 in non_metals or element2 in i and element1 in halogens:
            element1,element2 = element2,element1
            can_form_ionic_bond = True
            host_metal = i
    if can_form_ionic_bond:
        print(f"{element1} is a metal and {element2} is a non-metal. They can form an ionic bond.")
        for each_element,metal_values in host_metal.items():
            if element1 == each_element:
                print(each_element,metal_values)
        if element2 in halogens:
            for halogen,halogen_values in halogens.items():
                if element2 == halogen:
                    print(halogen,halogen_values)
        else:
            for non_metal,non_metals_values in non_metals.items():
                if element2 == non_metal:
                    print(non_metal,non_metals_values)
                    electrons = int(non_metals_values[0])
                    while electrons>0:
                        prev = electrons
                        shell += 1
                        electrons -= (2*(shell**2))
                        print(2*(shell**2))
                    print('valency:',electrons)
                    print('Valence Electrons:',prev)


    else:
        print('sad its not there')




valence_electrons('carbon')

