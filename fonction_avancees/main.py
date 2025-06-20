# Les notions avancées en python : les fonctions récursives

def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n*n, limit) # récursive c'est le fait de s'appeller soi-même mais en étant dans une code de sortie

a(2, 100)

def demander_choix_user(min, max):
    reponse = input("Quel est votre choix entre "+ str(min) + " et "+ str(max) + " :")
    try:
        reponse_int = int(reponse)
        if not min <= reponse_int <= max:
            print("Erreur")
            return demander_choix_user(min, max)
        return reponse_int
    except:
        print("Erreur: vous devez rentrer un nombre")
        return demander_choix_user(min, max) #la recursive permet de reposer la question et de laisser une choix d'avoir la bonne réponse

choix = demander_choix_user(1, 10)
print("Choix de l'utilisteur:", choix)

#Difference entre BREAK et RETURN :

def b():
    for i in range(0, 100):
        if i > 20:
            break #Permet de casser une boucle sans stopper l'exécution de la suite de la fct en dehors de la boucle
            #return <- le return va completement stoppé la fonction, le print("Fin fonction") ne s'executera pas
        print(i)
    print("Fin de la fonction")

b()

# Les Callback :

def ma_fonction():
    print("toto")
    return 1

a = 5

b = ma_fonction

print("a", a, "b", b())

"""def affiche_table_multiplication(n):
    for i in range(1,10):
        print(i, "x", n, "=", i*n)

def afficher_table_addition(n):
    for i in range(1, 10):
        print(i, "+", n, "=", i+n)"""

def afficher_table(n, operateur_str, operation_callback):
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_callback(i, n))

def mult_callback(a, b):
    return a*b

def add_callback(a, b):
    return a+b

def power_callback(a, b):
    return pow(a, b)

afficher_table(2, "*", mult_callback)
print()
afficher_table(2, "+", add_callback)
print()
afficher_table(2, "^", power_callback)

#Fonctions Lambda <- permet de créer une fonction lambda et ainsi de compacter le code
def afficher_table(n, operateur_str, operation_callback):
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_callback(i, n))

afficher_table(2, "*", lambda a, b : a * b)
print()
afficher_table(2, "+", lambda a, b : a + b)
print()
afficher_table(2, "^", lambda a, b : pow(a, b))

# Nombre variable de paramètres

def somme(titre, *args):#permet d'avoir autant d'args que prévue
    print("TITRE:", titre)
    resultat = 0
    for n in args:
        resultat += n
    return resultat

print(somme("somme des points", 5, 2, 4, 7))

def somme(titre, **args): #deux ** permets de donner des clefs
    print("TITRE:", titre)
    resultat = 0
    for n in args.values():
        resultat += n
    return resultat

print(somme("somme des points", math=5, geo=2))
