#!/usr/bin/env python3
"""Dispatch point for the helper scripts."""
from dict_managers import *
from archive.names import names_dict
from pathlib import Path
import os
import shutil
import sys

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
    [5] Restore default dict
    [6] Quit (does not save)"""
        )
        match input():
            case "6":
                sys.exit(0)
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
                    file.write(f"names_dict = {str(names_dict)}")
                    if yapf_installed == True:
                        FormatFile(path, in_place=True)
                print("Save complete!")
            case "5":
                match input("Restore default dict?\n").lower():
                    case "y" | "yes":
                        namespath = Path("__file__").parent / Path("archive/names.py")
                        defaultpath = Path("__file__").parent / Path(
                            "archive/defaultnames.py"
                        )
                        os.replace(defaultpath, namespath)
                        shutil.copyfile(namespath, defaultpath)
                        print("Restored!")
                        sys.exit(0)
                    case "n" | "no":
                        print("Okay!")
                        continue
            case _:
                print("Please select a valid menu option.")


if __name__ == "__main__":
    namegen_helper()
