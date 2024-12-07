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
@app.route("/math-challenge/factorial")
def factorial():
    # Vérifie si l'utilisateur vient d'une redirection
    if request.args.get('via_redirect'):
        # Appel de la fonction challenge factorielle
        # La fonction renvoie number:int (le nombre dont on cherche la factorielle) et expected_answer:int (la réponse attendue)
        number, expected_answer = factorialChallenge()
        # Renvoie la page HTML de l'énigme factorielle
        # Transmet en paramètres les variables number:int et expected_answer:int
        return render_template("math_challenge_template/factorial.html", number=number, expected_answer=expected_answer)
    else:
        # Renvoie à la page d'accueil si l'utilisateur accède à la page autrement que via une redirection (méthode utilisée par le jeu)
        return redirect(url_for('menu'))

# Route pour l'énigme d'équation linéaire
@app.route("/math-challenge/linear-equation")
def linearEquation():
    # Vérifie si l'utilisateur vient d'une redirection
    if request.args.get('via_redirect'):
        # Call de la fonction challenge associée
        return render_template("math_challenge_template/linear-equation.html")
    else:
        return redirect(url_for('menu'))


@app.route("/math-challenge/prime-number")
def primeNumber():
    number, expected_answer = primeNumberChallenge()
    return render_template("math_challenge_template/prime-number.html", number=number, expected_answer=expected_answer)


###### Routes pour les énigmes aléatoires ######

# Route pour l'énigme bonneteaux
@app.route("/random-challenge/bonneteau")
def bonneteau():
    bonneteaux_list, right_bonneteau = bonneteauChallenge()
    return render_template("random_challenge_template/bonneteau.html", bonneteaux_list=bonneteaux_list, right_bonneteau=right_bonneteau)


#Route pour créer une nouvelle connaissance
@app.route("/next-challenge", methods=["POST","GET"])
def nextChallenge():
    chosen_challenge = chooseRandomChallenge()
    print(f"CHOSEN CHALLENGE : {chosen_challenge}")
    return redirect(url_for(chosen_challenge, via_redirect=True))


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