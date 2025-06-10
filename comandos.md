#
fdisk :: Muestra y manipula las tablas de particiones
fdisk -l :: Lista todas las particiones de todos los discos
fdisk -l /dev/sda :: Lista las particiones del disco /dev/sda
fdisk -l /dev/sda1 :: Lista las particiones del disco /dev/sda1
fdisk -l /dev/sdb :: Lista las particiones del disco /dev/sdb
lshw :: Muestra información detallada del hardware del sistema
lshw -short :: Muestra un resumen del hardware del sistema
lshw -class disk :: Muestra información detallada de los discos del sistema
lshw -class memory :: Muestra información detallada de la memoria del sistema
lshw -class network :: Muestra información detallada de las interfaces de red del sistema
lshw -class processor :: Muestra información detallada de los procesadores del sistema
lshw -class display :: Muestra información detallada de las tarjetas gráficas del sistema
lshw -class storage :: Muestra información detallada de los dispositivos de almacenamiento del sistema
lspci :: Muestra información detallada de los dispositivos PCI del sistema
lspci -v :: Muestra información detallada de los dispositivos PCI del sistema con más detalles
lspci -vv :: Muestra información detallada de los dispositivos PCI del sistema con aún más detalles
lspci -vvv :: Muestra información detallada de los dispositivos PCI del sistema con el máximo de detalles
lspci -k :: Muestra información de los controladores de los dispositivos PCI del sistema
lsusb :: Muestra información detallada de los dispositivos USB del sistema
lsusb -v :: Muestra información detallada de los dispositivos USB del sistema con más detalles
lsusb -t :: Muestra la topología de los dispositivos USB del sistema
lsusb -s :: Muestra información de un dispositivo USB específico
lsusb -d :: Muestra información de un dispositivo USB específico por ID de proveedor y producto
df :: Muestra información sobre el uso del sistema de archivos
df -h :: Muestra información sobre el uso del sistema de archivos en un formato legible
df -i :: Muestra información sobre el uso de inodos del sistema de archivos
df -T :: Muestra información sobre el tipo de sistema de archivos
df -a :: Muestra información sobre todos los sistemas de archivos, incluyendo los pseudo-sistemas
df -l :: Muestra información sobre los sistemas de archivos locales
df -x :: Muestra información sobre los sistemas de archivos excluyendo el tipo especificado
lsblk :: Muestra información sobre los dispositivos de bloques
lsblk -a :: Muestra información sobre todos los dispositivos de bloques, incluyendo los vacíos
lsblk -f :: Muestra información sobre los sistemas de archivos de los dispositivos de bloques
lsblk -l :: Muestra información sobre los dispositivos de bloques en formato de lista
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT :: Muestra información específica de los dispositivos de bloques
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE,UUID :: Muestra información detallada de los dispositivos de bloques
lsblk -p :: Muestra información sobre los dispositivos de bloques con rutas completas
lsblk -d :: Muestra información sobre los dispositivos de bloques sin particiones
lsb_release :: Muestra información del sistema operativo
lsb_release -a :: Muestra información de la distribución instalada
uname :: Muestra información del sistema
uname -a :: Muestra información del sistema, incluyendo el kernel
uname -r :: Muestra la versión del kernel
uname -m :: Muestra la arquitectura del sistema
uname -o :: Muestra el nombre del sistema operativo
hostname :: Muestra el nombre del host
hostname -I :: Muestra las direcciones IP del host
hostnamectl :: Muestra información del sistema y del host
uptime :: Muestra el tiempo de actividad del sistema
uptime -p :: Muestra el tiempo de actividad del sistema en un formato legible
uptime -s :: Muestra la fecha y hora de inicio del sistema
date :: Muestra la fecha y hora actual
date -u :: Muestra la fecha y hora actual en UTC
cal :: Muestra el calendario del mes actual
cal 2023 :: Muestra el calendario del año 2023
cal 2023 10 :: Muestra el calendario de octubre de 2023
whoami :: Muestra el nombre del usuario actual
who :: Muestra los usuarios conectados al sistema
w :: Muestra los usuarios conectados y su actividad
last :: Muestra el historial de inicio de sesión de los usuarios
last -a :: Muestra el historial de inicio de sesión de los usuarios con direcciones IP
last -x :: Muestra el historial de inicio de sesión de los usuarios con información adicional
last -F :: Muestra el historial de inicio de sesión de los usuarios con fechas completas
last -i :: Muestra el historial de inicio de sesión de los usuarios con direcciones IP
last -n 10 :: Muestra los últimos 10 inicios de sesión de los usuarios
last -p :: Muestra el historial de inicio de sesión de los usuarios con información de tiempo
last -R :: Muestra el historial de inicio de sesión de los usuarios sin mostrar el nombre del host
last -w :: Muestra el historial de inicio de sesión de los usuarios con información de tiempo extendida
uptime -V :: Muestra la versión del comando uptime
free :: Muestra información sobre la memoria del sistema
free -h :: Muestra información sobre la memoria del sistema en un formato legible
free -m :: Muestra información sobre la memoria del sistema en megabytes
free -g :: Muestra información sobre la memoria del sistema en gigabytes
df :: Muestra información sobre el uso del sistema de archivos
df -h :: Muestra información sobre el uso del sistema de archivos en un formato legible
df -i :: Muestra información sobre el uso de inodos del sistema de archivos
df -T :: Muestra información sobre el tipo de sistema de archivos
df -a :: Muestra información sobre todos los sistemas de archivos, incluyendo los pseudo-sistemas
df -l :: Muestra información sobre los sistemas de archivos locales
df -x :: Muestra información sobre los sistemas de archivos excluyendo el tipo especificado
df -t :: Muestra información sobre los sistemas de archivos del tipo especificado
df --total :: Muestra un resumen del uso del sistema de archivos
df --block-size=1K :: Muestra información sobre el uso del sistema de archivos en bloques de 1K
df --block-size=1M :: Muestra información sobre el uso del sistema de archivos en bloques de 1M
df --block-size=1G :: Muestra información sobre el uso del sistema de archivos en bloques de 1G
df --block-size=1T :: Muestra información sobre el uso del sistema de archivos en bloques de 1T
df --block-size=1P :: Muestra información sobre el uso del sistema de archivos en bloques de 1P
df --block-size=1E :: Muestra información sobre el uso del sistema de archivos en bloques de 1E
df --block-size=1Z :: Muestra información sobre el uso del sistema de archivos en bloques de 1Z


