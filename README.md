# Inglenook puzzle generator #

A python script to generate start and end arrangements for the [inglenook shunting puzzle](http://www.wymann.info/ShuntingPuzzles/sw-inglenook.html). Arrangements of wagons can be generated for 3-2-2 or 5-3-3 puzzles.

## Usage ##

Currently the code is command-line only. The program is run as: `python inglenook2.py 322` or `python inglenook2.py 533` followed by a list of the wagons to be arranged.

For example:

```python inglenook2.py 533 HAA ZKV IEA MLA YMO clam rudd HTA```
