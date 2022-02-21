"""
Quality
@author: MrChapelle, Nexmat
last update: 21-04-2016
"""

import sys
import timeit
import random
from Goban import *
from Joueur import *
from Exceptions import *

class Quality :
    """ Evalue la qualité d'un coup proposé """

    def __init__(self, niveau, game, joueur):
        """
        Constructeur
        """
        self.niveau = niveau
        self.game   = game
        self.joueur = joueur

    def capture_group(self, col, lgn):
        """
        :param col : colonne du coup testé
        :param lgn : ligne du coup testé
        :param goban : état actuel du plateau
        Détecte si le coup joué permettra de capturer un groupe
        Un groupe est capturé si sa liberté passe à 0
        """
        # on parcourt les voisins du coup testé
        for (k,l) in self.game.goban.get_neighbour(col,lgn):
            # on test si c'est un emplacement adverse
            if (self.game.goban.cell[k][l]!= None and self.game.goban.cell[k][l] != self.joueur.number):
                # si le groupe associé a cet emplacement n'a qu'une liberté et
                # que cette liberté correspond au coup qui va etre joué
                # on renvoie true
                if (len(self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color))) == 1):
                        if self.game.goban.return_liberty(goban, self.game.goban.find_group(k, l, [], color))[0] == (k,l):
                            return True
        return False

    def construct_group(self, col, lgn):
        """
        :param col : colonne du coup testé
        :param lgn : ligne du coup testé
        :param goban : état actuel du plateau
        Détecte si le coup testé contribue a la formation d'un groupe
        """
        num = 0
        # on parcourt les voisins du coup testé
        for (k, l) in self.game.goban.get_neighbour(lgn, col):
            # si un des voisins est déjà en possession du joueur alors cela contribue
            if self.game.goban.cell[k][l] == num :
                return True
        return False

    def influence(self, col, lgn): # Influence sur les territoiress
        # Influence de départ
        inf = 0

        # Detection des territoires
        territories = detect_territory(self.game.goban)

        # Nouveau cell
        new_cell = []
        # Copie des cells
        for old_lines in self.game.goban.cell:
            new_cell.append(list(old_lines))
        new_cell[lgn][col] = self.joueur.number # Ajout du coup

        # Nouveau goban
        new_goban = Goban(self.game.goban.taille)
        new_goban.cell = new_cell
        new_territories = detect_territory(new_goban)

        #if len(new_territories[self.joueur.number])>len(territories[self.joueur.number]):
        #    inf += (len(new_territories[self.joueur.number])-len(territories[self.joueur.number]))
        inf = len(new_territories[self.joueur.number]) - len(territories[self.joueur.number])
        return inf
        

    def importance(self, col, lgn):
        inf = 0
        try:
            ret = self.game.goban.test_move(col, lgn, self.joueur)
            inf = self.influence(col, lgn)
            # S'il n'y a pas de capture
            if ret == False:
                return (1 + inf)
            # S'il y a capture
            else:
                imp = 0
                # On calcule le nombre de pierres utilisées
                for group in ret:
                    imp += len(group)
                return imp * 2 + inf
                    
        # S'il y a erreur
        except Forbidden_move as e:
            #cprint("Erreur IA: coup interdit,", str(e), fg = "red")
            return 0

    def fuseki (self,numero):
        """
        permet de paramétrer le début de partie choisir par l'IA
        :param numero : int, caractérise le fuseki choisi
        :param numero :
         -> 0 : Ni Ren Sei
         -> 1 : San Ren Sei
         -> 2 : Fuseki Chinois
         -> 3 : Hoshi et Shimari
         -> 4 : San San et Shimari
         :return : la liste des coups a jouer selon la stratégie choisie
         """
        grandeur = self.game.goban.taille
        grd = grandeur - 4 
        if (numero == 0) :
            L = [(2,2), (2,grd)]
            return L
        elif (numero == 1) :
            L = [(grd,3), (grandeur-1,grd), (grd,grd)]
            return L
        elif (numero == 2) :
            L = [(grd,3),(grandeur//2,grd+1),(grd,grd)]
            return L
        elif (numero == 3) :
            L = [(grd,3),(grandeur-1,grd+1),(grd+1,grd)]
            return L
        else :
            L = [(grd,grd),(grd-1,grd-1),(grd+1,grd+1)]
            return L
         
    
