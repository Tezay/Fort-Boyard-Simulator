from flask import Flask, render_template, request, redirect, url_for, abort, session
from challenges import *
from utils import *

app = Flask(__name__)


#Route du menu principal
@app.route("/")
def menu():
    # Appelle la fonction qui permet de réinitialiser le nombre de clés
    resetKeyCounter()
    # Appelle la fonction qui permet fe réinitialiser la composition de l'équipe
    resetTeam()
    return render_template("index.html")


# Route pour le Fort Boyard
@app.route("/fort-boyard")
def fortBoyard():
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

    if request.method == 'POST':
        # Vérifie si l'utilisateur ajoute encore un joueur ou s'il confirme l'équipe, et affecte la variable team_completed en fonction
        action = request.form['action']
        if action == "confirm-team":
            teamChoice.team_completed = True
        # On récupère le nom et la profession du joueur dans la variable player_name et player_job
        player_name = request.form.get('player-name')
        player_job = request.form.get('player-job')

        # On ajoute le joueur au fichier JSON avec la fonction dédiée (Par défaut on initialise is_leader à False)
        addToTeam(player_name,False,player_job)
    else:
        # On initialise la variable à False une première fois
        teamChoice.team_completed = False

    # Récupère la liste des joueurs de l'équipe
    team = getTeam()
    player_indice = len(team) + 1

    return render_template('team-choice.html', team=team, player_indice=player_indice, team_completed=teamChoice.team_completed)



###### Routes pour les énigmes mathématiques ######

# Route pour l'énigme factorielle
@app.route("/math-challenge/factorial", methods=["POST","GET"])
def factorial():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
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
        # [compléter la docstring ici]
        factorial.question, factorial.right_answer = factorialChallenge()

    return render_template("math_challenge_template/factorial.html", question=factorial.question, right_answer=factorial.right_answer, user_answer=user_answer)

# Route pour l'énigme d'équation linéaire
@app.route("/math-challenge/linear-equation", methods=["POST","GET"])
def linearEquation():
        # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
        # Si c'est le cas, il utilise la méthode POST
        if request.method == 'POST':
            user_answer = request.form.get("user-answer")
        # Sinon, il charge la page une première fois pour poser la question
        else:
            # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
            user_answer = None
            # Appelle de la fonction énigme associée
            # [compléter la docstring ici]
            linearEquation.question, linearEquation.right_answer = linearEquationChallenge()

        return render_template("math_challenge_template/linear-equation.html", question=linearEquation.question, right_answer=linearEquation.right_answer, user_answer=user_answer)


@app.route("/math-challenge/prime-number", methods=["POST","GET"])
def primeNumber():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        primeNumber.question, primeNumber.right_answer = primeNumberChallenge()

    return render_template("math_challenge_template/prime-number.html", question=primeNumber.question, right_answer=primeNumber.right_answer, user_answer=user_answer)

# Route pour l'énigme roulette mathématique
@app.route("/math-challenge/roulette", methods=['GET','POST'])
def roulette():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        roulette.question, roulette.right_answer = rouletteChallenge()

    return render_template("math_challenge_template/roulette.html", question=roulette.question, right_answer=roulette.right_answer, user_answer=user_answer)


# route pour l'énigme trouver le nombre premier
@app.route("/math-challenge/who-is-prime-number", methods=["POST","GET"])
def whoisprimeNumber():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        whoisprimeNumber.question, whoisprimeNumber.right_answer = findPrimeNumberChallenge()
    return render_template("math_challenge_template/who-is-prime.html", question=whoisprimeNumber.question, right_answer=whoisprimeNumber.right_answer, user_answer=user_answer)

# route pour l'énigme trouver le carré
@app.route("/math-challenge/what-the-square", methods=["POST","GET"])
def whatTheSquare():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        whatTheSquare.question, whatTheSquare.right_answer = squareChallenge()
    return render_template("math_challenge_template/what-the-square.html", question=whatTheSquare.question, right_answer=whatTheSquare.right_answer, user_answer=user_answer)


# route pour l'énigme trouver la racine carré
@app.route("/math-challenge/what-the-square-root", methods=["POST","GET"])
def whatTheSquareRoot():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        whatTheSquareRoot.question, whatTheSquareRoot.right_answer = squareRootChallenge()
    return render_template("math_challenge_template/what-the-square-root.html", question=whatTheSquareRoot.question, right_answer=whatTheSquareRoot.right_answer, user_answer=user_answer)

@app.route("/math-challenge/what-the-sequence", methods=["POST","GET"])
def whatTheSequence():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = int(request.form.get("user-answer"))
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        whatTheSequence.question, whatTheSequence.right_answer = sequenceChallenge()
    return render_template("math_challenge_template/what-the-sequence.html", question=whatTheSequence.question, right_answer=whatTheSequence.right_answer, user_answer=user_answer)

@app.route("/math-challenge/is-the-equation-correct", methods=["POST","GET"])
def isTheEquationCorrect():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        choice = request.form['choice']
        question , right_answer= equalityChallenge()
        if choice == "yes":
            user_answer = True
        elif choice == "no":
            user_answer = False
        else:
            user_answer = None

    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        isTheEquationCorrect.question, isTheEquationCorrect.right_answer = equalityChallenge()
    return render_template("math_challenge_template/is-the-equation-correct.html", question=isTheEquationCorrect.question, right_answer=isTheEquationCorrect.right_answer, user_answer=user_answer)


###### Routes pour les énigmes aléatoires ######

# Route pour l'énigme bonneteaux
@app.route("/random-challenge/bonneteau", methods=['GET','POST'])
def bonneteau():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
    # Si c'est le cas, il utilise la méthode POST
    if request.method == 'POST':
        user_answer = request.form.get("user-answer").lower()
        # On incrémente de 1 le compteur d'essai du joueur
        bonneteau.counter += 1
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # On initialise le compteur d'essai à 0
        bonneteau.counter = 0
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        bonneteau.bonneteaux_list, bonneteau.right_bonneteau = bonneteauChallenge()

    return render_template("random_challenge_template/bonneteau.html", bonneteaux_list=bonneteau.bonneteaux_list, right_answer=bonneteau.right_bonneteau, user_answer=user_answer, counter=bonneteau.counter)

# Route pour l'énigme de lancer de dés
@app.route("/random-challenge/dice-roll", methods=['GET','POST'])
def diceRoll():

    # Structure de l'énigme à optimiser

    if request.method == 'POST':
        # On vérifie à qui était le tour précédent, et définie le prochain tour pour l'autre joueur
        if diceRoll.turn == 'player':
            diceRoll.turn = 'master'
            diceRoll.number_of_try += 1
        else:
            diceRoll.turn = 'player'
    
    else:
        diceRoll.number_of_try = 0
        diceRoll.turn = 'player'
    
    # On tire les dés à chaque tour
    roll = diceRollChallenge()

    return render_template("random_challenge_template/dice-roll.html", roll=roll, turn=diceRoll.turn, number_of_try=diceRoll.number_of_try)



# Routes pour les énigmes de logique

# Route pour l'énigme bonneteaux
@app.route("/logic-challenges/naval-battle", methods=['GET','POST'])
def navalBattle():

    # On vérifie si l'utilisateur charge la page après avoir répondu au questionnaire ET qu'il 
    if request.method == 'POST' and hasattr(navalBattle, 'moment_game'):
        if navalBattle.moment_game == "beginning":
            win = None
            user_answer = request.form.getlist("cell")

            if errorNavalBattle(user_answer, navalBattle.moment_game):
                navalBattle.moment_game = "middle"
                navalBattle.bateaux = []

                for answer in user_answer:
                    navalBattle.bateaux.append(tuple(map(int, answer.split("-"))))
                navalBattle.error = None

            else:
                navalBattle.error = "bateau"

        elif navalBattle.moment_game == "middle":
            user_answer = request.form.getlist("cell")

            if errorNavalBattle(user_answer, navalBattle.moment_game):
                user_answer = tuple(map(int, user_answer[0].split("-")))
                navalBattle.liste_tir[user_answer] = navalBattleGame(navalBattle.bateaux_ordi, user_answer)

                tir_ordi = tirOrdi()
                while tir_ordi in navalBattle.liste_tir_ordi:
                    tir_ordi = tirOrdi()
                navalBattle.liste_tir_ordi[tir_ordi] = navalBattleGame(navalBattle.bateaux, tir_ordi)
                print(navalBattle.liste_tir_ordi)
                winner_ordi = gagnant(navalBattle.liste_tir_ordi)

                winner = gagnant(navalBattle.liste_tir)

                win = whoWin(winner, winner_ordi)

                navalBattle.error = None
            else:
                navalBattle.error = "tir"

    else:
        navalBattle.moment_game = "beginning"
        navalBattle.error = None
        navalBattle.toucher = None
        navalBattle.tir = None
        navalBattle.bateaux = None
        navalBattle.liste_tir = {}
        navalBattle.bateaux_ordi = bateauxOrdi([])
        navalBattle.liste_tir_ordi = {}
        win = None


    return render_template("logic_challenge_template/naval-battle.html", moment_game=navalBattle.moment_game, error=navalBattle.error, bateaux=navalBattle.bateaux, liste_tir=navalBattle.liste_tir, liste_tir_ordi=navalBattle.liste_tir_ordi, win=win)


##### Route pour l'énigme de Père Fouras ####

@app.route("/pere-fouras-challenge", methods=['GET','POST'])
def pereFouras():
    # On vérifie si l'utilisateur charge la page après avoir répondu à a question (form)
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
        # [compléter la docstring ici]
        pereFouras.question, pereFouras.right_answer = pereFourasChallenge()
        # Passe la réponse attendue en minuscules
        pereFouras.right_answer = pereFouras.right_answer

    return render_template("pere-fouras.html", question=pereFouras.question, right_answer=pereFouras.right_answer, user_answer=user_answer, number_of_try=pereFouras.number_of_try)


#### Route pour l'épreuve finale ####

@app.route("/final-challenge", methods=['GET','POST'])
def finalChallenge():

    if request.method == 'POST':
        user_answer = request.form.get("user-answer").lower()
        finalChallenge.number_of_try += 1
        finalChallenge.number_of_clues += 1

    else: 
        user_answer = None
        finalChallenge.keyCount = getKeyCounter()
        finalChallenge.number_of_clues = finalChallenge.keyCount
        finalChallenge.number_of_try = 0
        finalChallenge.code_word, finalChallenge.clues_list = final()
        print(finalChallenge.code_word)

    return render_template("final_challenge_template/final-challenge.html", keyCount=finalChallenge.keyCount, code_word=finalChallenge.code_word, clues_list=finalChallenge.clues_list, number_of_clues=finalChallenge.number_of_clues, number_of_try=finalChallenge.number_of_try, user_answer=user_answer)

@app.route("/treasure-room")
def treasureRoom():
    return render_template("final_challenge_template/treasure-room.html")


# Route pour séléctionner le joueur pour la prochaine épreuve
@app.route("/next-player", methods=['GET','POST'])
def nextPlayer():
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
# A TERMINER (il est 2h du mat mieux vaut aller dormir...)
@app.route("/next-challenge")
def nextChallenge():
    challenges_count = getChallengesCount()
    remaining_challenges_counter = getRemainingChallengesCounter()
    key_count = getKeyCounter()
    # Initialise la variable qui donne accès à l'épreuve finale à False, et si les joueurs ont cumulé +3 clés passe à True
    final_challenge_access = False
    if key_count >= 3:
        final_challenge_access = True

    return render_template("next-challenge.html", challenges_count=challenges_count,remaining_challenges_counter=remaining_challenges_counter,key_count=key_count, final_challenge_access=final_challenge_access)


#Route pour afficher l'obtention d'une nouvelle clé
@app.route("/new-key")
def newKey():
    key_number = int(request.args.get('key_number'))
    addToKeyCounter(key_number)
    return render_template('new-key.html')

# Route pour afficher la liste de toutes les énigmes disponibles dans le jeu
# Note : Ne sert que pour debug des énigmes, ou pour démo (pas utile dans le jeu)
@app.route("/challenges-list")
def challengesList():
     # Récupère dans la variable la liste de toutes les énigmes disponibles (du fichier JSON)
     challenges_list = getChallengesList()
     return render_template("/challenges-list.html", challenges_list=challenges_list)


# Gestionnaire d'erreur
@app.errorhandler(403)
def page_forbidden(e):
    # Rendu d'une page HTML personnalisée
    return render_template('/error_templates/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    # Rendu d'une page HTML personnalisée pour l'erreur 404
    return render_template('/error_templates/404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)