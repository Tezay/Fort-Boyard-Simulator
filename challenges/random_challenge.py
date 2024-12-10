import random

# Fonction de l'énigme bonneteaux
def bonneteauChallenge():
    # Initialiser la liste des bonneteaux
    bonneteaux_list = ['A', 'B', 'C']
    # Choisir aléatoirement le bonneteau contenant la clé
    right_bonneteau = random.choice(bonneteaux_list)
    # Renvoie la liste de bonneteaux, et le bonneteau sous lequel se trouve la clé
    return bonneteaux_list, right_bonneteau


# Fonction énigme lancé de dés
def dices():
    users_dice_roll = (random.randint(1, 6), random.randint(1, 6))
    game_master_dice_roll = (random.randint(1, 6), random.randint(1, 6))
    return users_dice_roll, game_master_dice_roll


#def diceGameChallenge():
    try_number = 1
    number = 6
    win = False
    nb = -1
    while try_number < 3 and nb == -1 and win == False:
        input("Press enter to continue...")
        print("vous avez fait ",try_number,"essai")
        users_dice_roll, game_master_dice_roll = dices()
        print("vos dés son", users_dice_roll)
        if number in users_dice_roll:
            win = True
            nb = 1
        print(game_master_dice_roll)
        if number in game_master_dice_roll:
            win = False
        else:
            try_number += 1

    return win
#oui = diceGameChallenge()
#print(oui)
