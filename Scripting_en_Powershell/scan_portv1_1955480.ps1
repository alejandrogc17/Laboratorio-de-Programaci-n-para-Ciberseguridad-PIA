#
#Escaneo de puertos (mas comunes) en equipos de misma subred
#Definimos array con puertos a escanear
#establecemos variable para tiempo de espera
#
param([Parameter(Mandatory)] [string] $direccion) #El parámetro dirección se toma de python
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,587,636,993,995,1025,2443,3389,5985,5986,8080,10000)
$waittime = 100
##Generamos bucle foreach para evaluar cada puerto en $portstoscan
foreach ( $p in $portstoscan )
{
    $TCPObject = new-object System.Net.Sockets.TcpClient #Establecemos la conexión TCP para evaluar cada puerto con socket
        try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{} #Intentamos conectar con cada puerto
        if ( $resultado -eq "True")  #si tenemos una conexión exitosa
        {
            Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green #Mostramos cada puerto abierto conforme se van realizando las conexiones
        }
}