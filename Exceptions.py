"""
Exceptions
@author: Nexmat, MrChapelle, MorfoisseT
last update: 08-04-2016
"""

class Forbidden_move(Exception):
    def __init__(self, lgn, col, msg):
        self.lgn = lgn
        self.col = col
        self.msg = msg

    def __str__(self):
        self.translate_coord()
        return self.msg + " en " + self.col + str(self.lgn) + "."

    def translate_coord(self):
        self.lgn += 1
        self.col = chr(self.col + 65)
