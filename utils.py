import json

ADDITIONNAL_DATA_FILE_PATH = "data/additionnal_data.json"


###### Toutes les fonctions qui permettent la liaison avec les fichiers de données JSON ######


# Fonction pour renvoyer le nombre de clé
def getKeyCounter():
    try:
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data.get("keyCounter", 0)  # Retourne 0 si 'keyCounter' n'existe pas
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")
        return None
    

# Fonction pour ajouter un nombre donné de clé au compteur dans le fichier JSON
def addToKeyCounter(value):
    if value <= 0:
        print("Error : Value must be positive.")
        return

    try:
        # Lecture des données existantes
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Ajout de la valeur à keyCounter
        data["keyCounter"] = data.get("keyCounter", 0) + value

        # Mise à jour du fichier JSON
        with open(ADDITIONNAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print(f"Value successfuly added. New keyCounter : {data['keyCounter']}")
    
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")

# Fonction pour réinitialiser le nombre de clé (appelée au début de chaque partie)
def resetKeyCounter():
    try:
        # Lecture des données existantes
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Remet à 0 la valeur de keyCounter
        data["keyCounter"] = 0

        # Mise à jour du fichier JSON
        with open(ADDITIONNAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print(f"Value successfuly added. New keyCounter : {data['keyCounter']}")
    
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")


# Fonction pour ajouter un nouveau joueur à l'équipe
def addToTeam(player_name):
    try:
        # Lire le contenu du fichier JSON
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Ajouter le joueur à la liste "team"
        if "team" in data:
            data["team"].append(player_name)
        else:
            data["team"] = [player_name]
        
        # Écrire les modifications dans le fichier
        with open(ADDITIONNAL_DATA_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"{player_name} has been added in the team.")

    except Exception as e:
        print(f"Error: {e}")


def resetTeam():
    try:
        # Lire le contenu du fichier JSON
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Vider la liste "team"
        data["team"] = []
        
        # Écrire les modifications dans le fichier
        with open(ADDITIONNAL_DATA_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print("Team reinitialised")
    except Exception as e:
        print(f"Error: {e}")


def getTeam():
    try:
        # Lire le contenu du fichier JSON
        with open(ADDITIONNAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Renvoyer la liste "team"
        return data.get("team", [])
    except Exception as e:
        print(f"Error: {e}")
        return []
