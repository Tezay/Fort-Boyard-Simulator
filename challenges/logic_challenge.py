import random as rd

# Fonctions pour l'énigme bataille navale

def errorNavalBattle(L, moment_game):
    if len(L) == 4 and moment_game == "beginning":
        return True
    elif len(L) == 1 and moment_game == "middle":
        return  True
    else:
        return False

def navalBattleGame(bateaux, case):
    print(bateaux, case)
    for bateau in bateaux:
        if case == bateau:
            return True
    return False

def tirOrdi():
    return (rd.randint(0,8), rd.randint(0,8))

def bateauxOrdi(L):
    for i in range(4):
        bateau = (rd.randint(0, 8), rd.randint(0, 8))
        if bateau not in L:
            L.append(bateau)
    return L