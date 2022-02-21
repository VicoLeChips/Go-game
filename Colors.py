"""
Colors
@author: Nexmat
last update: 21-02-2016
"""

import sys;

def cprint(*args, fg = '', bg = '', sep = ' ', end = '\n', file = sys.stdout, flush = False):
    """Wrapper pour la fonction print, permet de manipuler les couleurs"""
    string = sep.join(args);

    colors = {"invisible": "0",
            "red": "1",
            "blue": "4",
            "black": "16",
            "white": "255",
            "brown": "130",
            "orange": "137",
            "": ""}

    bg = colors[bg]
    fg = colors[fg]

    if fg == "":
        if bg == "":
            print(string);
        else:
            print('\033[48;5;' + bg + 'm' + string + '\033[0m', sep = sep, end = end, file = file, flush = flush);
    else:
        if bg == "":
            print('\033[38;5;' + fg + 'm' + string + '\033[0m', sep = sep, end = end, file = file, flush = flush);
        else:
            print('\033[48;5;' + bg + ';38;5;' + fg + 'm' + string + '\033[0m', sep = sep, end = end, file = file, flush = flush);

