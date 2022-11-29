#Yordi Alejandro González Campos
#1955480
from email.message import EmailMessage #Importamos el modulo que nos ayudará a enviar el mensaje
import smtplib #nos ayudará a realizar la conexión con el servicio de correo
remitente = "remitente"
destinatario = "destinatario"
mensaje = """<p><strong>"Practica 12</strong></p> 
<p>Ejercicio de la practica 12 para envio de correos</p>
<p><strong>Alumno:</strong> Yordi Alejandro Gonzalez Campos</p>
<p><strong>Matricula</strong>: 19445480</p>
<p>"</p>"""  #mensaje en codigo html
email = EmailMessage()
email["From"] = 'remitente' #nosotros, quien envía el correo
email["To"] = 'destinatario' #hacia quien enviamos el correo
email["Subject"] = "Prueba de envio (script python) 1955480" #Asunto del correo
email.set_content(mensaje, subtype="html") #Adjuntamos el mensaje html como cuerpo, especificando su formato
with open("fcfm_cool.png", "rb") as f: #abrimos la imagen que enviaremos, en modo bytes (rb)
    email.add_attachment( #Añadimos la imagen al correo
        f.read(),
        filename="fcfm_cool.png", #especificaciones para correo
        maintype="application",
        subtype="png"
    )
smtp = smtplib.SMTP("smtp.gmail.com", port=587) #hacemos la conexion con gmail, medio por donde enviaremos el correo
smtp.starttls() #iniciamos sesion tls
smtp.login('usuario', 'contraseña') #ingresamos con nuestro usuario y contraseña de aplicacion.
smtp.sendmail(remitente, destinatario, email.as_string()) #enviamos el mensaje previamente establecido, junto con la imagen adjunta
smtp.quit() #cerramos la conexión
print("Correo enviado!!")
