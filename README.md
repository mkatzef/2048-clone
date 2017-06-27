# 2048-clone

A clone of the game [2048](https://gabrielecirulli.github.io/2048/), written in Python3. Supported on Windows, MacOS, and GNU/Linux. 

## Getting Started

This project consists of only the following two modules.
* `twenty48.py` - The internal structure of the 2048 game.
* `twenty48gui.py` - A GUI to interact with an instance of the `twenty48` structure.

These files must be present in the same directory to run.

### Prerequisites

To run 2048-clone, the host machine must have the following installed:
* `Python3` - The programming language in which 2048-clone was written. Available [here](https://www.python.org/).
* `Tkinter` - The Python library required for the 2048-clone user interface.\*

\*Included with the standard Python3 installation on Windows and MacOS, requires separate installation on Linux. For Debian-based systems, this is achieved through the following command:
`apt-get install python3-tk`

### Running

The game may be started by running the script `twenty48gui.py` as follows:
`python3 twenty48gui.py` 

This will open the game window, with a new game started.


### Game Play
The tiles of the game board may be moved using the arrow keys on a keyboard. Each movement combines adjacent tiles of the same value to generate one of greater value. As with the original game, the goal is to get the highest single tile value.

The game may be restarted at any time using the "New Game" button at the bottom of the GUI. Before restarting, the next board's "Size" and "Base" may be selected.

"Size" refers to the width and height of the (Size * Size) game board. "Base" refers to the smallest starting tile value, and multiplier for every combination. By default, the starting grid size is 4, and base is 2.

## Authors

* **Marc Katzef** - [mkatzef](https://github.com/mkatzef)
