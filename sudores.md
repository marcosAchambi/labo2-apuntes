# Comandos y Configuración de Sudo

## Comandos Principales

sudo [comando] :: Super User DO. Ejecuta un comando con los privilegios de root u otro usuario.
sudo -l :: Lista los comandos que el usuario actual tiene permitido ejecutar con sudo.
sudo -l -U [usuario] :: Lista los privilegios de sudo para otro usuario específico.
sudo visudo :: Edita el archivo /etc/sudoers de forma segura (comprueba la sintaxis antes de guardar).
sudo visudo -c :: Comprueba la sintaxis del archivo /etc/sudoers sin abrir el editor.

## Sintaxis y Archivos de Configuración

/etc/sudoers :: Archivo de configuración principal de sudo. NO editar directamente, usar `visudo`.
Sintaxis básica :: usuario HOST=(usuario_ejecutor:grupo_ejecutor) COMANDOS
usuario ALL=(ALL:ALL) ALL :: Permite a 'usuario' ejecutar cualquier comando como cualquier usuario/grupo en cualquier host.
%grupo ALL=(ALL) ALL :: Permite a cualquier miembro del 'grupo' ejecutar cualquier comando. El '%' indica que es un grupo.
!/sbin/halt :: Niega la ejecución de un comando específico. La '!' es el operador de negación.

## Alias en Sudoers

User_Alias [ALIAS] = usuario1, usuario2 :: Crea un alias para un grupo de usuarios.
Cmnd_Alias [ALIAS] = /ruta/cmd1, /ruta/cmd2 :: Crea un alias para un grupo de comandos.

## Directivas de Configuración (Defaults)

Defaults timestamp_timeout=0 :: Deshabilita el "periodo de gracia". Sudo pedirá la contraseña para cada comando.
Defaults timestamp_timeout=5 :: Fija el periodo de gracia a 5 minutos (valor por defecto en muchas distros).
Defaults passwd_tries=3 :: Configura el número máximo de intentos de contraseña fallidos (por defecto 3).

### --- Ejemplos de Configuración en /etc/sudoers ---

# Usuario 'elena' puede ejecutar comandos de diagnóstico de hardware
elena ALL=(ALL) /usr/sbin/dmidecode, /sbin/hwclock, /bin/dmesg

# Usuario 'elena' puede ejecutar cfdisk sin necesidad de introducir su contraseña
elena ALL=(ALL) NOPASSWD: /sbin/cfdisk

# Usuario 'alumno' puede ejecutar todo excepto los comandos para apagar el sistema
alumno ALL=(ALL) ALL, !/sbin/halt, !/sbin/poweroff, !/sbin/shutdown

# Creación de un alias de comandos para apagar/reiniciar
Cmnd_Alias POWER_COMMANDS = /sbin/halt, /sbin/shutdown, /sbin/poweroff, /sbin/reboot

# Creación de un alias de usuarios administradores
User_Alias ADMINS = rperez, alexis

# Uso de los alias para dar permisos
ADMINS ALL=(ALL) ALL
elena ALL=(ALL) POWER_COMMANDS

# Permitir a un usuario ejecutar un script específico
elena ALL=(ALL) /home/alumno/testServer.sh
