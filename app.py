# Imports des modules
from flask import Flask, render_template, request, redirect, url_for, abort, session
from challenges import *
from utils import *
import argparse

# On créer l'application Flask
app = Flask(__name__)


# Route du menu principal
@app.route("/")
def menu():
    # Appelle la fonction qui permet de réinitialiser le nombre de clés
    resetKeyCounter()
    # Appelle la fonction qui permet de réinitialiser la composition de l'équipe
    resetTeam()
    # Appelle de la fonction qui permet de réinitialiser les compteurs d'épreuves
    resetChallengesCount()
    # Vérifie si le mode débug est actif ou pas
    debug_mode = app.debug
    # On retourne la template de la page HTML dédiée, et on passe en paramètre la variable debug_mode
    return render_template("index.html", debug_mode=debug_mode)


# Route pour le Fort Boyard
@app.route("/fort-boyard")
def fortBoyard():
    # On récupère le nombre de clés
    key_count = getKeyCounter()
    # Vérifie si le mode debug est actif ou pas
    # Permet d'avoir accès à la page admin (repertorie toutes les énigmes dispo) lorsqu'actif
    debug_mode = app.debug
    #Renvoie la page HTML du Fort Boyard (salle où les joueurs reviennent après chaque épreuve)
    # Transmet en paramètre la variable key_count:int (pour afficher le nombre de clés obtenues)
    return render_template("fort-boyard.html", key_count=key_count, debug_mode=debug_mode)


# Route pour le choix de l'équipe
@app.route('/team-choice', methods=['GET', 'POST'])
def teamChoice():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        # Vérifie si l'utilisateur ajoute encore un joueur ou s'il confirme l'équipe, et affecte la variable team_completed en fonction
        action = request.form['action']
        if action == "confirm-team":
            teamChoice.team_completed = True
        # On récupère le nom et la profession du joueur dans la variable player_name et player_job
        player_name = request.form.get('player-name')
        player_job = request.form.get('player-job')

        # On ajoute le joueur au fichier JSON avec la fonction dédiée (Par défaut on initialise is_leader à False)
        addToTeam(player_name,teamChoice.is_first_player,player_job)
        # On passe à False la variable qui vérifie si c'est le premier joueur
        teamChoice.is_first_player = False
    else:
        # On initialise la variable à False une première fois
        teamChoice.team_completed = False
        teamChoice.is_first_player = True

    # Récupère la liste des joueurs de l'équipe
    team = getTeam()
    player_indice = len(team) + 1

    return render_template('team-choice.html', team=team, player_indice=player_indice, team_completed=teamChoice.team_completed)



###### Routes pour les énigmes mathématiques ######

# Route pour l'énigme factorielle
@app.route("/math-challenge/factorial", methods=["POST","GET"])
def factorial():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        # On récupère la réponse de l'utilisateur (provenant du formulaire)
        # On converti sa réponse en entier, afin de pouvoir la comparer avec la réponse attendue par la fonction factorial
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        factorial.question, factorial.right_answer = factorialChallenge()

    return render_template("math_challenge_template/factorial.html", question=factorial.question, right_answer=factorial.right_answer, user_answer=user_answer)

# Route pour l'énigme d'équation linéaire
@app.route("/math-challenge/linear-equation", methods=["POST","GET"])
def linearEquation():
        # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
        # Si c'est le cas, il utilise la méthode POST
        if request.method == 'POST':
            user_answer = request.form.get("user-answer")
        # Sinon, il charge la page une première fois pour poser la question
        else:
            # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
            user_answer = None
            # Appelle de la fonction énigme associée
            # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
            linearEquation.question, linearEquation.right_answer = linearEquationChallenge()

        return render_template("math_challenge_template/linear-equation.html", question=linearEquation.question, right_answer=linearEquation.right_answer, user_answer=user_answer)


@app.route("/math-challenge/prime-number", methods=["POST","GET"])
def primeNumber():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        primeNumber.question, primeNumber.right_answer = primeNumberChallenge()

    return render_template("math_challenge_template/prime-number.html", question=primeNumber.question, right_answer=primeNumber.right_answer, user_answer=user_answer)

# Route pour l'énigme roulette mathématique
@app.route("/math-challenge/roulette", methods=['GET','POST'])
def roulette():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        roulette.question, roulette.right_answer = rouletteChallenge()

    return render_template("math_challenge_template/roulette.html", question=roulette.question, right_answer=roulette.right_answer, user_answer=user_answer)


# route pour l'énigme trouver le nombre premier
@app.route("/math-challenge/who-is-prime-number", methods=["POST","GET"])
def whoisprimeNumber():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        whoisprimeNumber.question, whoisprimeNumber.right_answer = findPrimeNumberChallenge()
    return render_template("math_challenge_template/who-is-prime.html", question=whoisprimeNumber.question, right_answer=whoisprimeNumber.right_answer, user_answer=user_answer)

# route pour l'énigme trouver le carré
@app.route("/math-challenge/what-the-square", methods=["POST","GET"])
def whatTheSquare():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        whatTheSquare.question, whatTheSquare.right_answer = squareChallenge()
    return render_template("math_challenge_template/what-the-square.html", question=whatTheSquare.question, right_answer=whatTheSquare.right_answer, user_answer=user_answer)


# route pour l'énigme trouver la racine carré
@app.route("/math-challenge/what-the-square-root", methods=["POST","GET"])
def whatTheSquareRoot():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        whatTheSquareRoot.question, whatTheSquareRoot.right_answer = squareRootChallenge()
    return render_template("math_challenge_template/what-the-square-root.html", question=whatTheSquareRoot.question, right_answer=whatTheSquareRoot.right_answer, user_answer=user_answer)

@app.route("/math-challenge/what-the-sequence", methods=["POST","GET"])
def whatTheSequence():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        whatTheSequence.question, whatTheSequence.right_answer = sequenceChallenge()
    return render_template("math_challenge_template/what-the-sequence.html", question=whatTheSequence.question, right_answer=whatTheSequence.right_answer, user_answer=user_answer)

@app.route("/math-challenge/is-the-equation-correct", methods=["POST","GET"])
def isTheEquationCorrect():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == "yes":
            user_answer = True
        else:
            user_answer = False

    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        isTheEquationCorrect.question, isTheEquationCorrect.right_answer = equalityChallenge()

    return render_template("math_challenge_template/is-the-equation-correct.html", question=isTheEquationCorrect.question, right_answer=isTheEquationCorrect.right_answer, user_answer=user_answer)


###### Routes pour les énigmes aléatoires ######


#Route pour l'énigmes pile ou face

@app.route("/random-challenge/Faces-or-Piles", methods=["POST","GET"])
def headsOrTails():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        choice = request.form['choice']
        if choice == "Pile":
            user_answer = "Pile"
        else:
            user_answer = "Face"
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
    else:
        user_answer = None

        #On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        headsOrTails.right_answer = coinChallenge()

    return render_template("/random_challenge_template/heads-or-tails.html", right_answer=headsOrTails.right_answer, user_answer=user_answer)


@app.route("/random-challenge/random-number", methods=["POST","GET"])
def randomNumber():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
        # On calcule la différence entre le résultat donné par le maitre et le joueur, avec la bonne valeur
        master_diff = abs(randomNumber.master_answer - randomNumber.right_answer)
        user_diff = abs(user_answer - randomNumber.right_answer)
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        master_diff = None
        user_diff = None
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        randomNumber.master_answer, randomNumber.right_answer = randomNumberChallenge()
    
    return render_template("/random_challenge_template/random-number.html", master_answer=randomNumber.master_answer,right_answer=randomNumber.right_answer, user_answer=user_answer, master_diff=master_diff, user_diff=user_diff)


# Route pour l'énigme bonneteaux
@app.route("/random-challenge/bonneteau", methods=['GET','POST'])
def bonneteau():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = request.form['user-answer']
        # On incrémente de 1 le compteur d'essai du joueur
        bonneteau.counter += 1
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # On initialise le compteur d'essai à 0
        bonneteau.counter = 0
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        bonneteau.bonneteaux_list, bonneteau.right_bonneteau = bonneteauChallenge()

    return render_template("random_challenge_template/bonneteau.html", bonneteaux_list=bonneteau.bonneteaux_list, right_answer=bonneteau.right_bonneteau, user_answer=user_answer, counter=bonneteau.counter)

# Route pour l'énigme de lancer de dés
@app.route("/random-challenge/dice-roll", methods=['GET','POST'])
def diceRoll():

    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        # On vérifie à qui était le tour précédent, et définie le prochain tour pour l'autre joueur
        if diceRoll.turn == 'player':
            diceRoll.turn = 'master'
            diceRoll.number_of_try += 1
        else:
            diceRoll.turn = 'player'
    # Sinon on charge une première fois la page en initialisant les variables
    else:
        diceRoll.number_of_try = 0
        diceRoll.turn = 'player'
    
    # On tire les dés à chaque tour
    roll = diceRollChallenge()

    return render_template("random_challenge_template/dice-roll.html", roll=roll, turn=diceRoll.turn, number_of_try=diceRoll.number_of_try)



##### Routes pour les énigmes de logique #####

# Route pour l'épreuve morpion
@app.route("/logic-challenges/tic-tac-toe", methods=['GET','POST'])
def ticTacToe():
    # On initialise la variable qui vérifie la victoire à None
    win = None
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form) ET si il vient de poser un symbole
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST' and hasattr(ticTacToe, 'pos_morpion'):
        # Récupère le mouvement du joueur depuis le formulaire
        player_move = request.form.getlist("cell")

        # On execute le code du jeu uniquement s'il n'y a pas d'erreur (la fonction renvoie True)
        if errorTicTacToe(player_move):
            error = None
            # Convertit la position du joueur en tuple pour la mise à jour de la grille
            player_move = tuple(map(int, player_move[0].split("-")))
            ticTacToe.pos_morpion = updateBoard(ticTacToe.pos_morpion, player_move, "player")
            # Vérifie si le joueur a gagné après son coup
            if isSol(ticTacToe.pos_morpion, "player"):
                win = "player"
            elif verifEgal(ticTacToe.pos_morpion):
                return redirect(url_for("ticTacToe"))  # Si égalité, recharge la page
            else:
                # Si le joueur n'a pas gagné, l'ordinateur joue
                master_move = masterMove()
                while ticTacToe.pos_morpion[master_move[0]][master_move[1]] != 0:
                    # Génère un nouveau coup si la case est déjà prise
                    master_move = masterMove() 
                ticTacToe.pos_morpion = updateBoard(ticTacToe.pos_morpion, master_move, "master")
                # Vérifie si l'ordinateur a gagné après son coup
                if isSol(ticTacToe.pos_morpion, "master"):
                    win = "master"

        else:
            error = "verif_player"

    else:
        # Si c'est la première fois qu'on charge la page, on initialise la grille 3x3 vide
        ticTacToe.pos_morpion = [[0 for j in range(3)] for i in range(3)]
        error = None

    # Rendu du template avec la grille, le gagnant et les erreurs éventuelles
    return render_template("logic_challenge_template/tic-tac-toe.html", pos_morpion=ticTacToe.pos_morpion, win=win, error=error)


# Route pour l'énigme bataille navale
@app.route("/logic-challenges/naval-battle", methods=['GET','POST'])
def navalBattle():

    # Vérifie si le formulaire a été soumis et si la variable 'moment_game' existe
    if request.method == 'POST' and hasattr(navalBattle, 'moment_game'):
        win = None
        if navalBattle.moment_game == "beginning":
            # Si le jeu commence, on récupère les positions des bateaux
            user_answer = request.form.getlist("cell")

            # On execute le code du jeu uniquement s'il n'y a pas d'erreur (la fonction renvoie True)
            if errorNavalBattle(user_answer, navalBattle.moment_game):
                # Change le moment du jeu à "middle"
                navalBattle.moment_game = "middle"
                navalBattle.bateaux = []

                # Ajoute les bateaux aux positions choisies
                for answer in user_answer:
                    navalBattle.bateaux.append(tuple(map(int, answer.split("-"))))
                # Réinitialise l'erreur
                navalBattle.error = None

            else:
                # Erreur si la configuration des bateaux est invalide
                navalBattle.error = "bateau"

        elif navalBattle.moment_game == "middle":
            # Lorsque le jeu est au milieu, on gère les tirs des deux joueurs
            user_answer = request.form.getlist("cell")

            # On execute le code du jeu uniquement s'il n'y a pas d'erreur (la fonction renvoie True)
            if errorNavalBattle(user_answer, navalBattle.moment_game):
                user_answer = tuple(map(int, user_answer[0].split("-")))
                navalBattle.liste_tir[user_answer] = navalBattleGame(navalBattle.bateaux_ordi, user_answer)

                # L'ordinateur fait un tir
                tir_ordi = tirOrdi(navalBattle.taille_grille)
                while tir_ordi in navalBattle.liste_tir_ordi:
                    # Assure que l'ordinateur ne tire pas deux fois au même endroit
                    tir_ordi = tirOrdi(navalBattle.taille_grille)
                navalBattle.liste_tir_ordi[tir_ordi] = navalBattleGame(navalBattle.bateaux, tir_ordi)

                # Vérifie si l'ordinateur ou le joueur a gagné
                winner_ordi = gagnant(navalBattle.liste_tir_ordi)
                winner = gagnant(navalBattle.liste_tir)

                # Détermine le gagnant
                win = whoWin(winner, winner_ordi)

                # Réinitialise les erreurs
                navalBattle.error = None
            else:
                # Erreur si le tir est invalide
                navalBattle.error = "tir"

    else:
        # On initialise toutes les variables du jeu au début
        navalBattle.taille_grille = 5 # Grille 5x5
        navalBattle.moment_game = "beginning"
        navalBattle.error = None
        navalBattle.toucher = None
        navalBattle.tir = None
        navalBattle.bateaux = None
        navalBattle.liste_tir = {}
        navalBattle.bateaux_ordi = bateauxOrdi([], navalBattle.taille_grille) # Place les bateaux de l'ordinateur
        navalBattle.liste_tir_ordi = {}
        win = None # Pas de gagnant au début

    # Rendu du template avec les données du jeu : taille de la grille, état du jeu, erreurs et résultats
    return render_template("logic_challenge_template/naval-battle.html", moment_game=navalBattle.moment_game, taille_grille=navalBattle.taille_grille, error=navalBattle.error, bateaux=navalBattle.bateaux, liste_tir=navalBattle.liste_tir, liste_tir_ordi=navalBattle.liste_tir_ordi, win=win)


##### Route pour l'énigme de Père Fouras ####

# Route pour l'épreuve du Père Fouras
@app.route("/pere-fouras-challenge", methods=['GET','POST'])
def pereFouras():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        # On récupère la réponse de l'utilisateur (provenant du formulaire)
        # On converti sa réponse en entier, afin de pouvoir la comparer avec la réponse attendue par la fonction factorial
        user_answer = request.form.get("user-answer").lower()
        # On incrémente le nombre d'essai
        pereFouras.number_of_try += 1
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # On initialise le nombre d'essai à 0
        pereFouras.number_of_try = 0 
        # Appelle de la fonction énigme associée
        # On enregistre les variables données par la fonction épreuve, sous forme d'attribut (pour pouvoir garder en mémoire leur contenu après rafraichissement de la page)
        pereFouras.question, pereFouras.right_answer = pereFourasChallenge()
        # Passe la réponse attendue en minuscules
        pereFouras.right_answer = pereFouras.right_answer

    return render_template("pere-fouras.html", question=pereFouras.question, right_answer=pereFouras.right_answer.lower(), user_answer=user_answer, number_of_try=pereFouras.number_of_try)


#### Route pour l'épreuve finale ####

# Route pour l'épreuve finale
@app.route("/final-challenge", methods=['GET','POST'])
def finalChallenge():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = request.form.get("user-answer").lower()
        finalChallenge.number_of_try += 1
        finalChallenge.number_of_clues += 1
    # Sinon on charge une première fois la page, en initialisant les variables
    else: 
        user_answer = None
        finalChallenge.keyCount = getKeyCounter()
        finalChallenge.number_of_clues = finalChallenge.keyCount
        finalChallenge.number_of_try = 0
        finalChallenge.code_word, finalChallenge.clues_list = final()

    return render_template("final_challenge_template/final-challenge.html", keyCount=finalChallenge.keyCount, code_word=finalChallenge.code_word.lower(), clues_list=finalChallenge.clues_list, number_of_clues=finalChallenge.number_of_clues, number_of_try=finalChallenge.number_of_try, user_answer=user_answer)

# Route pour accéder à la page qui précède la salle du trésor
@app.route("/before-treasure")
def beforeTreasure():
    return render_template("final_challenge_template/before-treasure.html")

# Route pour la salle du trésor
@app.route("/treasure-room")
def treasureRoom():
    return render_template("final_challenge_template/treasure-room.html")

# Route pour la fin du jeu
@app.route('/end-game', methods=['POST'])
def endGame():
    # On récupère le score du formulaire, et on met 0 par défaut
    score = request.form.get('score', 0)
    # On appelle la fonction qui permet de stocker toutes les données de la partie dans un fichier log
    storeGameData(score)
    return render_template('final_challenge_template/end-game.html', score=score)


# Route pour séléctionner le joueur pour la prochaine épreuve
@app.route("/next-player", methods=['GET','POST'])
def nextPlayer():
    # On vérifie si l'utilisateur charge la page après avoir répondu à la question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        # On récupère le joueur qui a été séléctionné
        selected_player = request.form['identity']
        # On incrémente le compteur d'épreuve passée du joueur
        addToPassedChallenges(selected_player)
    else:
        # On initialise la variable à None
        selected_player = None

    # On récupère la liste des joueurs
    team = getTeam()
    return render_template("next-player.html", team=team, selected_player=selected_player)


# Route pour accéder à la prochaine épreuve
@app.route("/next-challenge")
def nextChallenge():
    # On récupère le nombre d'épreuve restantes
    challenges_count = getChallengesCount()
    # On récupère le nombre de clé
    key_count = getKeyCounter()
    # Initialise la variable qui donne accès à l'épreuve finale à False, et si les joueurs ont cumulé +3 clés passe à True
    final_challenge_access = False
    if key_count >= 3:
        final_challenge_access = True

    return render_template("next-challenge.html", challenges_count=challenges_count,key_count=key_count, final_challenge_access=final_challenge_access)


# Route pour séléctionner une épreuve aléatoire parmi la catégorie spécifiée
@app.route("/random-challenge-selector")
def selectRandomChallenge():
    # On récupère la catégorie séléctionnée, en paramètre de l'URL
    challenge_type = request.args.get('challenge_type')
    # On incrémente le compteur du type d'épreuve
    addToChallengesCount(challenge_type)
    # On séléctionne une épreuve au hasard parmi la catégorie donnée, et on la stock dans la variable selected_challenge
    selected_challenge = chooseChallengeByType(challenge_type)

    # On renvoie l'url de l'épreuve séléctionnée
    return redirect(url_for(selected_challenge))

#Route pour afficher l'obtention d'une nouvelle clé
@app.route("/new-key")
def newKey():
    # On récupère le path d'une vidéo au hasard parmi le dossier video
    video_path = selectRandomVideo()
    # On récupère en paramètre de la requète le nombre de clé à ajouter aux joueurs
    key_number = int(request.args.get('key_number'))
    # On ajoute le nombre de clé au fichier JSON
    addToKeyCounter(key_number)
    return render_template('new-key.html', video_path=video_path)

# Route pour afficher la liste de toutes les énigmes disponibles dans le jeu
# Note : Ne sert que pour debug des énigmes, ou pour démo (pas utile dans le jeu)
@app.route("/challenges-list")
def challengesList():
     # Récupère dans la variable la liste de toutes les énigmes disponibles (du fichier JSON)
     challenges_list = getChallengesList()
     return render_template("/challenges-list.html", challenges_list=challenges_list)


@app.errorhandler(404)
def page_not_found(e):
    # Rendu d'une page HTML personnalisée pour l'erreur 404
    return render_template('/error_templates/404.html'), 404


if __name__ == "__main__":

    # On définit les arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", type=bool, default=False, help="Activer le mode debug")

    # On nalyse les arguments
    args = parser.parse_args()

    # Appelle de la fonction avec les paramètres obtenus
    app.run(debug=args.debug)