# Fort Boyard Simulator
Projet EFREI TI101 - Programmation en Python

## 1. Présentation Générale

### Etat du projet
Ce projet est en cours de développement, les fonctionnalités proposées ne sont pas encore entièrement terminées.

### Contributeurs
- Eliot.C : Tezay
- Eliot.C : CSScooby

### Description
Dans le cadre d'un projet d'école en programmation en Python, nous avons réalisé un mini-jeu qui reprend le concept de Fort Boyard, avec des épreuves variées qui permettent aux joueurs d'obtenir des clés, et d'accéder à la salle au trésor.

Notre projet se démarque par l'utilisation du framework Flask, qui permet une expérience de jeu plus immersive, en proposant une interface personnalisée directement dans le navigateur internet. 

### Fonctionnalités Principales
- Enigmes de mathématiques, logique, chance, et épreuve du Père Fouras.
- Gestion des composants du jeu dans des fichiers JSON.
- etc.

### Technologies Utilisées
- **Langages de programmation :** Python (pour l'intégralité du backend), HTML et CSS (pour la partie bonus, frontend)
- **Bibliothèques :** Flask, random
- **Outils :** VSCode, pyCharm, chatGPT 4o

### Installation

#### Prérequis :
Python 3.9+, pip, un navigateur internet.

#### 1. Instructions pour cloner le dépôt Git
```bash
git clone https://github.com/Tezay/Fort-Boyard-Simulator.git
cd Fort-Boyard-Simulator
```
#### 2. Configuration de l'environnement de développement (optionnel)
```bash
python -m venv env
```
- Sous Windows :
    ```
    .\env\Scripts\activate
    ```
- Sous macOS/Linux :
    ```
    source env/bin/activate
    ```
#### 3. Installation des dépendances nécessaires
```bash
pip install -r requirements.txt
```
#### 4. Création du fichier de données locales
Dans le dossier `data/`, dupliquer le fichier `local_data_example.json` et le renommer `local_data.json` (commande ci-dessous)
```bash
cp data/local_data_example.json data/local_data.Json
```

### Utilisation
Pour lancer le projet, exécuter le fichier **app.py**
```bash
python app.py
```
Depuis un navigateur, se connecter en local sur le port 5000 (Flask) :
```url
http://127.0.0.1:5000/
```

## 2. Documentation Technique

### 1. Initialisation
1.1 Composition de l'équipe 

- Nombre de joueurs, nom et profession des joueurs 

### 2. Début du jeux
2.1 Entrez sur le fort 

2.2 Choix du joueur qui fera l'épreuve 

2.3 Choix de l'épreuve 
  
- Choix parmi les 4 type d'épreuves possible 
  - mathématique
  - logique
  - aléatoire
  - Pere Fouras 

2.4 Dans le type d'épreuve choisi auparavant choix aléatoire d'une épreuve

### 3. Début des épreuves 
3.1 Exécution de l'épreuve : 

- Le joueur séléctionner réalise l'epreuve qu'il a choisis.
  
  - Épreuve réussie -> Clef gagné et ajouter au compteur 
  - Épreuve raté -> Aucune clef n'est donné

### 4. Duré du jeux

4.1 Chaque type d'épreuve doit être efféctué au moins 1 fois et au maximum 2 fois 

4.2 Il faut au minimum trois clefs pour rentrer dans l'épreuve final 

4.3 Au bout de 5 clefs les épreuve s'arrette et c'est le passage à l'épreuve final

### 5. Épreuve finale 

5.1 En fonction du nombre de clefs, le même nombre d'indices est donné 
  
  - Trois chances pour réussir l'épreuve finale
  - À chaque essaie un indice est ajouté pour aider les joueures 