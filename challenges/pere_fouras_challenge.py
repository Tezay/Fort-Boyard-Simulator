import json
import random

JSON_FILE_PATH = ".\\data\\enigmesPF.json"

def pereFourasChallenge():
    # Charger les données du fichier JSON
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # On séléctionne une énigme au hasard dans le fichier json
    selected_question = random.choice(data)

    return selected_question["question"], selected_question["reponse"]
