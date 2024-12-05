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

#Verifier si le nombre est premier
def isPrime(n):
    is_prime = True
    i = 2
    if n <= 1:
        is_prime = False
    else:
        while is_prime and i < n:
            if n % i == 0:
                is_prime = False
            else:
                i += 1
    return is_prime

#Quelle est le nombre premier le plus proche d'un nombre
def nearestPrimeNumber(n):
    found = false
    if isPrime(n):
        return n
    i = 1
    while found == false:
        if isPrime(n+i) == True:
            prime_number = n + i
            found = True
        else:
            i += 1
    return prime_number


##### Fonctions des énigmes mathématiques #####
# Pour chaque fonction :
# Entrée : Entier (entrée utilisateur)
# Sortie : Booléen (énime réussie ou pas), Entier (réponse donnée)

def factorialChallenge():
    number = randint(1,10)
    expected_answer = factorial(number)
    return number, expected_answer

def primeNumberChallenge():
    number = randint(10,20)
    expected_answer = nearestPrimeNumber(number)
    return number, expected_answer