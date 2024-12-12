import random as rd

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

def tirOrdi():
    return (rd.randint(0,7), rd.randint(0,7))

def bateauxOrdi(L):
    for i in range(4):
        bateau = (rd.randint(0, 7), rd.randint(0, 7))
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