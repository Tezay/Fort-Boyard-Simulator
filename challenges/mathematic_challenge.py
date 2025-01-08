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
#vérification que le nombre ne soit ni 0 ni 1
    if n <= 1:
        is_prime = False
#vérification que le nombre est premier
    else:
        while is_prime and i < squareRoot(n):
            if n % i == 0:
                is_prime = False
            else:
                i += 1
    return is_prime

#Quel est le nombre premier le plus proche d'un nombre
def nearestPrimeNumber(n):
    found = False
#vérification que le nombre donné ne soit pas premier
    if isPrime(n):
        return n
#incremantation pour trouver le nombre premier supérieur le plus proche
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
#ajout de 5 nombres aléatoire
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
#verification de quel opérateur
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

    #ajout de 5 nombres aléatoires qui ne sont pas premier à la liste 5 nombres valides
    for n in range(5):
        five_valid_numbers.append(random.choice(valid_numbers))
    #ajout du nombre premier aléatoire à la liste de la question
    numbers_list.append(prime_number)
    #ajout des 5 nombres aléatoires dans la liste question
    for number in five_valid_numbers:
        numbers_list.append(number)
    #mélange des éléments de la liste
    random.shuffle(numbers_list)
    return numbers_list , prime_number

#Quel est son carré
def squareOfWhat():
    number = random.randint(2, 25)
    squared_number = squareNum(number)
    return number , squared_number

#Quelle est sa racine carré
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
    #Suite arythmétique
    for n in range(6):
        if operator == "+" or operator == "-":
            #Formule de Un Suite arythmétique
            number = U0 + r*n
    #Suite géométrique
        elif operator == "*":
            #Formule de Un Suite géométrique
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
    #vérification de l'op
    if operator == "+":
        right_result = number1 + number2
    elif operator == "-":
        right_result = number1 - number2
    elif operator == "*":
        right_result = number1 * number2
    #liste entre le résultat et un nb aléatoire proche du résultat
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

# Fonction pour l'épreuve vérification d'une égalité
def equalityChallenge():
    # Appel des fonctions utiles
    number1 , number2, operator = equality()
    right_result, result = equalityResult(number1,number2,operator)
    # Question et Réponse du Challenge
    question = f"{number1}{operator}{number2} = {result}"
    right_answer = equalityAnswer(right_result, result)
    return question, right_answer

# Fonction pour l'épreuve deviner la suite
def sequenceChallenge():
    # Appel des fonctions utiles
    U0, r = valueSequence()
    number = random.randint(4,20)
    entire_sequence = sequence(U0, r)
    # Question et Réponse du Challenge
    right_answer, question = sequenceNumber(entire_sequence)
    return question, right_answer

# Fonction pour l'épreuve trouver la factorielle
def factorialChallenge():
    # Question et Réponse du Challenge
    question = random.randint(1,10)
    right_answer = factorial(question)
    return question, right_answer

# Fonction pour l'épreuve deviner le nombre premier le plus proche
def primeNumberChallenge():
    # Question et Réponse du Challenge
    question = random.randint(10,20)
    right_answer = nearestPrimeNumber(question)
    return question, right_answer

# Fonction pour l'épreuve de résolution de l'équation linéaire
def linearEquationChallenge():
    # Générer les coefficients a et b
    a = random.randint(1, 10)
    b = 0
    while b == 0:
        b = random.randint(-10, 10)

    # On calcule la solution exacte
    solution_exacte = -b / a
    # On construit une liste des réponses acceptables
    right_answer = []
    # On calcule le PGCD(a,b)
    pgcd = findPgcd(a, -b)

    # On vérifie si le dénominateur vaut -1 ou 1, et on simplifie la réponse si c'est le cas
    if a//pgcd == 1 or a//pgcd == -1:
        right_answer.append(f"{-(a//pgcd)*b//pgcd}")

    # On vérifie si la fraction est réductible, donc si PGCD(numérateur,dénominateur) est différent de 1
    if pgcd != 1 or pgcd != -1:
        right_answer.append(f"{-b//pgcd}/{a//pgcd}")
        right_answer.append(f"{b//pgcd}/{-a//pgcd}")

    # On ajoute la fraction exacte sous forme de chaîne
    right_answer.append(f"{-b}/{a}")
    right_answer.append(f"{b}/{-a}")

    # On ajoute la version décimale avec arrondi à différentes précisions
    for precision in range(1, 10):  # On arrondit jusqu'à 3 décimales
        arrondi = round(solution_exacte, precision)
        right_answer.append(f"{arrondi}".replace(".", ","))  # Format français avec virgule
        right_answer.append(f"{arrondi}")  # Format anglais avec point

    # On rajoute un (+) si b positif, sinon on laisse le (-)
    if b > 0:
        b = f"+{b}"
    else:
        b = f"{b}"

    question = {'a': a, 'b': b}

    return question, right_answer

# Fonction pour l'épreuve roulette 
def rouletteChallenge():
    # Appel des fonctions utiles
    numbers_list = fiveNumbersRandom()
    operator = randomOperator()
    # Question et Réponse du Challenge
    right_answer = rouletteMath(operator, numbers_list)
    question = {"numbers_list":numbers_list, "operator":operator}
    return question, right_answer

def findPrimeNumberChallenge():
    # Appel de la fonction utile
    numbers_list, prime_number = whoIsPrime()
    # Question et Réponse du Challenge
    question = numbers_list
    right_answer = prime_number
    return question, right_answer

def squareChallenge():
    # Question et Réponse du Challenge
    question, right_answer = squareOfWhat()
    return question, right_answer

def squareRootChallenge():
    # Question et Réponse du Challenge
    question, right_answer = squareRootOfWhat()
    return question, right_answer