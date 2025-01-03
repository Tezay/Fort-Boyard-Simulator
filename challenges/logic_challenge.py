import random as rd

##### Fonctions pour l'épreuve bataille navale #####

def errorNavalBattle(L, moment_game):
    if len(L) == 4 and moment_game == "beginning":
        return True
    elif len(L) == 1 and moment_game == "middle":
        return  True
    else:
        return False

def navalBattleGame(bateaux, case):
    for bateau in bateaux:
        if case == bateau:
            return True
    return False

def tirOrdi(taille):
    return (rd.randint(0,taille-1), rd.randint(0,taille-1))

def bateauxOrdi(L, taille):
    for i in range(4):
        bateau = (rd.randint(0, taille-1), rd.randint(0, taille-1))
        if bateau not in L:
            L.append(bateau)
    return L

def gagnant(dico):
    compteur = 0
    for tir in dico.values():
        if tir:
            compteur += 1

    return compteur == 4

def whoWin(player1, ordi):
    if player1:
        return "player"
    elif ordi:
        return "ordi"
    else:
        return None



##### Fonctions pour l'épreuve morpion #####

def updateBoard(pos_morpion, move, person):
    if person == "player":
        pos_morpion[move[0]][move[1]] = 1
    else:
        pos_morpion[move[0]][move[1]] = 2
    return pos_morpion

def masterMove():
    return (rd.randint(0, 2), rd.randint(0, 2))

def verifLin(pos_morpion, person):
    n = len(pos_morpion)
    if person == "player":
        key = 1
    else:
        key = 2
    for elt in pos_morpion:
        if elt[0] == elt[1] == elt[2] and elt[0] == key:
            return True
    return False

def verifCol(pos_morpion, person):
    if person == "player":
        key = 1
    else:
        key = 2
    for i in range(len(pos_morpion)):
        if pos_morpion[0][i] == pos_morpion[1][i] == pos_morpion[2][i] and pos_morpion[0][i] == key:
            return True
    return False

def verifAntiDiag(pos_morpion, person):
    n = len(pos_morpion)
    counterDict = {}
    if person == "player":
        key = 1
    else:
        key = 2
    for i in range(n):
        for j in range(n):
            if i+j in counterDict and pos_morpion[i][j] == key:
                counterDict[i+j] += 1
            elif i+j not in counterDict and pos_morpion[i][j] == key:
                counterDict[i+j] = 1
    if 2 in counterDict and counterDict[2] == 3:
        return True
    return False

def verifDiag(pos_morpion, person):
    n = len(pos_morpion)
    counterDict = {}
    if person == "player":
        key = 1
    else:
        key = 2
    for i in range(n):
        for j in range(n):
            if i-j in counterDict and pos_morpion[i][j] == key:
                counterDict[i-j] += 1
            elif i-j not in counterDict and pos_morpion[i][j] == key:
                counterDict[i-j] = 1
    if 0 in counterDict and counterDict[0] == 3:
        return True
    return False

def estSol(pos_morpion, person):
    return verifLin(pos_morpion, person) or verifCol(pos_morpion, person) or verifAntiDiag(pos_morpion, person) or verifDiag(pos_morpion, person)

def verifEgal(pos_morpion):
    for line in pos_morpion:
        for elt in line:
            if elt == 0:
                return False
    return True

def errorTicTacToe(player_move):
    if len(player_move) != 1:
        return False
    return True