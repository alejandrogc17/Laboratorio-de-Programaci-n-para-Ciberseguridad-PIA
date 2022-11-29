#Yordi ALejandro Gonzalez Campos #Matricula:1955480
#!/bin/bash
PS3="Ingresa la opcion que necesitas:"
opc=("Escaneo de red" "Escaneo individual" "Escaneo udp" "Escaneo de script" "Salir")
select i in "${opc[@]}" ; do
        case $i in
          "Escaneo de red")
                        echo "Ingrese la subred a escanear"
                        read subred
                        echo "Ingrese el archivo donde se guardara la informacion (no olvide agregar el .txt)"
                        read archivo
                        nmap -sn $subred -oN $archivo
                        ;;
          "Escaneo individual")
                        echo "Ingrese la ip que desea escanear individualmente"
                        read ip
                        echo "Ingrese el nombre del archivo a donde se dirigira la informacion, agregue el .txt"
                        read archivo2
                        nmap -v -A $ip -oN $archivo2 
                        ;;
          "Escaneo udp")
                        echo "Ingrese la ip a realizar el escaneo udp"
                        read ip2
                        echo "Ingrese el archivo al cual se redirigira la informacion, agregando el .txt"
                        read archivo3
                        nmap -sU $ip2 -oN $archivo3
                        ;;
	  "Escaneo de script")
                        echo "Ingrese la direccion ip que desea escanear"
                        read ip3
                        echo "Ingrese el nombre del script que desea utilizar"
                        read script
                        echo "Ingrese el nombre del archivo al que se redirigira la salida, con .txt"
                        read archivo4
                        nmap --script $script $ip3 -oN $archivo4
                        ;;
          "Salir")
                        echo "Saliendo del menu, adios:)"
                        break
                        ;;
          *)
                        echo "Opcion invalida $REPLY"
                        ;;
        esac
done

