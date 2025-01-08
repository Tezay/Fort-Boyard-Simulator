import json
import random
import os
from datetime import datetime

LOCAL_DATA_FILE_PATH = "data/local_data.json"
CHALLENGES_LIST_FILE_PATH = "data/challenges_list.json"
VIDEO_FOLDER_PATH = "static/video/new_key/"


###### Toutes les fonctions qui permettent la liaison avec les fichiers de données JSON ######


# Fonction pour renvoyer le nombre de clés
def getKeyCounter():
    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data.get("keyCounter", 0)  # Retourne 0 si 'keyCounter' n'existe pas
    except Exception as e:
        print(f"Error: {e}")

# Fonction pour ajouter un nombre donné de clés au compteur dans le fichier JSON
def addToKeyCounter(value):
    if value <= 0:
        print("Error : Value must be positive.")
        return

    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Ajout de la valeur à keyCounter
        data["keyCounter"] = data.get("keyCounter", 0) + value

        # Mise à jour du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print(f"Value successfully added. New keyCounter: {data['keyCounter']}")
    
    except Exception as e:
        print(f"Error: {e}")

# Fonction pour réinitialiser le nombre de clés (appelée au début de chaque partie)
def resetKeyCounter():
    try:
        # Lire le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Remet à 0 la valeur de keyCounter
        data["keyCounter"] = 0

        # Mise à jour du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)  # Sauvegarde avec une mise en forme lisible
        
        print("Key counter successfully reset.")
    
    except Exception as e:
        print(f"Error: {e}")


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
        # Charger le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Vider la section "team"
        data["team"] = {}
        
        # On écrit les modifications dans le fichier
        with open(LOCAL_DATA_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print("Team reinitialized.")
    except Exception as e:
        print(f"Error: {e}")

# Fonction pour obtenir la liste des joueurs de l'équipe
def getTeam():
    # Charger le contenu du fichier JSON
    with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # On extrait les informations des joueurs
    team_list = []
    for player_name, player_data in data.get("team", {}).items():
        player_info = {
            "name": player_name,
            **player_data
        }
        team_list.append(player_info)
    
    return team_list


def addToPassedChallenges(player):
    # Charger le contenu du fichier JSON
    with open(LOCAL_DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # On vérifie si le joueur existe dans l'équipe
    if player in data['team']:
        # Ajouter +1 à passedChallenges du joueur
        data['team'][player]['passedChallenges'] += 1

        # Enregistrer les modifications dans le fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Challenge added for {player}.")
    else:
        print(f"{player} is not in the file.")


# Fonction qui renvoie une énigme au hasard parmi la catégorie spécifiée
def chooseChallengeByType(type):
    try:
        # Charger les données JSON depuis le fichier
        with open(CHALLENGES_LIST_FILE_PATH, "r") as file:
            data = json.load(file)
        
        # Vérifier si le type existe dans les données
        if type in data:
            challenges = data[type]
            # Retourner une épreuve aléatoire dans la catégorie spécifiée
            return random.choice(challenges)
        else:
            print(f"Type :'{type}' is not in the file.")
    except Exception as e:
        print(f"Error: {e}")

# Fonction qui renvoie la liste de tous les challenges par type (sous forme de dictionnaire)
# Note : sert uniquement pour le mode debug
def getChallengesList():
    try:  
        # Ouvrir le fichier JSON et charger les données
        with open(CHALLENGES_LIST_FILE_PATH, 'r') as file:
            data = json.load(file)
        # On renvoie toutes les énigmes par catégorie
        return data
    except Exception as e:
        print(f"Error: {e}")


# Fonction pour renvoyer le compteur de chaque type d'énigme
def getChallengesCount():
    try:
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data['challengesCount']
    except Exception as e:
        print(f"Error: {e}")


# Fonction pour incrémenter le compteur d'une épreuve spécifiée
def addToChallengesCount(challenge):
    # Charger le contenu du fichier JSON
    with open(LOCAL_DATA_FILE_PATH, 'r') as file:
        data = json.load(file)

    # Vérifier si le challenge existe
    if challenge in data['challengesCount']:
        # Ajouter +1 au challenge
        data['challengesCount'][challenge] += 1

        # Enregistrer les modifications dans le fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Challenge counter incremented for {challenge}.")
    else:
        print(f"{challenge} is not in the file.")



def resetChallengesCount():
    try:
        # Charger le contenu du fichier JSON
        with open(LOCAL_DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Vérifier si "challengesCount" existe dans les données
        if "challengesCount" in data:
            # Réinitialiser les compteurs des épreuves
            for key in data["challengesCount"]:
                data["challengesCount"][key] = 0
            
            # Sauvegarder les modifications dans le fichier
            with open(LOCAL_DATA_FILE_PATH, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            print("Key not found.")

    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


##### Fonction pour séléctionner un fichier vidéo au hasard pour la page "ney-key" #####

# Fonction pour séléctionner le chemin d'accès d'une vidéo aléatoirement dans le dossier
def selectRandomVideo():
    # Liste tous les fichiers dans le dossier "video"
    file_name = os.listdir(VIDEO_FOLDER_PATH)
    # On renvoie le path d'un fichier au hasard parmi le dossier
    if file_name:
        return "video/new_key/" + random.choice(file_name)
    else:
         return None
    
# Fonction pour enregister les données de la partie dans un fichier log
def storeGameData(score):
    # On charge les données JSON à partir du fichier
    with open(LOCAL_DATA_FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    # On extrait les informations nécessaires
    key_counter = data.get("keyCounter", 0)
    team = data.get("team", {})

    # On construie les lignes
    lines = []
    lines.append(f"Nombre de pièces obtenues par l'équipe : {score}")
    lines.append(f"Nombre de clés obtenues par l'équipe : {key_counter}")

    team_composition = ", ".join(team.keys())
    lines.append(f"Composition de l'équipe : {team_composition}")

    lines.append("Statistiques des joueurs :")
    # On ajoute l'information que le joueur est leader si la condition est vérifiée
    for player, stats in team.items():
        if stats.get("is_leader", False):
            is_leader = " (leader)"
        else:
            is_leader = ""

        job = stats.get("job", "aucun")
        passed_challenges = stats.get("passedChallenges", 0)
        lines.append(f"{player}, {job}{is_leader} : {passed_challenges} épreuves passées")

    # On créer le dossier log s'il n'existe pas
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)

    # On génère un nom de fichier unique avec horodatage
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"game_log_{timestamp}.txt")

    # On écrit les lignes dans le fichier log
    with open(log_file, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Game data saved in file : {log_file}")