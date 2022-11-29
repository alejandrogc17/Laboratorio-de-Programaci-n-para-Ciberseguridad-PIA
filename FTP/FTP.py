#Script para la transferencia de datos FTP
#El objetivo es conectarse a un servidor ftp,y realizar una subida de este archivo
#Yordi Alejandro González Campos, 1955480, 21/10/2022

#Importación del módulo FTP
from ftplib import FTP
#Establecemos conexión con el servidor#
ftp = FTP("dirección") #Ingresar la dirección ip del servidor.
#Iniciamos sesión con el usuario y contraseña
try:
    user = input("Ingrese el nombre del usuario: ")
    passwd = input ("Ingrese la contraseña del usuario: ")
    ftp.login(user, passwd)
except: #en caso de que algun dato esté equivocado
    print("Error, por favor verifique los datos")
print("Cambiando directorio de trabajo...")
#Cambiamos el directorio de trabajo a 'upload'
ftp.cwd('upload')
print(ftp.pwd())
print("Enviando archivo..")
with open("ADVERTENCIA.txt", "rb") as text_file:
    ftp.storlines('STOR ADVERTENCIA.txt', text_file) #Enviamos nuevamente el archivo ADVERTENCIA.txt, pero esta vez será el modificado.
print("El contenido del directorio actualizado es:")
ftp.retrlines('LIST') #Imprimimos el contenido del directorio, para ver que el archivo fue correctamente cargado.
print("listo, terminando la conexión")
ftp.quit() #Una vez enviado el archivo, cerramos la conexión con el servidor
