from flask import Flask, render_template, request, redirect, url_for, abort, session
from select_next_challenge import chooseRandomChallenge
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
    #Renvoie la page HTML du Fort Boyard (salle où les joueurs reviennent après chaque épreuve)
    # Transmet en paramètre la variable key_count:int (pour afficher le nombre de clés obtenues)
    return render_template("fort-boyard.html", key_count=key_count)


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
@app.route("/math-challenge/linear-equation")
def linearEquation():
        # Appelle de la fonction équation linéaire associée
        question, expected_answer = linearEquationChallenge()
        return render_template("math_challenge_template/linear-equation.html", question=question, expected_answer=expected_answer)


@app.route("/math-challenge/prime-number")
def primeNumber():
    number, expected_answer = primeNumberChallenge()
    return render_template("math_challenge_template/prime-number.html", number=number, expected_answer=expected_answer)

@app.route("/math-challenge/roulette")
def roulette():
        # Appelle de la fonction équation linéaire associée
        question , expected_answer = rouletteChallenge()
        return render_template("math_challenge_template/roulette.html", question = question, expected_answer = expected_answer)



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