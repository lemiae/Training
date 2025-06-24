def tri_perso(e):
    return len(e)

def afficher(collection, nb=-1):
    c = collection[0:3]

    if not nb == -1:
        c = collection[:nb]
    
    print(f"---- LISTE DES PIZZAS ({len(c)}) ----")
    #collection.sort(reverse=True)
    c.sort(key=tri_perso)
    if len(c) == 0:
        "AUCUNE PIZZA"
    else:
        for i in c:
            print(i)
        print()
        print("Première pizza :", c[0])
        print("Dernière pizza :", c[-1])

pizzas = ["4 fromage", "végétarienne", "hawai", "calzone"]

def ajouter_pizza_user(collection):
    new_pizza = input("Nom de la nouvelle pizza :")
    #if pizza_existe(new_pizza, collection):
    if new_pizza in collection:
        print("Erreur : la pizza existe déjà")
    else:
        collection.append(new_pizza)

"""def pizza_existe(e,collection):
    for i in collection:
        if i == e:
            return True
    return False"""

#afficher(pizzas)
ajouter_pizza_user(pizzas)
afficher(pizzas,2)