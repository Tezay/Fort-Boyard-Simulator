import random

##### Fonctions utiles #####

# Fonction énigme lancé de dés
def dices():
    users_dice_roll = (random.randint(1, 6), random.randint(1, 6))
    game_master_dice_roll = (random.randint(1, 6), random.randint(1, 6))
    return users_dice_roll, game_master_dice_roll

def randomNum():
    return random.randint(1, 50)

def randomCoin():
    coin = ["Face", "Pile"]
    return random.choice(coin)
##### Fonctions des énigmes de hasard #####


# Fonction de l'énigme bonneteaux
def bonneteauChallenge():
    # Initialiser la liste des bonneteaux
    bonneteaux_list = ['A', 'B', 'C']
    # Choisir aléatoirement le bonneteau contenant la clé
    right_bonneteau = random.choice(bonneteaux_list)
    # Renvoie la liste de bonneteaux, et le bonneteau sous lequel se trouve la clé
    return bonneteaux_list, right_bonneteau


# Fonction de l'énigme lancé de dés
def diceRollChallenge():
    roll = (random.randint(1, 6), random.randint(1, 6))
    return roll


# Fonction de l'énigme du nombre aléatoire
def randomNumberChallenge():
    number = randomNum()
    master_answer = random.randint(number-11, number+11)
    return master_answer, number

def coinChallenge():
    coin = randomCoin()
    return coin