#Yordi Alejandro González Campos
#1955480 
#!/usr/bin/python
# _*_ coding: utf-8 _*_
#parte1
#Importamos librerias necesarias
import sys
from socket import *
#Parte2
#Modo de ejecución del script
# port_scan.py <host> <start_port>-<end_port>
#Primer argumento se guarda en variable host
#Segundo argumento se guarda en variable portstrs
host = sys.argv[1]
portstrs = sys.argv[2].split('-')
#Parte3
#portstrs contiene dos variables que asignamos
#en strart_port e valor de inicio
#en end_port el valor fin
start_port = int(portstrs[0])
end_port = int(portstrs[1])
#parte4
#Para usar en el socket asignado lo de la
#variable host a traget_ip
#Definimos una lista de puertos opened_ports
target_ip = gethostbyname(host)
opened_ports = []
#Parte5
#Iniciamos bucle for para probar puertos
for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)
#Parte 6 se imprime salida
        print("Opened ports:")
    #
for i in opened_ports:
    print(i)
