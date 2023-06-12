#!/usr/bin/env python3
from archive.names import names_dict


"""View, manaage, and edit name sets."""


def set_manager():
    """set_manager"""
    while True:
        match input(
            """Welcome to the set manager! What would you like to do?
    [1] View current sets.
    [2] Create new set.
    [3] Add to existing set.
    [4] Remove from existing set.
    [5] Delete set.
    [6] Back to manager.
"""
        ):
            case "6":
                break
            case "1":
                for x in names_dict["sets"]:
                    print(str(names_dict["sets"].index(x) + 1) + f". {x}")
            case "2":
                next_key = str(len(names_dict["sets"]) + 1)
                while True:
                    set_items = input(
                        f"Please type the items you'd like to add to new set {next_key}, separated by commas:\n"
                    ).split(",")
                    set_items = list(filter(None, [x.strip() for x in set_items]))
                    if set_items == []:
                        print("Please enter items for the set!")
                        continue
                    break
                names_dict["sets"].append(set_items)
                print(f"Set {next_key} added, with the items {set_items}.")
            case "3":
                add_key = input("Add items to which set?\n")
                while True:
                    add_items = input(
                        f"Please type the items you'd like to add to set {add_key}, separated by commas:\n"
                    ).split(",")
                    add_items = list(filter(None, [x.strip() for x in add_items]))
                    if add_items == []:
                        print("Please enter items to add!")
                        continue
                    break
                names_dict["sets"][int(add_key) - 1].extend(add_items)
                print(f"{add_items} added to set {add_key}.")
            case "4":
                removal_key = int(input("Remove items from which set?\n")) - 1
                removal_set = names_dict["sets"][removal_key]
                while True:
                    print(removal_set)
                    remove_item = input("Remove which item? Or, type done to finish.\n")
                    match remove_item:
                        case "done" | "Done":
                            break
                        case _:
                            try:
                                removal_set.remove(remove_item)
                            except ValueError:
                                print("Set item not found!")
                            continue
            case "5":
                delete_key = int(input("Delete which set?\n")) - 1
                del names_dict["sets"][delete_key]
            case _:
                print("Please enter a valid option!")


def structure_manager():
    """Structure managers"""
    while True:
        match input(
            """Welcome to the structure manager! What would you like to do?
    [1] View current structures.
    [2] Create new structure.
    [3] Modify existing structure.
    [4] Delete structure.
    [5] Back to manager.
"""
        ):
            case "5":
                break
            case "1":
                for x in names_dict["structures"]:
                    print(str(names_dict["structures"].index(x) + 1) + f". {x}")
            case "2":
                next_key = str(len(names_dict["sets"]) + 1)
                while True:
                    new_struct = input(
                        f"Please type the format of structure {next_key}, with each item separated by a space (see the readme for instructions:\n)"
                    ).split()
                    new_struct = list(filter(None, [x.strip() for x in new_struct]))
                    if new_struct == []:
                        print("Please enter a structure!")
                        continue
                    break
                names_dict["sets"].append(new_struct)
                print(f"Structure {next_key} added with the structure {new_struct}.")
            case "3":
                edit_struct = (
                    int(input("Which structure would you like to edit?\n")) - 1
                )
                while True:
                    new_struct = input(
                        f'The current structure is {names_dict["structures"][edit_struct]}.\nPlease type the new structure, with each item separated by a space.\n'
                    ).split()
                    new_struct = list(filter(None, [x.strip() for x in new_struct]))
                    if new_struct == []:
                        print("Please enter a structure!")
                        continue
                    break
                names_dict["structures"][edit_struct] = new_struct
            case "4":
                delete_key = int(input("Delete which structure?\n")) - 1
                del names_dict["structures"][delete_key]
