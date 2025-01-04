# Moduls import
import random

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
        five_number.append(random.randint(1, 20))
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
    if n ==int(n):
        Integer = True
    else:
        Integer = False
    return Integer

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

#Quel est son carré
def squareOfWhat():
    number = random.randint(1, 50)
    squared_number = squareNum(number)
    return number , squared_number

#Quel est sa racine carré
def squareRootOfWhat():
    squared_number = 1.5
    while isInteger(squared_number) == False:
        number = random.randint(1, 100)
        squared_number = squareRoot(number)

    return number, squared_number

def valueSequence():
    U0 = random.randint(-25, 25)
    r = random.randint(-10,10)
    return U0, r

def sequence(U0, r):
    sequence = []
    operator = randomOperator()
    for n in range(6):
        if operator == "+" or operator == "-":
            number = U0 + r*n
        elif operator == "*":
            number = U0 * r ** n
        sequence.append(number)
    return sequence

def sequenceNumber(sequence):
    show_sequence = sequence[0:-1]
    number = sequence[-1]
    return number , show_sequence


def equality():
    number1 = random.randint(-25, 25)
    number2 = random.randint(-25, 25)
    operator = randomOperator()
    return number1, number2 ,operator

def equalityResult(number1,number2,operator):
    if operator == "+":
        right_result = number1 + number2
    elif operator == "-":
        right_result = number1 - number2
    elif operator == "*":
        right_result = number1 * number2
    result_liste = [random.randint(right_result-10,right_result+10),right_result]
    return right_result, random.choice(result_liste)

def equalityAnswer(right_result,result):
    if right_result == result:
        return True
    else:
        return False
    
# Fonction pour faire le PGCD de deux nombres
def findPgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

##### Fonctions des énigmes mathématiques #####
# Pour chaque fonction :
# Sortie : Booléen (énigme réussie ou pas), Entier (réponse donnée)

def equalityChallenge():
    number1 , number2, operator = equality()
    right_result, result = equalityResult(number1,number2,operator)
    question = f"{number1}{operator}{number2} = {result}"
    right_answer = equalityAnswer(right_result, result)
    return question, right_answer


def sequenceChallenge():
    U0, r = valueSequence()
    number = random.randint(4,20)
    entire_sequence = sequence(U0, r)
    right_answer, question = sequenceNumber(entire_sequence)
    return question, right_answer

def factorialChallenge():
    question = random.randint(1,10)
    right_answer = factorial(question)
    return question, right_answer

def primeNumberChallenge():
    question = random.randint(10,20)
    right_answer = nearestPrimeNumber(question)
    return question, right_answer

def linearEquationChallenge():
    # Générer les coefficients a et b
    a = random.randint(1, 10)
    b = 0
    while b == 0:
        b = random.randint(-10, 10)

    # Calculer la solution exacte
    solution_exacte = -b / a

    # Construire une liste de réponses acceptables
    right_answer = []

    pgcd = findPgcd(a, -b)
    print(pgcd)
    if pgcd != 1:
        right_answer.append(f"{b//pgcd}/{-a//pgcd}")
        right_answer.append(f"{-b//pgcd}/{a//pgcd}")

    if a//pgcd == 1 or a//pgcd == -1:
        right_answer.append(f"{-(a//pgcd)*b//pgcd}")

    # Ajouter la fraction exacte sous forme de chaîne
    right_answer.append(f"{-b}/{a}")
    right_answer.append(f"{b}/{-a}")

    # Ajouter la version décimale avec arrondi à différentes précisions
    for precision in range(1, 10):  # On arrondit jusqu'à 3 décimales
        arrondi = round(solution_exacte, precision)
        right_answer.append(f"{arrondi}".replace(".", ","))  # Format français avec virgule
        right_answer.append(f"{arrondi}")  # Format anglais avec point
    print(right_answer)
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

def squareRootChallenge():
    question, right_answer = squareRootOfWhat()
    return question, right_answer