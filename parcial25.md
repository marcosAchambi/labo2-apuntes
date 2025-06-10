Continúo con las respuestas del examen:
Te ayudo a resolver este examen de Sistemas Operativos II (Linux). Voy corrigiendo también algunos errores de tipeo que veo en las preguntas:

## Respuestas:

**1. Muestre las unidades asociadas a sistemas de archivos**
```bash
systemctl list-units --type=mount
```
o
```bash
df -h
```

**2. Reinicie el servicio rsyslog**
```bash
systemctl restart rsyslog
```

**3. Muestre los últimos 20 registros del kernel**
```bash
journalctl -k -n 20
```
o
```bash
dmesg | tail -20
```

**4. Ver archivos asociados al paquete nano**
```bash
dpkg -L nano
```

**5. Ver dependencias del paquete dmidecode.deb ubicado en /opt**
```bash
dpkg -I /opt/dmidecode.deb | grep Depends
```
o
```bash
dpkg --info /opt/dmidecode.deb
```

**6. Agregar usuario lily con directorio /home/lillana y shell sh**
```bash
useradd -d /home/lillana -s /bin/sh lily
```

**7. Agregar usuario lily al grupo cdrom**
```bash
usermod -a -G cdrom lily
```

**8. Cambiar directorio actual del usuario lily a /home/lily**
```bash
usermod -d /home/lily lily
```

**9. Password del usuario lily debe caducar en 2 días**
```bash
passwd -x 2 lily
```
o
```bash
chage -M 2 lily
```

**10. Sesión remota segura al host 10.10.2.30, puerto 2526, usuario amanda**
```bash
ssh -p 2526 amanda@10.10.2.30
```

**11. Objetivo del comando `systemctl disable rsyslog.service`**
Deshabilita el servicio rsyslog para que NO se inicie automáticamente durante el arranque del sistema. El servicio puede seguir ejecutándose actualmente, pero no se iniciará en futuros reinicios.

**12. Diferencia entre `systemctl is-active ssh` y `systemctl is-enabled ssh`**
- **`systemctl is-active ssh`**: Verifica si el servicio SSH está **ejecutándose actualmente** (estado: active/inactive)
- **`systemctl is-enabled ssh`**: Verifica si el servicio SSH está **habilitado para iniciarse automáticamente** en el arranque (estado: enabled/disabled)

Un servicio puede estar activo pero no habilitado, o habilitado pero no activo actualmente.

¿Necesitas aclaración en alguna de estas respuestas?
**13. Script backup.sh que se ejecute cada 2 días a las 11:30 PM**

Agregar la siguiente línea al crontab:
```bash
crontab -e
```
```
30 23 */2 * * /path/to/backup.sh
```

O si quieres que se ejecute en días específicos (cada 2 días desde una fecha):
```
30 23 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31 * * /path/to/backup.sh
```

**14. Objetivo del comando `apt-get remove --purge vsftpd`**

Desinstala completamente el paquete vsftpd (servidor FTP) y elimina todos sus archivos de configuración. La opción `--purge` asegura que se borren también los archivos de configuración que normalmente se conservan con `remove`.

**15. Línea en /etc/sudoers para que lily ejecute chroot y hwclock**

```
lily ALL=(ALL) NOPASSWD: /usr/sbin/chroot, /sbin/hwclock
```

O si quieres que pida password:
```
lily ALL=(ALL) /usr/sbin/chroot, /sbin/hwclock
```

**16. Objetivo del comando `nmap google.com.ar -O`**

Realiza un escaneo de red con nmap hacia google.com.ar con detección del sistema operativo. La opción `-O` (OS detection) intenta identificar qué sistema operativo está ejecutando el host remoto basándose en las características de la pila TCP/IP.

**Nota**: Este comando requiere privilegios de root para funcionar correctamente debido a que necesita enviar paquetes TCP/IP de bajo nivel.

¿Necesitas que aclare alguna de estas respuestas o hay más preguntas del examen?

