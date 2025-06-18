import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4

def poser_question():
    nbr_a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nbr_b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)

    operateur = "+"
    if o == 1:
        operateur = "*"

    question = input(f"Calculer : {nbr_a} {operateur} {nbr_b} = ")

    calcul = nbr_a+nbr_b
    if o == 1:
        calcul = nbr_a*nbr_b
    if int(question) == calcul:
        #print("Correcte")
        return True
    """else:
        print("Incorrecte")"""
    return False

nb_points = 0
for i in range(0, NB_QUESTION):
    print(f"Question n°{i+1} sur {NB_QUESTION}:")
    if poser_question() == True:
        print("Correcte")
        nb_points = nb_points + 1
    else:
        print("Incorrecte")

print(f"Votre score est de {nb_points} / {NB_QUESTION}")
moyenne = int(NB_QUESTION/2)
if nb_points == NB_QUESTION:
    print("Excellent")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points > moyenne:
    print("Pas mal")
elif nb_points < moyenne:
    print("Peut mieux faire")

