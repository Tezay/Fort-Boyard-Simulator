# Moduls import
import random
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
        while is_prime and i < squareRoot(n):
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
    for nb in range(5):
        five_number.append(randint(1, 20))
    return five_number

#Choix d'un opérateur aléatoire
def randomOperator():
    operators_list = ["+","-","*"]
    return random.choice(operators_list)

# Roulette mathématique
def rouletteMath(operator, numbers_list):
    result = numbers_list[0]
    if operator == "+":
        for i in numbers_list[1:]:
            result += i
        return result
    elif operator == "-":
        for i in numbers_list[1:]:
            result -= i
        return result
    elif operator == "*":
        for i in numbers_list[1:]:
            result *= i
        return result
    else:
        return None

# carre d'un nombre
def squareNum(n):
    return n*n

# racine carre d'un nombre
def squareRoot(n):
    return n**(1/2)

#verification si le nombre est entier ou non
def isInteger(n):
    return n == int(n)

#choix d'un nombre premier
def randomPrimeNumber():
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19]
    return random.choice(prime_number)

# Quel est le nombre premier
def whoIsPrime():
    #Variable
    numbers_list = []
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    prime_number = randomPrimeNumber()
    valid_numbers = [i for i in range(21) if i not in prime_numbers]
    five_valid_numbers = []

    #ajout de 5 nombre aleatoire qui ne sont pas premier a la liste 5 nombre valide
    for n in range(5):
        five_valid_numbers.append(random.choice(valid_numbers))
    #ajout du nombre premier aleatoir a la liste de la question
    numbers_list.append(prime_number)
    #ajout des 5 nombre aleatoire dans la liste question
    for number in five_valid_numbers:
        numbers_list.append(number)
    #melange des éléments de la liste
    random.shuffle(numbers_list)
    return numbers_list , prime_number

#Quel est sont nombres premier
def squareOfWhat():
    number = random.randint(1, 20)
    squared_number = squareNum(number)
    return number , squared_number

##### Fonctions des énigmes mathématiques #####
# Pour chaque fonction :
# Sortie : Booléen (énigme réussie ou pas), Entier (réponse donnée)

def factorialChallenge():
    question = randint(1,10)
    right_answer = factorial(question)
    return question, right_answer

def primeNumberChallenge():
    question = randint(10,20)
    right_answer = nearestPrimeNumber(question)
    return question, right_answer

def linearEquationChallenge():
    # Générer les coefficients a et b
    a = randint(1, 10)
    b = 0
    while b == 0:
        b = random.randint(-10, 10)

    # Calculer la solution exacte
    solution_exacte = -b / a

    # Construire une liste de réponses acceptables
    right_answer = []

    # Ajouter la fraction exacte sous forme de chaîne
    right_answer.append(f"{-b}/{a}")

    # Ajouter la version décimale avec arrondi à différentes précisions
    for precision in range(1, 10):  # On arrondit jusqu'à 3 décimales
        arrondi = round(solution_exacte, precision)
        right_answer.append(f"{arrondi}".replace(".", ","))  # Format français avec virgule
        right_answer.append(f"{arrondi}".replace(",", "."))  # Format anglais avec point

    # Ajouter une marge d'erreur pour les réponses proches
    marge_erreur = 0.005
    for delta in [-marge_erreur, marge_erreur]:
        valeur_proche = solution_exacte + delta
        valeur_proche_arrondie = round(valeur_proche, 2)  # Arrondi à 2 décimales
        right_answer.append(f"{valeur_proche_arrondie}".replace(".", ","))
        right_answer.append(f"{valeur_proche_arrondie}".replace(",", "."))

    b = f"+{b}" if b > 0 else f"{b}"
    question = {'a': a, 'b': b}

    return question, right_answer


def rouletteChallenge():
    numbers_list = fiveNumbersRandom()
    operator = randomOperator()
    right_answer = rouletteMath(operator, numbers_list)
    question = {"numbers_list":numbers_list, "operator":operator}
    return question, right_answer

def findPrimeNumberChallenge():
    numbers_list, prime_number = whoIsPrime()
    question = numbers_list
    right_answer = prime_number
    return question, right_answer

def squareChallenge():
    question, right_answer = squareOfWhat()
    return question, right_answer