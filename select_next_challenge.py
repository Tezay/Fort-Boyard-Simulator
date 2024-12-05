import json
import random

file_path = "data/additionnal_data.json"

# Charger les données depuis le fichier JSON
def loadData():
    with open(file_path, 'r') as f:
        return json.load(f)

# Fonction pour choisir un challenge au hasard
def chooseRandomChallenge():
    # Créer une liste vide pour tous les challenges
    all_challenges = []
    data = loadData()

    # Ajouter tous les challenges des trois types dans la liste
    for challenge_type in data['challengesTypes']:  # Itérer sur les clés
        all_challenges += data['challengesTypes'][challenge_type]['challengesList']
    
    # Choisir un challenge au hasard
    chosen_challenge = random.choice(all_challenges)
    
    return chosen_challenge
