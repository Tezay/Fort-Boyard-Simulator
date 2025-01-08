import random as rd

##### Fonctions pour l'épreuve bataille navale #####

# Vérifie si le nombre de cases fournies est correct en fonction de l'étape du jeu
def errorNavalBattle(L, moment_game):
    # Si le moment est le début du jeu, il faut fournir exactement 4 cases
    if len(L) == 4 and moment_game == "beginning":
        return True
    # Si le moment est le milieu du jeu, une seule case est attendue
    elif len(L) == 1 and moment_game == "middle":
        return True
    else:
        return False

# Vérifie si une case donnée correspond à un bateau présent
def navalBattleGame(bateaux, case):
    # Parcourt toutes les cases des bateaux pour vérifier la correspondance
    for bateau in bateaux:
        if case == bateau:
            return True
    return False

# Génère une position aléatoire pour le tir de l'ordinateur
def tirOrdi(taille):
    return (rd.randint(0, taille-1), rd.randint(0, taille-1))

# Place aléatoirement les bateaux de l'ordinateur sur la grille
def bateauxOrdi(L, taille):
    # Génère 4 positions uniques pour les bateaux
    for i in range(4):
        bateau = (rd.randint(0, taille-1), rd.randint(0, taille-1))
        if bateau not in L:
            L.append(bateau)
    return L

# Vérifie si un joueur a coulé tous les bateaux
def gagnant(dico):
    compteur = 0
    # Compte le nombre de tirs réussis
    for tir in dico.values():
        if tir:
            compteur += 1
    # Si 4 tirs réussis, le joueur gagne
    return compteur == 4

# Détermine le gagnant entre le joueur et l'ordinateur
def whoWin(player1, ordi):
    if player1:
        return "player"
    elif ordi:
        return "ordi"
    else:
        return None

##### Fonctions pour l'épreuve morpion #####

# Met à jour la grille après le coup d'un joueur
def updateBoard(pos_morpion, move, person):
    # Définit la valeur selon le joueur
    if person == "player":
        pos_morpion[move[0]][move[1]] = 1
    else:
        pos_morpion[move[0]][move[1]] = 2
    return pos_morpion

# Génère un coup aléatoire pour l'ordinateur
def masterMove():
    return (rd.randint(0, 2), rd.randint(0, 2))

# Vérifie si un joueur a une ligne gagnante
def verifLin(pos_morpion, person):
    n = len(pos_morpion)
    key = 1 if person == "player" else 2
    for elt in pos_morpion:
        # Si toutes les cases d'une ligne appartiennent au joueur, il gagne
        if elt[0] == elt[1] == elt[2] and elt[0] == key:
            return True
    return False

# Vérifie si un joueur a une colonne gagnante
def verifCol(pos_morpion, person):
    key = 1 if person == "player" else 2
    for i in range(len(pos_morpion)):
        # Si toutes les cases d'une colonne appartiennent au joueur, il gagne
        if pos_morpion[0][i] == pos_morpion[1][i] == pos_morpion[2][i] and pos_morpion[0][i] == key:
            return True
    return False

# Vérifie si un joueur a une diagonale anti-gagnante
def verifAntiDiag(pos_morpion, person):
    n = len(pos_morpion)
    counter = 0
    key = 1 if person == "player" else 2
    for i in range(n):
        for j in range(n):
            if i + j == 2 and pos_morpion[i][j] == key:
                counter+= 1
    # Si la diagonale anti est remplie par le joueur, il gagne
    if counter == 3:
        return True
    return False

# Vérifie si un joueur a une diagonale gagnante
def verifDiag(pos_morpion, person):
    n = len(pos_morpion)
    counter = 0
    if person == "player":
        key = 1
    else:
        key = 2
    for i in range(n):
        for j in range(n):
            if i - j == 0 and pos_morpion[i][j] == key:
                counter+= 1
    # Si la diagonale est remplie par le joueur, il gagne
    if counter == 3:
        return True
    return False

# Vérifie si un joueur a gagné sur l'une des conditions
def isSol(pos_morpion, person):
    return verifLin(pos_morpion, person) or verifCol(pos_morpion, person) or verifAntiDiag(pos_morpion, person) or verifDiag(pos_morpion, person)

# Vérifie si la grille est pleine (égalité)
def verifEgal(pos_morpion):
    for line in pos_morpion:
        for elt in line:
            if elt == 0:
                return False
    return True

# Vérifie si un mouvement est valide
def errorTicTacToe(player_move):
    # Un mouvement valide doit contenir exactement une case
    if len(player_move) != 1:
        return False
    return True