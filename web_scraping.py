import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette_ua/"
HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0" }
response = requests.get(url, headers = HEADERS) #Requete avec une paramètre headers qui permet de contourner les requetes par scripts
response.encoding = response.apparent_encoding #Determine le codage du contenu de la response


if response.status_code == 200: #Vérifie le code la requete que tout s'est bien passé donc 200
    html = response.text # Réponse de la requetes assigner à la variable html
    soup = BeautifulSoup(html, "html5lib") # html utilise le parser html5lib assigner à la variable soup

    div_ingredients = soup.find("table", class_="preparation") #Trouve le premier élement table avec classe preparation
    etapes = div_ingredients.find_all("td", class_="preparation_etape") #Trouve tous les élements de td avec une class preparation_etape
    for etape in etapes: #Itération dans chaque td
        print(etape.text) #Affiche le texte du td

