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


pizzas = [Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True), 
          Pizza("Hawai", 8.5, ("annanas", "creme", "poulet")), 
          Pizza("raviole", 11, ("raviole", "emmental", "compté", "creme")),
          Pizza("Végétarienne", 7.8, ("raviole", "oignon", "tomate", "poivrons"), True)]
#pizza1 = Pizza(pizzas)

#Trier par nom
def trie(e):
    return e.prix

pizzas.sort(key=trie)

for pizza in pizzas:
    pizza.Afficher()
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