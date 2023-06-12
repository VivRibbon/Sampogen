#!/usr/bin/env python3
import random
from archive.test import *
import sys

NAMES_DICT = names_dict
STRUCT_KEY = "structures"
SETS_KEY = "sets"


def namegen():
    """Generates a name"""
    name = ""

    rand = random.randrange(0, len(NAMES_DICT[STRUCT_KEY]))
    picked_struct = NAMES_DICT[STRUCT_KEY][rand]

    for x in picked_struct:
        if x.isdigit() == True:
            rand = random.randrange(0, len(NAMES_DICT[SETS_KEY]))
            picked_set = NAMES_DICT[SETS_KEY][rand]
            rand = random.randrange(0, len(picked_set))
            name += picked_set[rand]
        else:
            name += x

    return name


def name_collector(count):
    """Assemble $count-long lists of first names and surnames"""
    first_names = []
    surnames = []

    while len(first_names) < count:
        name = namegen().capitalize()
        if name not in first_names:
            first_names.append(name)
            sys.stdout.write(str(len(first_names)) + " first names generated.\r")
    print("\n")
    while len(surnames) < count:
        name = namegen().capitalize()
        if name not in first_names and name not in surnames:
            surnames.append(name)
            sys.stdout.write(str(len(surnames)) + " surnames generated.\r")

    print("\n")
    return (first_names, surnames)


def name_stitcher(first_names, surnames, count):
    """Creates $count number of full names from the lists provided by name_collector()"""
    names = []
    i = 1

    while i <= count:
        rand_first = random.randrange(1, len(first_names))
        rand_sur = random.randrange(1, len(surnames))
        name = [first_names[rand_first], surnames[rand_sur]]
        names.append(" ".join(name))
        name = []
        i += 1
        sys.stdout.write("\r" + str(len(names)) + " names stitched.")

    print("\n")
    return names
