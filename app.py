from flask import Flask, render_template, request, redirect, url_for, abort, session
from select_next_challenge import chooseRandomChallenge, getChallengesListByType
from challenges import *
from utils import *

app = Flask(__name__)


#Route du menu principal
@app.route("/")
def menu():
    # Appelle la fonction qui permet de réinitialiser le nombre de clés
    resetKeyCounter()
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


# Routes pour les énigmes de logique

# Route pour l'énigme bonneteaux
@app.route("/logic-challenges/naval-battle", methods=['GET','POST'])
def navalBattle():

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
    # Sinon, il charge la page une première fois pour poser la question
    else:
        # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
        user_answer = None
        # Appelle de la fonction énigme associée
        # [compléter la docstring ici]
        pereFouras.question, pereFouras.right_answer = pereFourasChallenge()
        # Passe la réponse attendue en minuscules
        pereFouras.right_answer = pereFouras.right_answer

    return render_template("pere-fouras.html", question=pereFouras.question, right_answer=pereFouras.right_answer, user_answer=user_answer)


#Route pour créer une nouvelle connaissance
@app.route("/next-challenge")
def nextChallenge():
    chosen_challenge = chooseRandomChallenge()
    print(f"CHOSEN CHALLENGE : {chosen_challenge}")
    return redirect(url_for(chosen_challenge))


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
     challenges_list = getChallengesListByType()
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