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


# Fonction qui renvoie la liste de tous les challenges par type (sous forme de dictionnaire)
def getChallengesListByType():
    data = loadData()
    
    # Créer un dictionnaire avec en clé le type de challenge et en valeur la liste des challenges
    challenges_by_type = {}
    for challenge_type, challenge_data in data['challengesTypes'].items():
        challenges_by_type[challenge_type] = challenge_data['challengesList']

    return challenges_by_type