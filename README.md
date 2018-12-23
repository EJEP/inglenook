# Inglenook puzzle generator #

A python script to generate start and end arrangements for the [inglenook shunting puzzle](http://www.wymann.info/ShuntingPuzzles/sw-inglenook.html). Arrangements of wagons can be generated for 3-2-2 or 5-3-3 puzzles.

## Usage ##

Currently the code is command-line only. The program is run as: `python inglenook.py 322` or `python inglenook.py 533` followed by a list of the wagons to be arranged.

For example:

```
$ python inglenook.py 533 HAA ZKV IEA MLA YMO clam rudd HTA
The target order is: ['ZKV', 'HAA', 'MLA', 'HTA', 'rudd']

The starting setup is:
Long siding:         ['rudd', 'HTA', 'ZKV', 'YMO', 'IEA']
First short siding:  ['clam', 'MLA']
Second short siding: ['HAA']
```
