
#1 - Définir les entitées (données, actions)
# class Question :
#   - titre, choix, bn_réponse 
#   - PoserQuest(), DemanderRepUser()

# class Questionnaire : 
#   - questions -> (Question), score 
#   - LancerQuestionnaire()


class Question:
    def __init__(self, titre: str, choix, bn_reponse: str):
        self.titre = titre
        self.choix = choix
        self.bn_reponse = bn_reponse
    
    def FromData(data):
        q = Question(data[0], data[1], data[2])
        return q
    
    def poser_question(self):
        """self.titre = question[0]
        self.choix = question[1]
        choix_bn_reponse = question[2]"""

        print("Question :", self.titre)
        for i in range(len(self.choix)):
            print(" ", i+1," - ", self.choix[i])

        #reponse_str = input("Votre réponse (entre 1 et "+str(len(choix))+ ") :")
        resultat_reponse_correcte = False
        reponse_int = Question.demander_rep_numerique_user(1, len(self.choix))

        if self.choix[reponse_int-1].lower() == self.bn_reponse.lower():
            print("Bonne réponse")
            resultat_reponse_correcte = True
        else:
            print("Mauvaise réponse")
        print()
        return resultat_reponse_correcte
    
    def demander_rep_numerique_user(min, max):
        reponse_str = input("Votre réponse (entre "+ str(min)+" et "+str(max)+ ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int
            print("Erreur : vous devez rentrer un nombre entre", min, " et ", max)
        except:
            print("Erreur : Rentrez uniquement des chiffres")
        return demander_rep_numerique_user(min, max)
    
class Questionnaire():
    def __init__(self, questions):
        #super().__init__
        self.questions = questions
    
    def lancer(self):
        score = 0
        for q in self.questions:
            if q.poser_question():
                score +=1
        print("Score final :", score, "/", len(self.questions))
        return score


"""question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")"""


#Pour factoriser :
"""data = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
Question(*data)
q = Question.FromData(data)
q.poser_question()"""

questions = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")
    )

"""lancer_questionnaire(questionnaire)"""

q1 = Questionnaire(questions)
q1.lancer()

#poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
