import requests
import json
#
#Nombre: Yordi Alejandro González Campos
#Matrícula: 1955480

if __name__ == "__main__":
    url = "http://httpbin.org/post"
    argumentos = {"nombre": "Yordi", "matricula":"1955480", "curso":"Laboratorio de Programación para Ciberseguridad"}
    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)
        
