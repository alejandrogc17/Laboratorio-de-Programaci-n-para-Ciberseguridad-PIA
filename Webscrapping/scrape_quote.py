#Yordi Alejandro González Campos Matricula: 1955480, Grupo: 063
#Importar módulos
import requests
import csv
from bs4 import BeautifulSoup
#Dirección de la página web
url = "http://quotes.toscrape.com/"
# ejecutar get request
response = requests.get(url)
#Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente.
html = BeautifulSoup(response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
#crear una lista de las citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
#crear una lista de los autores
authors = list()
for author in authors_html:
    authors.append(author.text)
#para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
#guardar las citas y los autores en un archivo CSV en el directorio actual
#abrir el archivo con excel/ Libreoffice, etc.
with open('./citas_1955480.csv', 'w') as csv_file:
    csv_writter = csv.writer(csv_file, dialect='excel')
    csv_writter.writerows(zip(quotes, authors))
