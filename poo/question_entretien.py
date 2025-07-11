import random

# inverser chaine de caractère
def reverse_string(str):
    chaine = ""
    a = 0
    for i in str:
        a += -1
        chaine += str[a]
    
    # Possibilité aussi : 
    # r = ""
    # for c in str:
    #   r = c + r
    # return r
    return chaine

def reverse_string2(str):
    return s[::-1]

s = "Bonjour toto"
print(reverse_string(s))

# mot le plus long et le plus court

def get_min_and_max_words(sentence):
    tab = sentence.split(" ")
    print(tab)
    maxi = max(tab, key=len)
    print(maxi)
    mini = min(tab, key=len)
    return (mini, maxi)

def get_min_max_word_sorted(sentence):
    sent = get_min_and_max_words(sentence)
    return sorted(sent)

s1 = "Un char sachant chasser"
min_w, max_w = get_min_max_word_sorted(s1)
print(min_w, max_w)

# Trie selectif :

#l = [5, 8, 10, 2, 1]


def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

# Complexité de O(N^2)
def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min

l = generate_random_list(5, 0, 10)
print("UNSORTED:", l)

selection_sort(l)
print("SORTED :", l)

import random
 
sujets = ("un chasseur", "une grand mère", "un chat")
verbes = ("mange", "écrase", "parle à")
complements = ("une vache", "un char", "une fleur")
 
def generer_phrases(donnees, nb_phrases = 0):
    phrases = []
 
    if nb_phrases == 0:
        nb_phrases = len(donnees[0]) * len(donnees[1]) * len(donnees[2])
    
    while len(phrases) < nb_phrases:
        sujet = donnees[0][random.randint(0, len(donnees[0])-1)]
        verbe = donnees[1][random.randint(0, len(donnees[1])-1)]
        complement = donnees[2][random.randint(0, len(donnees[2])-1)]
 
        phrase = sujet + " " + verbe + " " + complement
        if not phrase in phrases:
            phrases.append(phrase)
 
    return phrases
 
 
phrases_generees = generer_phrases((sujets, verbes, complements))
 
print(len(phrases_generees), "phrases générées")
for p in phrases_generees:
    print(p)

