# Comandos de Gestión de Usuarios, Grupos y Políticas en Linux

## Gestión de Usuarios

su [usuario] :: Substitute User. Cambia al usuario root u otro usuario. Pide la contraseña del usuario de destino.
useradd [usuario] :: Crea un nuevo usuario. Opciones: -u [UID], -g [grupo principal], -G [grupos secundarios], -m (crea home), -s [shell], -M (no crea home), -d [ruta_home].
adduser [usuario] :: Comando interactivo y amigable para crear un nuevo usuario (común en Debian/Ubuntu).
usermod [opciones] [usuario] :: Modifica un usuario existente. Opciones: -l [nuevo_nombre], -L (bloquea), -U (desbloquea), -d [nuevo_home], -s [nueva_shell], -a -G [grupo] (añade a grupo secundario).
passwd [usuario] :: Cambia la contraseña de un usuario. Si no se especifica usuario, cambia la propia.
passwd -l [usuario] :: Bloquea la cuenta de un usuario (impide login con contraseña). Alternativa a `usermod -L`.
passwd -u [usuario] :: Desbloquea la cuenta de un usuario bloqueada con `passwd -l`. Alternativa a `usermod -U`.
userdel [usuario] :: Elimina un usuario, pero mantiene su directorio home por defecto.
userdel -r [usuario] :: Elimina un usuario y también su directorio home y cola de correo.

## Gestión de Grupos

groupadd [grupo] :: Crea un nuevo grupo.
groupadd -g [GID] [grupo] :: Crea un nuevo grupo con un GID (Group ID) específico.
groupdel [grupo] :: Elimina un grupo.
gpasswd -a [usuario] [grupo] :: Agrega un usuario a un grupo.
gpasswd -d [usuario] [grupo] :: Elimina un usuario de un grupo.
gpasswd -M [user1,user2] [grupo] :: Define la lista completa de miembros de un grupo.

## Políticas de Contraseña y Cuentas

chage [opciones] [usuario] :: Change Age. Administra la información de expiración de la contraseña y la cuenta.
chage -l [usuario] :: Muestra la información de expiración de la contraseña y cuenta de un usuario.
chage -M [días] [usuario] :: Fija el número máximo de días que una contraseña es válida.
chage -m [días] [usuario] :: Fija el número mínimo de días antes de poder cambiar una contraseña.
chage -E [YYYY-MM-DD] [usuario] :: Fija la fecha de expiración de la cuenta de usuario.
/etc/login.defs :: Archivo de configuración con valores por defecto para políticas de cuentas (PASS_MAX_DAYS, etc.).
/etc/skel :: Directorio plantilla. Los archivos y directorios aquí se copian al home de los nuevos usuarios.

## Comandos de Información y Diagnóstico

id [usuario] :: Muestra el UID, GID y grupos a los que pertenece un usuario.
groups [usuario] :: Muestra los grupos a los que pertenece un usuario.
who :: Muestra los usuarios que están actualmente logueados en el sistema.
w :: Muestra los usuarios logueados y lo que están haciendo.
last [usuario] :: Muestra el historial de inicios de sesión de un usuario.
cat /etc/passwd :: Muestra la base de datos de usuarios del sistema.
cut -d: -f1 /etc/passwd :: Muestra solo los nombres de usuario del sistema.
cat /etc/group :: Muestra la base de datos de grupos del sistema.
cut -d: -f1 /etc/group :: Muestra solo los nombres de los grupos del sistema.
dmidecode :: Muestra información detallada del hardware del sistema (BIOS, CPU, RAM). Requiere `sudo`.
hwclock :: Consulta y configura el reloj del hardware (RTC). Requiere `sudo`.
dmesg :: Muestra los mensajes del buffer del kernel. Útil para diagnosticar problemas de hardware.
pwck :: Verifica la integridad del archivo /etc/passwd y ficheros asociados.
grpck :: Verifica la integridad del archivo /etc/group y ficheros asociados.
chmod +x [script.sh] :: Otorga permisos de ejecución a un archivo (script).

### --- Ejemplos Prácticos ---

# Crear un usuario 'alexis' con UID 1020, home en /opt/develop, shell /bin/sh y grupo principal 'develop'
sudo useradd -u 1020 -d /opt/develop -s /bin/sh -g develop alexis

# Crear un usuario de sistema 'emulate' sin directorio home y sin capacidad de login
sudo useradd -u 140 -M -s /usr/sbin/nologin emulate

# Agregar al usuario 'admin' al grupo 'wheel' (usado para dar privilegios de sudo en algunos sistemas)
sudo useradd -G wheel admin

# Cambiar el home del usuario 'tester' a /opt/tester y mover sus archivos
sudo usermod -d /opt/tester -m tester

# Fijar que la contraseña de 'alexis' expire cada 30 días y que su cuenta se desactive el 2025-09-21
sudo chage -M 30 -E 2025-09-21 alexis
