# Sampogen
Roguelike-style procedural name generator with easy customization interface by Moira Oona Campbell

## What's this?
Sampogen is a simple program for generating names a la a roguelike, working from defined structures and sets of phonemes, allowing simple definition of phonotactics. It originated from a roguelike project I'm conceptualizing, itself inspired by my reading of the Kalevala, hence the name.

It is also quite modular and should be fairly easy to slot into a larger system for use in games and such.

## Installation

Ensure you have Python installed and then just clone the repository:
``` sh
git clone https://github.com/VivRibbon/Sampogen
```
You can also download a zip or tarball of the code from the releases. It should work on any system with Python installed but is currently only tested in Linux, so let me know if there are any issues.

Optionally, install yapf, which will automatically format the source dictionary to be more human-readable after you make changes to it:

``` sh
pip install yapf
```

## Usage

Move into the cloned directory and either run the sampogen file with Python or make it executable and then run it:
``` sh
python sampogen
or:
chmod +x sampogen
./sampogen
```

With no arguments, it will generate 100 first and surnames and then make 10 full names from those lists. Pass the -r and -n arguments to set the amount of names in the originating lists and the names delivered respectively. Pass -m to run the manager which allows you to edit the source structures and sets. Pass -h to see help for the script and review these options.

``` sh
./sampogen -r 1000 -n 100
./sampogen -m
./sampogen -h
```

### The Namegen Manager
The namegen manager is a command line tool to easily customize the source that sampogen uses to generate names. In order to use it I need to briefly explain how things are structured.

The source that the program uses to generate things is a Python dictionary consisting of two parts, "sets" and "structures".

A **set** is a set of letters that represent the building blocks from which names are made (often, though certainly not necessarily, a single phoneme). Although the examples only use letters, this can be any unicode character so feel free to get wacky with it.

A **structure** takes the form of a series of numbers separated by spaces and defines the structure of a name by determining what set a given section of the name will be taken from, in what order. For instance, the structure "1 2 3" means the program will randomly take an item from set one, set two, and set three, and put them together in that order. Only numbers are read as structure instructions, while all other characters are left in the resulting name unchanged. This allows you to do things like have a name that always has a hyphen or certain letters in the same place (such as "2 - 3 4" and "1 5 Ha 3").

At run time, the namegen function randomly chooses a structure and then follows that structure's instructions to randomly choose items from the correct sets and return a name. It does this as many times as the amount of raw names you ask for, then does it a second time to generate a list of surnames. These two lists are unique, the same name can not appear on both. Then a name is randomly chosen from each list and combined to form a full name. It does this as many times as asked to by the names argument.

(Note also that the first name and surname lists are directly returned by the function that defines them, which means they could be used for other purposes within a larger program, such as generating a large list of names during world generation to pull from later.)

The functioning of the manager itself should be fairly self-explanatory, but it's worth noting that your changes will not be saved unless you choose the save option from the manager's main menu. Quitting without saving will result in your changes being lost. If anything ever gets really messed up, use the "restore default dict" menu option to restore the original state of the generator.

## License
MIT license. Attribution appreciated but not legally required. Have fun.
