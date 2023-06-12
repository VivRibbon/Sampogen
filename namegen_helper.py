#!/usr/bin/env python3
"""Dispatch point for the helper scripts."""
from dict_managers import *
import archive.names
from archive.names import names_dict
import importlib
from pathlib import Path

# Checks if the user has YAPF installed. If so, it will be used to format the save dict.
try:
    from yapf.yapflib.yapf_api import FormatFile
except ImportError:
    yapf_installed = False
else:
    yapf_installed = True


def namegen_helper():
    """Main function."""
    while True:
        print(
            """What script would you like to run?
    [1] View full dict
    [2] Set Manager
    [3] Structure Manager
    [4] Save all changes
    [5] Quit (Does Not Save)"""
        )
        match input():
            case "5":
                exit(0)
            case "1":
                print("Structures:")
                for x in names_dict["structures"]:
                    print(x)
                print("+----------+\nSets:")
                for x in names_dict["sets"]:
                    print(str(names_dict["sets"].index(x) + 1) + f". {x}")
            case "2":
                set_manager()
            case "3":
                structure_manager()
            case "4":
                path = Path("__file__").parent / Path("archive/names.py")
                with open(path, mode="w") as file:
                    file.write("names_dict = " + str(names_dict))
                if yapf_installed == True:
                    FormatFile(path, in_place=True)
                print("Save complete!")
            case _:
                print("Please select a valid menu option.")


if __name__ == "__main__":
    namegen_helper()
