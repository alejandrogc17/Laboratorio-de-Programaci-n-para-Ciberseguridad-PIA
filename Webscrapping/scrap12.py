#Yordi Alejandro González Campos 1955480
#importación de módulos
import requests
from bs4 import BeautifulSoup
#obtención de los datos mediante petición GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Analizamos el contenido con beautifulsoup
soup= BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
#Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")
#buscar todos los elementos que contengan la palabra "python"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )
#buscar cada elemento que contenga referencia de python_jobs y almacenarlo en python_jobs_elements
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]
#buscamos y mostramos información sobre los elementos python_jobs
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    #buscamos etiqueta "a"
    link_url = job_element.find_all("a")[1]["href"]
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(title_element.text.strip())
    #Imprimimos la salida con link_url
    print(f"Apply Here: {link_url}\n")
    print()
    
