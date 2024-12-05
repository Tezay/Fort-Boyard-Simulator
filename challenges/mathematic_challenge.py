# Moduls import
from random import randint


##### Fonctions utiles #####

# Factorielle (sans utiliser le module factorial de la librairie math)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defind for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


##### Fonctions des énigmes mathématiques #####
# Pour chaque fonction :
# Entrée : Entier (entrée utilisateur)
# Sortie : Booléen (énime réussie ou pas), Entier (réponse donnée)

def factorialChallenge():
    number = randint(1,10)
    expected_answer = factorial(number)
    return number, expected_answer

def primeNumberChallenge():
    number = 14
    expected_answer = 17
    return number, expected_answer