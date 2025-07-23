from bs4 import BeautifulSoup

#Lecture de données en html
f = open("recette.html", "r")
html_content =f.read()
f.close()
soup = BeautifulSoup(html_content, 'html.parser')

titre_h1 = soup.find("h1")
print("Titre de la page HTML :", titre_h1.text)

list_div_centre = soup.find_all("div", class_="centre")
if list_div_centre and len(list_div_centre) >= 2:
    paragraphe_description= list_div_centre[1].find("p", class_="description")
print("Paragraphe de la description :", paragraphe_description.text)

div_info = soup.find("div", class_="info")
img_info = div_info.find("img")
print("Image de la recette :", img_info["src"])
print()