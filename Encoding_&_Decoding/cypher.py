#Alumno: Yordi Alejandro González Campos, Matricula: 1955480, Grupo: 063
#Importamos fernet desde cryptography
#
from cryptography.fernet import Fernet
#Definición del función genwrite que genera una llave para cifrado
def genwrite():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

#Llamamos a la función para generar el archivo "pass.key" que contiene la llave
genwrite()
#Definicion de la función call_key con la cual leemos el contenido de "pass_key"
def call_key():
    return open("pass.key", "rb").read()
#
#Ahora cifraremos un mensaje almacenado y codificado previamente
key = call_key()
banner = "Hola, me llamo Yordi, y estoy programando".encode()  #Introduce aquí tu mensaje a cifrar
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)
#Agregamos el proceso para descifrar el mensaje previo
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)
#
#Fin del script
