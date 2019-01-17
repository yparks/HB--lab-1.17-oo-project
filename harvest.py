############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', True, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

list_of_melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melonType in melon_types:
        print("{} pairs with ".format(melonType.name))
        for pairing in melonType.pairings:
            print("- {}".format(pairing))
            print("\n")

# print_pairing_info(list_of_melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}

    for melonType in melon_types:
        melon_dict[melonType.code] = melonType
        # print("{}: {}".format(melonType.code, melonType.pairings))

    return melon_dict

# print(make_melon_type_lookup(list_of_melon_types))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, worker):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.worker = worker

    def is_sellable(self, shape_rating, color_rating, field):
        if self.field == 3:
            return False
        if self.color_rating > 5 and self.shape_rating > 5:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)
    # print(melon_types)
    all_melon_harvest = []
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Micheal')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Micheal')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Micheal')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Micheal')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    all_melon_harvest.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])
    
    return all_melon_harvest

    
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.is_sellable():
            print("Harvested by {} from Field {} (CAN BE SOLD)".format(melon.worker, melon.field))
        else: 
            print("Harvested by {} from Field {} (NOT SELLABLE)".format(melon.worker, melon.field))

# list_harvestmelons = make_melons(make_melon_type_lookup(list_of_melon_types))