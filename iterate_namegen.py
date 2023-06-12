#!/usr/bin/env python3

from pathlib import Path


def iterate_namegen():
    source = str(Path("__file__").parent / Path("generators/namegen.py"))
    with open(source) as file:
        namegen = file.readlines()

    insert_index = namegen.index("            # insert point\n")
    number_index = insert_index - 4
    iterated_num = str(int("".join(filter(str.isdigit, namegen[number_index]))) + 1)

    namegen.insert(insert_index, f'        elif x == "{iterated_num}":\n')
    insert_index += 1
    namegen.insert(insert_index, "            intx = int(x)\n")
    insert_index += 1
    namegen.insert(
        insert_index,
        "            rand = random.randrange(0, len(NAMES_DICT[SETS_KEY][intx - 1][x]))\n",
    )
    insert_index += 1
    namegen.insert(
        insert_index,
        "            name += str(list(NAMES_DICT[SETS_KEY][intx - 1].values())[0][rand])\n",
    )

    namegen = "".join(namegen)

    file = open(source, "w")
    file.write(namegen)
    file.close()


if __name__ == "__main__":
    iterate_namegen()
