import json

LOCAL_DATA_FILE_PATH = "data/local_data.json"


###### Toutes les fonctions qui permettent la liaison avec les fichiers de données JSON ######


# Fonction pour renvoyer le nombre de clés
def getKeyCounter():
    try:
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data.get("keyCounter", 0)  # Retourne 0 si 'keyCounter' n'existe pas
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")
        return None

# Fonction pour ajouter un nombre donné de clés au compteur dans le fichier JSON
def addToKeyCounter(value):
    if value <= 0:
        print("Error : Value must be positive.")
        return

    try:
        # Lecture des données existantes
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Ajout de la valeur à keyCounter
        data["keyCounter"] = data.get("keyCounter", 0) + value

        # Mise à jour du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print(f"Value successfully added. New keyCounter: {data['keyCounter']}")
    
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")

# Fonction pour réinitialiser le nombre de clés (appelée au début de chaque partie)
def resetKeyCounter():
    try:
        # Lecture des données existantes
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Remet à 0 la valeur de keyCounter
        data["keyCounter"] = 0

        # Mise à jour du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print("Key counter successfully reset.")
    
    except FileNotFoundError:
        print("Error : Specified JSON file is not found.")



# Fonction pour ajouter un nouveau joueur à l'équipe
def addToTeam(player_name, is_leader, job):
    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Ajouter le joueur avec ses attributs
        player_data = {
            "is_leader": is_leader,
            "job": job,
            "passedChallenges": 0
        }
        data["team"][player_name] = player_data
        
        # Écrire les modifications dans le fichier
        with open(LOCAL_DATA_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"{player_name} has been added to the team.")

    except Exception as e:
        print(f"Error: {e}")

# Fonction pour réinitialiser l'équipe
def resetTeam():
    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Vider la section "team"
        data["team"] = {}
        
        # Écrire les modifications dans le fichier
        with open(LOCAL_DATA_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print("Team reinitialized.")
    except Exception as e:
        print(f"Error: {e}")

# Fonction pour obtenir la liste des joueurs de l'équipe
def getTeam():
    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Extraire et formater les informations des joueurs
        team_list = []
        for player_name, player_data in data.get("team", {}).items():
            player_info = {
                "name": player_name,
                **player_data
            }
            team_list.append(player_info)
        
        return team_list
    except Exception as e:
        print(f"Error: {e}")
        return []