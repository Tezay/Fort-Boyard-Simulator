import random

# Fonction de l'énigme bonneteaux
def bonneteauChallenge():
    # Initialiser la liste des bonneteaux
    bonneteaux_list = ['A', 'B', 'C']
    # Choisir aléatoirement le bonneteau contenant la clé
    right_bonneteau = random.choice(bonneteaux_list)
    # Renvoie la liste de bonneteaux, et le bonneteau sous lequel se trouve la clé
    return bonneteaux_list, right_bonneteau