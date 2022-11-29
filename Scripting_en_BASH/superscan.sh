#!/bin/bash
#
# Menu en BASH
#<26/09/2022>-Hecho por: <Yordi Alejandro Gonzalez Campos>
date
        echo "---------------"
        echo "    Menu Principal"
        echo "---------------"
        echo "1. Net Discover"
        echo "2. Port Scan"
        echo "3. Welcome"
        echo "4. Exit"
read -p "Opciòn [ 1-4 ] " c
case $c in
        1) $HOME/netdiscover.sh;;
        2) read -p "introduce la ip a revisar: " ip
           ./portscanv1.sh $ip;;
        3) $HOME/welcome.sh;;
        4) echo "Bye!"; exit 0;;
esac

