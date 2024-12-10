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
    found = False
    if isPrime(n):
        return n
    i = 1
    while found == False:
        if isPrime(n+i) == True:
            prime_number = n + i
            found = True
        else:
            i += 1
    return prime_number


# Creation de 5 nombre aléatoire
def fiveNumbersRandom():
    five_number = []
    for i in range(5):
        five_number[i] = randint(1, 20)
    return five_number

#Choix d'un opérateur aléatoire
def randomOperator():
    # 1 = + ; 2 = - ; 3 = *
    operator = randint(1, 3)
    return operator

#Roulette mathématique
def rouletteMath():
    numbers = fiveNumbersRandom()
    operator = randomOperator() # 1 = + ; 2 = - ; 3 = *
    if operator == 1:
        result = 0
        for i in numbers:
            result = result + i
    if operator == 2:
        result = 0
        for i in numbers:
            result = result - i
    if operator == 3:
        result = 1
        for i in numbers:
            result = result * i
    return result


##### Fonctions des énigmes mathématiques #####
# Pour chaque fonction :
# Sortie : Booléen (énigme réussie ou pas), Entier (réponse donnée)

def factorialChallenge():
    number = randint(1,10)
    expected_answer = factorial(number)
    return number, expected_answer

def primeNumberChallenge():
    number = randint(10,20)
    expected_answer = nearestPrimeNumber(number)
    return number, expected_answer

def linearEquationChallenge():
    a , b = randint(1,10), randint(1,10)
    expected_answer = -b/a
    question = {'a': a, 'b': b}
    return question, expected_answer

def mathematicalRouletteChallenge():
    question_list = fiveNumbersRandom()
    operator = randomOperator()
    expected_answer = rouletteMath()
    return question_list, operator, expected_answer