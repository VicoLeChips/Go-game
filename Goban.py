"""
Plateau
@author: Nexmat
last update: 03-04-2016
"""

import sys
from Exceptions import *
from Colors import cprint 

class Goban:
    """Modélise un plateau de jeu de Go, le goban."""

    def __init__(self, taille = 9):
        """Creates a Goban. 
        Goban takes as parameter the size of the goban itself."""
        self.taille = taille
        # On crée un tableau carré grâce à la taille passée en paramètre
        self.cell = [[None for i in range(taille)] for j in range(taille)]
        self.last_gobans = []


    def make_move(self, colonne, ligne, joueur):
        """Permet d'effectuer un tour de jeu.
        colonne (lettre): Désigne la colonne dans laquelle la pièce sera posée.
        ligne   (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (nombre): Désigne le joueur qui joue, 0 pour noir et 1 pour blanc.
        Retour: True ou False selon si l'opération a réussi ou non."""
        
        # Si tout est valide, on pose la pièce
        self.cell[ligne][colonne] = joueur
        
        return True
    
    
    def test_move(self, col, lgn, joueur):
        """Tester le coup choisi par le joueurs.
        col     (nombre): Désigne la colonne dans laquelle la pièce sera posée.
        lgn     (nombre): Désigne la ligne   dans laquelle la pièce sera posée.
        joueur  (Joueur): Désigne le joueur qui joue, joueur.number est 0 pour noir et 1 pour blanc.
        Retour: False selon s'il n'y a pas capture.
                Les groupes à capturer s'il y a capture.
                En cas de coup interdit, la fonction lève un erreur.
        """

        #print("\nGoban", lgn, col)

        capture = False
        captured_group = []

        # On vérifie si la colonne entree reste dans le goban
        if col < 0 or col >= self.taille:
            raise Forbidden_move(lgn, col, "mauvaise colonne entrée")

        # On vérifie si la ligne entree reste dans le goban
        if lgn < 0 or lgn >= self.taille:
            raise Forbidden_move(lgn, col, "mauvaise ligne entrée")

        # On vérifie que joueur est bien soit 1 soit 2
        if joueur.number != 0 and joueur.number != 1:
            raise Forbidden_move(lgn, col, "coup d'un non-joueur")

        # On vérifie que l'emplacement est bien vide
        if self.cell[lgn][col] != None:
            raise Forbidden_move(lgn, col, "intersection déjà prise")

        # On vérifie si il y a capture
        voisins = self.get_neighbour(lgn, col)

        # On met le coup en place pour calculer les libertés
        new_goban = []
        for old_lines in self.cell:
            new_goban.append(list(old_lines))
        new_goban[lgn][col] = joueur.number
        
        # Parmi les voisins
        for (i, j) in voisins:
            # S'il y a une pierre adverse
            if self.cell[i][j] != joueur.number and self.cell[i][j] != None:
                # On trouve le groupe de pierre auquel il est rattaché
                group = self.find_group(i, j, [], self.cell[i][j])

                # Determine si le groupe a une liberté ou non
                if not self.find_liberty(new_goban, group) and not self.edge_extend(new_goban, group):
                    capture = True
                    captured_group.append(group)

        # On fait le coup pour tester
        new_goban = make_capture(new_goban, captured_group)

        # On vérifie la règle du Ko
        if len(self.last_gobans) > 1 and self.was_same_state(new_goban) == True:
            raise Forbidden_move(lgn, col, "Ko")

        # On vérifie la règle du suicide
        if self.suicide_rule(col, lgn, joueur.number) == True and not capture == True:
            raise Forbidden_move(lgn, col, "suicide")

        if capture:
            return captured_group
        else:
            return False


    def was_same_state(self, new_goban):
        """Compare le goban courant avec le goban en paramètre
        Arg: new_goban (tableau) le nouveau goban à comparer
        Ret: True si les deux gobans ont le même état, False sinon"""
        for i in range(self.taille):
            for j in range(self.taille):
                if self.last_gobans[-2][i][j] != new_goban[i][j]:
                    return False
        return True

    
    def get_neighbour(self, i, j):
        """Trouve les voisins directs d'une case
        Arg: goban, le goban concerné
             (i,j) les coordonnées
        Ret: La liste des voisins """
        ret = []
    
        # Pas la première ligne
        if not i == 0:
            ret.append((i-1, j))
        # Pas la première colonne
        if not j == 0:
            ret.append((i, j-1))
        # Pas la dernière ligne
        if not i == self.taille - 1:
            ret.append((i+1, j))
        # Pas la première colonne
        if not j == self.taille - 1:
            ret.append((i, j+1))

        return ret


    def suicide_rule(self, col, lgn, joueur):
        """Détermine si la règle du suicide s'applique
        Arg: col, lgn sont les coordonnées du coup
             joueur est le joueur qui a effectué le coup
        Ret: True si il y a suicide False sinon"""
        voisins = self.get_neighbour(lgn, col)
        for (i, j) in voisins: 
            if self.cell[i][j] == None:
                return False
            if self.cell[i][j] == joueur:
                return False

        return True

    def save_goban(self, cells):
        self.last_gobans.append(cells)

    def find_group(self, i, j, group, color):
        """Trouve le groupe de pierre auquel la pierre entrée est rattachée
        Fonction récursive
        Arg: color la couleur du groupe (peut être None, ie vide)
        """
        # On recupere la liste des voisins
        voisins = self.get_neighbour(i, j) + [(i,j)]
        # On parcourt la liste des voisins
        for (k, l) in voisins:
            # Si le voisin est bien vide et n'est pas deja dans le groupe
            if self.cell[k][l] == color and not (k, l) in group:
                # On l'ajoute au groupe
                group.append((k,l))
                self.find_group(k, l, group, color)
        return group

    def find_liberty(self, goban, group):
        """Trouve les libertés d'un groupe
        Arg: goban, le plateau hypothétique"""
        for (i, j) in group:
            voisins = self.get_neighbour(i, j) + [(i, j)]
            for (k, l) in voisins:
                if goban[k][l] == None:
                    return True
        return False

    def edge_extend(self, goban, group):
        """Si un groupe s'étend de gauche à doite ou de haut en bas
        alors il ne peut être capturé """
        top, bot, left, right = False, False, False, False
        for (i, j) in group:
            if i == 0:
                top = True
            elif i == self.taille - 1:
                bot = True

            if j == 0:
                left = True
            elif j == self.taille - 1:
                right = True
        return (top and bot) or (left and right)


    def return_liberty(self, goban, group):
        """
        Trouve les libertés d'un groupe et les renvoie sous forme d'une liste
        Arg: goban, le plateau hypothétique
        """
        list_liberty = []
        for (i, j) in group:
            voisins = self.get_neighbour(i, j) + [(i, j)]
            for (k, l) in voisins:
                if goban[k][l] == None:
                    list_liberty.append((k,l))
        return list_liberty

def make_capture(goban, groups):
    """Fait les captures d'un (ou plusieurs) groupes de pierre
    Arg: groups, les groupes à capturer"""
    for group in groups:
        for (i, j) in group:
            goban[i][j] = None
    return goban


def detect_territory(goban):

    # On récupère toutes les cases vides
    coord_none = [(i, j) for i in range(goban.taille) for j in range(goban.taille) if goban.cell[i][j] == None]

    black_territory = []
    white_territory = []

    # Parmi toutes ces cases vides
    for (i, j) in coord_none:

        # On récupère les voisins non vides
        voisins = goban.get_neighbour(i, j)
        voisins = [(k, l) for (k, l) in voisins if goban.cell[k][l] != None]

        # Si tous les voisins sont vides, on passe à la case suivante
        if voisins == []:
            continue

        # S'ils sont tous noirs
        if find_color(goban, voisins) == 0:
            black_territory.append((i,j))

        # S'ils sont tous blancs
        elif find_color(goban, voisins) == 1:
            white_territory.append((i,j))

    #print("\n\n\nBlack:", black_territory) #TODO Affichage
    #print("White:", white_territory)
                
    return black_territory, white_territory

def find_color(goban, coords):
    """Determine la couleur des cases entrees en parametre
    Arg: coords, liste de coordonnees (i, j), ne peut pas désigner une case vide
    Ret: 0 pour noir, 1 pour blanc, 2 pour aucun
    """

    color = goban.cell[coords[0][0]][coords[0][1]]

    for (i, j) in coords:
        if goban.cell[i][j] != color:
            return 2
    return color


if __name__ == '__main__':
    g = Goban()
    
