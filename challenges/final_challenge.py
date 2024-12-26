import json
import random

JSON_FILE_PATH = ".\\data\\indicesSalle.json"

def final():
    try:
        # Lecture du fichier JSON
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file:
            donnees = json.load(file)
        
        # Extraire toutes les émissions
        emissions = []
        for annee, details in donnees["Fort Boyard"].items():
            emissions.extend(details.values())
        
        # Sélectionner une émission au hasard
        selected_emission = random.choice(emissions)
        
        # Extraire le mot-code et les indices
        code_word = selected_emission["MOT-CODE"]
        clues_list = selected_emission["Indices"]
        
        return code_word, clues_list

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None, None
