# Play with Curses

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>
This project implements the Python Curses library (Which is an implementation of C++'s ncurses library). 

Play with Curses adds a layer of abstraction above the Python Curses library, allowing the programmer to build GUI terminal menus that execute Python code faster.

## Getting Started <a name = "getting_started"></a>
1. Clone the repo.
2. Populate the functions you want the menu items to execute within the [fucntion_map](https://github.com/camratchford/play_with_curses/blob/master/interface/interface.py#L20-L23)
2. Build your menu by editing the contents of [config.py](https://github.com/camratchford/play_with_curses/blob/master/config.py#L3-L74), mapping your function to menu item.
4. Execute main.py

### Prerequisites
- python3.7 binaries (curses should be part of the standard library)

