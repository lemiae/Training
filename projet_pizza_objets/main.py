#nom, prix, ingrédients, végé
class Pizza:
    def __init__(self, nom: str, prix: float, ingredients: str, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne
    
    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "- VEGETERIENNE"
        print(f"Pizza {self.nom} : {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisée" + str(self.numero), 0, [])
        self.demander_ingredient_utilisateur()
        self.calculer_le_prix()

    def demander_ingredient_utilisateur(self):
        print(f"Ingrédients pour la pizza personnalisé {self.numero}")
        while True:
            ingredient = input("Ajouter un ingrédient (ou ENTER pour terminer) :")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")
    
    def calculer_le_prix(self):
        self.prix = (len(self.ingredients)* self.PRIX_PAR_INGREDIENT) + self.PRIX_DE_BASE



pizzas = [Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True), 
          Pizza("Hawai", 8.5, ("annanas", "creme", "poulet")), 
          Pizza("raviole", 11, ("raviole", "emmental", "compté", "creme")),
          Pizza("Végétarienne", 7.8, ("raviole", "oignon", "tomate", "poivrons"), True),
          PizzaPersonnalisee(),
          PizzaPersonnalisee()]

for pizza in pizzas:
    pizza.Afficher()

#pizza1 = Pizza(pizzas)


#Trier par nom
"""def trie(e):
    return e.prix

pizzas.sort(key=trie)
"""
#afficher les pizza avec de la tomate
"""for pizza in pizzas:
    if pizza.prix < 10:
        pizza.Afficher()"""


"""    if  "tomate" in pizza.ingredients:
        pizza.Afficher()"""

"""    if pizza.vegetarienne:
        pizza.Afficher()"""

    #print(pizza)
    #piz = Pizza(pizza[0], pizza[1], pizza[2])

    #pizza.Afficher()

#