import sys
from Colors import cprint

HR_LINE = chr(9472)
VR_LINE = chr(9474)
INTERSE = chr(9532)

def color_display(goban):
    """Affiche dans le terminal le goban"""
    # Affichage des lettres des colonnes
    cprint('    ', bg = "brown", end = '')
    for i in range(len(goban.cell[0])):
        cprint(chr(65 + i) + '  ', bg = "brown", end = '')
    print('')

    # Première ligne de verticaux
    cprint('    ', bg = "brown", end = '')
    for i in goban.cell[0]:
        cprint(VR_LINE + '  ', bg = "brown", end = '')
    print('')

    nb_ligne = 1
    # Pour chaque ligne
    for ligne in goban.cell:
        # Affichages des numéros de ligne
        cprint(repr(nb_ligne).rjust(2), bg = "brown", end = '')
        nb_ligne += 1

        # Lignes horizontales
        cprint(HR_LINE * 2, bg = "brown", end = '')

        # Affichage des intersections
        for colonne in ligne:
            # Intersection
            if colonne == None:
                cprint(INTERSE + HR_LINE * 2, bg = "brown", end = '')
            # Pion
            else:
                # Le joueur blanc
                if colonne == 1:
                    cprint("0", bg = "brown", end = '')
                    cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
                # Le joueur noir
                else:
                    cprint("0", fg = "black", bg = "brown", end = '')
                    cprint(HR_LINE * 2, fg = "white", bg = "brown", end = '')
        print("")
        cprint('    ', bg = "brown", end = '')

        # Lignes verticales
        for colonne in ligne:
            cprint(VR_LINE + '  ', bg = "brown", end = '')
        print('')

def display_min(goban):
    """Affiche dans le terminal le goban"""
    # Affichage des lettres des colonnes
    print('    ', end = '')
    for i in range(len(goban.cell[0])):
        print(chr(65 + i) + '  ', end = '')
    print('')

    # Première ligne de verticaux
    print('    ', end = '')
    for i in goban.cell[0]:
        print(VR_LINE + '  ', end = '')
    print('')

    nb_ligne = 1
    # Pour chaque ligne
    for ligne in goban.cell:
        # Affichages des numéros de ligne
        print(repr(nb_ligne).rjust(2), end = '')
        nb_ligne += 1

        # Lignes horizontales
        print(HR_LINE * 2, end = '')

        # Affichage des intersections
        for colonne in ligne:
            # Intersection
            if colonne == None:
                print(INTERSE + HR_LINE * 2, end = '')
            # Pion
            else:
                if colonne == 0:
                    print("0", end = '')
                    print(HR_LINE * 2, end = '')
                else:
                    print("1", end = '')
                    print(HR_LINE * 2, end = '')
        print("")
        print('    ', end = '')

        # Lignes verticales
        for colonne in ligne:
            print(VR_LINE + '  ', end = '')
        print('')

def round_display(partie):
    # On affiche le numéro du tour
    cprint("\n\n\n        - Tour numéro", str(partie.tour + 1), "-", fg = "blue")
    cprint("----------------------------------", fg = "blue")
    
    # Score du joueur noir
    cprint(" Joueur noir: " + str(partie.player1.score), fg = "black", bg = "blue", end = "")

    # Score du joueur blanc
    cprint(" Joueur blanc: " + str(partie.player2.score) + " ", fg = "white", bg = "blue", end = "")
    cprint("\n----------------------------------\n", fg = "blue")

    # Affichage du goban
    color_display(partie.goban)
    print()

    # Affichage de la ligne d'input
    cprint(" Au tour du joueur ", bg = "blue", end = "")
    # Tour du joueur noir
    if partie.tour % 2 == 0:
        cprint("noir ", fg = "black",  bg = "blue", end = "")
    # Tour du joueur blanc
    else: 
        cprint("blanc ", fg = "white",  bg = "blue", end = "")
    cprint(">> ", fg = "white",  bg = "blue", end = "")
    sys.stdout.flush()

def round_display_min(partie):
    # On affiche le numéro du tour
    print("\n\n\n        - Tour numéro", str(partie.tour + 1), "-")
    print("----------------------------------")
    
    # Score du joueur noir
    print(" Joueur noir: " + str(partie.player1.score), end = "")

    # Score du joueur blanc
    print(" Joueur blanc: " + str(partie.player2.score) + " ", end = "")
    print("\n----------------------------------\n")

    # Affichage du goban
    display_min(partie.goban)
    print()

    print(" Au tour du joueur ", end = "")
    # Tour du joueur noir
    if partie.tour % 2 == 0:
        print("noir ", end = "")
    # Tour du joueur blanc
    else: 
        print("blanc ", end = "")
    print(">>", end = "")
    sys.stdout.flush()


def display_end_game(partie):
    print("\n\n")
    cprint(" ---------------------------------- ", fg = "blue")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|", fg = "black", end = "")
    cprint("          FIN DE PARTIE           ", fg = "blue",  end = "")
    cprint("|", fg = "white", end = "\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    # Score du joueur noir
    cprint("| Joueur noir: " + str(partie.player1.score), fg = "black", bg = "blue", end = "")
    # Score du joueur blanc
    cprint(" Joueur blanc: " + str(partie.player2.score) + " |", fg = "white", bg = "blue", end = "\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    # Territoire du joueur noir
    cprint("| Terr. noir: " + str(len(partie.player1.territory)) + " ", fg = "black", bg = "blue", end = "")
    # Territoire du joueur blanc
    cprint(" Terr. blanc: " + str(len(partie.player2.territory)) + "    |", fg = "white", bg = "blue", end = "\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    # Territoire du joueur noir
    cprint("| Score noir: " + str(len(partie.player1.territory) + partie.player1.score) + " ", fg = "black", bg = "blue", end = "")
    # Territoire du joueur blanc
    cprint(" Score blanc: " + str(len(partie.player2.territory) + partie.player2.score) + "  |", fg = "white", bg = "blue", end = "\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|", fg = "black", end = "")
    if (len(partie.player1.territory) + partie.player1.score < len(partie.player2.territory) + partie.player2.score):
        cprint("      VICTOIRE JOUEUR BLANC       ", fg = "blue", end = "")
    elif (len(partie.player1.territory) + partie.player1.score > len(partie.player2.territory) + partie.player2.score):
        cprint("      VICTOIRE JOUEUR NOIR        ", fg = "blue", end = "")
    else:
        cprint("             EGALITE              ", fg = "blue", end = "")
    cprint("|", fg = "white", end = "\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint("|                                  ", fg = "black", end = "|\n")
    cprint(" ---------------------------------- ", fg = "blue")

def display_end_game_min(partie):
    print("\n\n")
    print(" ---------------------------------- ")
    print("|                                  ", end = "|\n")
    print("|", end = "")
    print("          FIN DE PARTIE           ",  end = "")
    print("|", end = "\n")
    print("|                                  ", end = "|\n")
    # Score du joueur noir
    print("| Joueur noir: " + str(partie.player1.score), end = "")
    # Score du joueur blanc
    print(" Joueur blanc: " + str(partie.player2.score) + " |", end = "\n")
    print("|                                  ", end = "|\n")
    print("|                                  ", end = "|\n")
    # Territoire du joueur noir
    print("| Terr. noir: " + str(len(partie.player1.territory)) + " ", end = "")
    # Territoire du joueur blanc
    print(" Terr. blanc: " + str(len(partie.player2.territory)) + "    |", end = "\n")
    print("|                                  ", end = "|\n")
    print("|                                  ", end = "|\n")
    # Territoire du joueur noir
    print("| Score noir: " + str(len(partie.player1.territory) + partie.player1.score) + " ", end = "")
    # Territoire du joueur blanc
    print(" Score blanc: " + str(len(partie.player2.territory) + partie.player2.score) + "  |", end = "\n")
    print("|                                  ", end = "|\n")
    print("|", end = "")
    if (len(partie.player1.territory) + partie.player1.score < len(partie.player2.territory) + partie.player2.score):
        print("      VICTOIRE JOUEUR BLANC       ", end = "")
    elif (len(partie.player1.territory) + partie.player1.score > len(partie.player2.territory) + partie.player2.score):
        print("      VICTOIRE JOUEUR NOIR        ", end = "")
    else:
        print("             EGALITE              ", end = "")
    print("|", end = "\n")
    print("|                                  ", end = "|\n")
    print("|                                  ", end = "|\n")
    print("|                                  ", end = "|\n")
    print(" ---------------------------------- ")
