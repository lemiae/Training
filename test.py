"""import random

CONV_POUCE = 2.54
CONV_CM = 0.394

def poser_question():
    question = print("Souhaitez vous convertir de pouces vers cm ou de cm vers pouces ?")
    print("A - Pouces vers cm")
    print("B - Cm vers pouces")
    reponse = input("Votre choix entre A et B : ")
    if reponse != "A" or "B":
        print("Rentrez une valeur A ou B.")
    return reponse

nb_conv = input("Combien de nombre souhaitez vous convertir : ")
nb_conv_int = int(nb_conv)
for i in range(0, nb_conv_int):
    conv_question = input("Quel nombre souhaitez vous convertir : ")
    conv_question_float = float(conv_question)
    if poser_question() == "A":
        conv = conv_question_float * CONV_POUCE
        print(f"Votre nombre convertie est : {conv} cm")
    else:
        conv = conv_question_float * CONV_CM
        print(f"Votre nombre convertie est : {conv} pouces")


#print(poser_question())"""

"""conv_question = input("Quel nombre souhaitez vous convertir : ")
conv_question_float = float(conv_question)
if poser_question() == "A":
    conv = conv_question_float * CONV_POUCE
    print(f"Votre nombre convertie est : {conv} cm")
else:
    conv = conv_question_float * CONV_CM
    print(f"Votre nombre convertie est : {conv} pouces")"""

# Exercice Test 2 :

"""import time

def poser_question():
    question = print("Quelle cuisson souhaitez vous ? ?")
    print("A - Oeufs à la coque : 3 minutes")
    print("B - Oeufs mollets : 6 minutes")
    print("C - Oeufs durs : 9 minutes")
    reponse = input("Votre choix entre A, B et C : ")
    if reponse not in ("A", "B", "C"):
        print("Rentrez une valeur A, B ou C.")
    return reponse

def tmp_cuisson():
    reponse = poser_question()
    if reponse == "A":
        d = 180
    elif reponse == "B":
        d = 360
    else:
        d = 540
    
    print("Cuisson en cours")

    for i in range(d, 0, -10):
        min = i // 60
        sec = i % 60
        ligne = f"Temps restant : {min:02d}:{sec:02d} "
        print(f"\r{ligne}", end="", flush=True)
        for t in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
        print()
    print("Félicitation, c'est cuit !")

tmp_cuisson()"""


#Exercice Test 3 :

#utiliser sleep pour retenez sequence pendant & sec puis lq sec en 3 sec

"""import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

bn = 0

print("Retenez la sequence")
time.sleep(1)
clear_screen()
#n = random.randint(0, 9)
seq = ''.join(str(random.randint(0, 9)) for _ in range(4))
print(seq)
time.sleep(3)
clear_screen()

reponse = input("Votre réponse : ")

while reponse == seq:
    bn = bn+1
    print(f"Bonne réponse, votre score est de {bn}")
    time.sleep(2)
    clear_screen()

    nouveau_chiffre = str(random.randint(0, 9))
    seq += nouveau_chiffre
    print("Retenez la sequence")
    time.sleep(1)
    clear_screen()

    print(seq)
    time.sleep(3)
    clear_screen()
    reponse = input("Votre réponse : ")

print(f"Mauvaise réponse, la sequence était : {seq}, votre score final est : {bn}")"""


import random
import time
import os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def afficher_message(message, delay=1, clear=True):
    print(message)
    time.sleep(delay)
    if clear:
        clear_screen()

def generer_sequence(taille):
    return ''.join(str(random.randint(0, 9)) for _ in range(taille))

def demander_reponse():
    return input("Votre réponse : ")

def jeu_de_memoire():
    score = 0
    taille_sequence = 4
    sequence = generer_sequence(taille_sequence)

    while True:
        afficher_message("Retenez la séquence", delay=1)
        print(sequence)
        time.sleep(3)
        clear_screen()

        reponse = demander_reponse()

        if reponse != sequence:
            print(f"Mauvaise réponse ! La séquence était : {sequence}")
            print(f"Votre score final est : {score}")
            break

        score += 1
        print(f"Bonne réponse ! Votre score est de {score}")
        time.sleep(2)
        clear_screen()

        # Ajoute un chiffre à la séquence
        sequence += str(random.randint(0, 9))

# Lancement du jeu
jeu_de_memoire()

a = 5
 
def ma_fonction():
  global a
  a = a + 1
  print(a)
 
ma_fonction()
ma_fonction()

def ma_fonction(nom, age, taille=0):
    print("vous etes" + nom)
    print("vous avez" + str(age) + "ans")
    if taille > 0:
        print("Vous faites" + str(taille))

ma_fonction("PAul", 20)

def f1(n):
  if n > 5:
    return
  ligne = ""
  for i in range(n):
    ligne += "#"
  print(ligne)
  f1(n+1)
 
f1(1)


class Personne:
    def __init__(self, nom: str):
        self.nom = nom
 
    def se_presenter(self, age):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(age) + " ans")
 
personne1 = Personne("Jean")
personne1.se_presenter(20)
 
personne2 = Personne("Emilie")
personne2.se_presenter(25)

class Animal:
  def parler(self):
    print("Rhhhhhh")
 
class Chat(Animal):
  def parler(self):
    print("Miaouuu")
 
class Chien(Animal):
  def aboyer(self):
    print("Woof")
 
chat = Chat()
chat.parler()
 
chien = Chien()
chien.parler()