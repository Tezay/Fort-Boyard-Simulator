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