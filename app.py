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
            user_answer = str(request.form.get("user-answer"))
        # Sinon, il charge la page une première fois pour poser la question
        else:
            # On initialise la réponse à None (car pas encore donnée par l'utilisateur)
            user_answer = None
            # Appelle de la fonction énigme associée
            # [compléter la docstring ici]
            linearEquation.question, linearEquation.right_answer = linearEquationChallenge()
            linearEquation.right_answer = str(linearEquation.right_answer)

        # Lignes de debug, cette énigme de fonctionne pas encore
        print("ANSWER TYPE :",type(linearEquation.right_answer), linearEquation.right_answer)
        print("USER ANSWER TYPE :",type(user_answer), user_answer)

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

    print(primeNumber.right_answer, type(primeNumber.right_answer), "|", primeNumber.question)
    return render_template("math_challenge_template/prime-number.html", question=primeNumber.question, right_answer=primeNumber.right_answer, user_answer=user_answer)

@app.route("/math-challenge/roulette")
def roulette():
        # Appelle de la fonction équation linéaire associée
        question, right_answer = rouletteChallenge()
        return render_template("math_challenge_template/roulette.html", question = question, right_answer = right_answer)



###### Routes pour les énigmes aléatoires ######

# Route pour l'énigme bonneteaux
@app.route("/random-challenge/bonneteau", methods=['GET','POST'])
def bonneteau():
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
        bonneteau.bonneteaux_list, bonneteau.right_bonneteau = bonneteauChallenge()

    return render_template("random_challenge_template/bonneteau.html", bonneteaux_list=bonneteau.bonneteaux_list, right_answer=bonneteau.right_bonneteau, user_answer=user_answer)


# Routes pour les énigmes de logique

# Route pour l'énigme bataille navale
@app.route("/logic-challenges/naval-battle", methods=['GET','POST'])
def navalBattle():

    if request.method == 'POST':
        if navalBattle.moment_game == "beginning":
            user_answer = request.form.getlist("cell")
            if len(user_answer) == 4:
                navalBattle.moment_game = "game"
                navalBattle.error = None
            else:
                navalBattle.error = "batteau"
    else:
        navalBattle.moment_game = "beginning"
        navalBattle.error = None

    return render_template("logic_challenge_template/naval-battle.html", moment_game=navalBattle.moment_game, error = navalBattle.error)


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