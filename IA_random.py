"""
IA_random
@author: MrChapelle
last update: 21-04-2016
"""

import sys
import timeit
import random
from Joueur import Joueur
from Goban import *
from Exceptions import *
from Colors import cprint
from optparse import OptionParser;

class IA_random(Joueur):
    """ Modélise les caractéristiques du joueur IA random """

    def __init__(self, number, game, isHuman = False, score = 0):
        """
        Constructeur : Definit les caracteristiques du joueur IA
        isHuman : bool définit si le joueur est humain ou non
        clock   : float, temps de jeu courant du joueur
        score   : int, score du joueur
        number  : int, numero du joueur IA (0 ou 1)
        moves   : array de couples désigne les coups du joueur (lgn, col)
        """
        super().__init__(number, game, isHuman = False, score = score)
    

    def choose_move(self):
        """
        Determine le mouvement de l'IA jusqu'à
        obtenir un coup possible
        
        return: les coordonnées entrées (col, lgn)
        """
        coord = "pass"
        for i in range(10000):                #on teste aléatoirement 10000 fois 
            col = random.randint(0, self.game.goban.taille - 1)
            lgn = random.randint(0, self.game.goban.taille - 1)
            try: 
                if self.game.goban.test_move(col, lgn, self) == False:
                    coord = (col, lgn)
                    sys.stdout.flush()
                    return coord
            except Forbidden_move as e:
                pass

        for col in range(self.game.goban.taille):
            for lgn in range(self.game.goban.taille):
                try: 
                    if not self.game.goban.test_move(col, lgn, self) == False:
                        coord = (col, lgn)
                        return coord
                except:
                    pass

        return coord

