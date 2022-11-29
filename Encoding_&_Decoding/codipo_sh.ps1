Clear-Host
Write-Host "Bienvenido a un ejemplo de codificación/decodificación base 64 usando Powershell" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
#
# Se va a leer el contenido del archivo de texto
#
$inputfile = "C:\Program Files\WindowsPowerShell\Modules\Tareas\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green
#
# Decodificando contenido de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" "C:\Program Files\WindowsPowerShell\Modules\Tareas\decode_secret.txt"
$outfile12 = Get-Content 'C:\Program Files\WindowsPowerShell\Modules\Tareas\secret.txt'
Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "Decodificado:" $outfile12
