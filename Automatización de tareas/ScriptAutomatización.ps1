$Path = (get-command powershell.exe).Path #Obtenemos la ruta de Powershell.exe, de modo que pueda ejecutar argumentos correctamente
$Acción = New-ScheduledTaskAction -Execute $Path -Argument "send_sysinfo.ps1" -workingDirectory "C:\Windows\System32" #Execute tiene la ruta de powershell, porque lo usamos para ejecutar el programa, -Argument es el script a ejecutar, y -WorkingDirectory el directorio de trabajo.
$Hora = New-ScheduledTaskTrigger -Once -At "1:46am" #-Once para que solo se haga una vez, y -At especifica la hora que queremos. 
Register-ScheduledTask SEND_SYSINFO2 -RunLevel Highest -Trigger $Hora -Action $Acción -TaskPath “MisTareas”
#Yordi Alejandro González Campos
#1955480

