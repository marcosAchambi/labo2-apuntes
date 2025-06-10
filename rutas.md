### Guía Rápida de Archivos y Comandos Clave (Para Exámenes de Laboratorio)

#### **1. Gestión de Usuarios y Privilegios**

| Palabra Clave / Concepto | Ubicación / Comando Clave | Descripción Breve |
| :--- | :--- | :--- |
| **Lista de usuarios** | `/etc/passwd` | Archivo que contiene la información básica de cada usuario (UID, GID, home, shell). |
| **Contraseñas (cifradas)** | `/etc/shadow` | Almacena las contraseñas hasheadas y las políticas de expiración (cuándo cambiar, cuándo expira). |
| **Lista de grupos** | `/etc/group` | Define los grupos y qué usuarios pertenecen a ellos. |
| **Shell para usuario normal** | `/bin/bash` | El intérprete de comandos interactivo estándar. Permite iniciar sesión y trabajar. |
| **Usuario especial (sin shell)**| `/usr/sbin/nologin` | **(¡Muy importante!)** Shell asignado a cuentas de servicio (ej: `www-data`, `backup`) para **impedir el inicio de sesión interactivo**. Solo muestra un mensaje y cierra la sesión. |
| **Alternativa sin shell** | `/bin/false` | Similar a `nologin`, pero no muestra ningún mensaje. Simplemente falla el login silenciosamente. |
| **Configuración de `sudo`** | `/etc/sudoers` | **(¡Crucial!)** Define quién puede ejecutar qué comandos como otro usuario (generalmente root). Se edita con `visudo`. |
| **Privilegios para un usuario** | `elena magda=(root) ...` | En `/etc/sudoers`, significa: El usuario `elena` en el host `magda` puede ejecutar comandos como `root`. |
| **Privilegios para un grupo** | `%srv2024 ALL=(ALL) ...` | En `/etc/sudoers`, significa: **Cualquier miembro del grupo** `srv2024` puede ejecutar comandos. El `%` indica que es un grupo. |
| **Añadir usuario** | `useradd` / `adduser` | Comando para crear nuevos usuarios. |
| **Modificar usuario** | `usermod` | Cambia propiedades de un usuario existente (shell, home, grupo, UID). |
| **Cambiar políticas de pass** | `chage` | Gestiona la caducidad de la contraseña (ej: `-M 45` para cambiar cada 45 días, `-E` para fecha de expiración). |

---

#### **2. Systemd (Gestión de Servicios y Arranque)**

| Palabra Clave / Concepto | Ubicación / Comando Clave | Descripción Breve |
| :--- | :--- | :--- |
| **Archivos de servicio** | `/lib/systemd/system/` | Directorio con las definiciones de unidades (`.service`, `.target`, `.socket`) que vienen con los paquetes instalados. |
| **Personalizar servicios** | `/etc/systemd/system/` | Aquí se colocan o se editan unidades para **sobrescribir** la configuración por defecto. Los cambios del administrador van aquí. |
| **Target por defecto** | `/etc/systemd/system/default.target` | Es un enlace simbólico al target que se inicia por defecto (ej: `graphical.target` o `multi-user.target`). |
| **Ver estado de unidades** | `systemctl status <unidad>` | Muestra si una unidad está activa, inactiva, su PID, y los últimos logs. |
| **Habilitar al arranque** | `systemctl enable <unidad>` | Crea los enlaces simbólicos para que el servicio se inicie automáticamente en el próximo arranque. |
| **Deshabilitar al arranque**| `systemctl disable <unidad>` | Elimina los enlaces para que el servicio NO se inicie automáticamente. |
| **Ver registros (logs)** | `journalctl` | El comando principal para ver los logs del sistema gestionados por systemd. |
| **Logs del kernel** | `journalctl -k` | Muestra solo los mensajes del kernel. |
| **Logs en tiempo real** | `journalctl -f` | Sigue mostrando los nuevos logs a medida que aparecen (muy útil). |

---

#### **3. Gestión de Paquetes (APT / DPKG)**

| Palabra Clave / Concepto | Ubicación / Comando Clave | Descripción Breve |
| :--- | :--- | :--- |
| **Fuentes de software** | `/etc/apt/sources.list` | Archivo principal que lista los repositorios de donde se descarga el software. |
| **Actualizar lista de paquetes**| `apt update` | **No actualiza el software**. Solo descarga la lista más reciente de paquetes disponibles desde los repositorios. |
| **Paquetes descargados (caché)** | `/var/cache/apt/archives/` | Aquí se guardan temporalmente los archivos `.deb` que se descargan antes de instalarse. |
| **Limpiar caché de paquetes**| `apt-get clean` | **Borra todos los archivos de `/var/cache/apt/archives/`**. Libera espacio en disco. |
| **Dependencias de un paquete** | `apt show <paquete>` | Muestra información detallada del paquete, incluyendo la línea `Depends:` (dependencias) y `Recommends:` (recomendaciones). |
| **Desinstalar con configuración**| `apt purge <paquete>` | Desinstala un paquete Y **borra sus archivos de configuración globales** (generalmente en `/etc/`). |
| **Ver archivos de un paquete** | `dpkg -L <paquete>` | Lista todos los archivos que un paquete instalado ha colocado en tu sistema. |

---

#### **4. Tareas Programadas (Cron)**

| Palabra Clave / Concepto | Ubicación / Comando Clave | Descripción Breve |
| :--- | :--- | :--- |
| **Tabla de cron del sistema** | `/etc/crontab` | Archivo para definir tareas programadas para todo el sistema. **Importante: requiere especificar el usuario** que ejecutará el comando. |
| **Formato `crontab`** | `minuto hora día-mes mes día-semana usuario comando` | El formato estándar de una línea en `/etc/crontab`. |
| **Ejemplo `crontab`** | `30 23 * * 1,3 root /opt/backup.sh` | Ejecuta `backup.sh` como usuario `root` a las 11:30 PM (`23:30`), todos los lunes (`1`) y miércoles (`3`). |
| **Ejemplo `crontab` (2)** | `0 14 * * 3,7 user /script.sh` | Ejecuta `script.sh` como `user` a las 2 PM (`14:00`) todos los miércoles (`3`) y domingos (`7` o `0`). |
| **Ejemplo `crontab` (3)** | `*/8 * * * * user /script.sh`| Ejecuta el script **cada 8 minutos**. El `*/` significa "cada". |

---

#### **5. Dispositivos y Sistema de Archivos**

| Palabra Clave / Concepto | Ubicación / Comando Clave | Descripción Breve |
| :--- | :--- | :--- |
| **Archivos de dispositivo** | `/dev/` | Directorio donde el sistema "representa" el hardware como si fueran archivos. |
| **Unidad de almacenamiento**| `/dev/sda1` | Representa la **primera partición (`1`)** del **primer disco duro tipo SATA/SCSI/USB (`a`)**. |
| **Montaje al arranque** | `/etc/fstab` | Archivo que define qué sistemas de archivos se montan automáticamente durante el inicio del sistema. |

### Consejos para el Examen:

*   **`sudoers` vs `crontab`:** No confundas el formato. `sudoers` define **permisos**, `crontab` define **cuándo** se ejecuta algo. `crontab` tiene el campo de `usuario` que `sudoers` no tiene en esa posición.
*   **`enable` vs `start`:** `systemctl start` inicia un servicio **ahora**, pero no sobrevive un reinicio. `systemctl enable` hace que se inicie en el **próximo arranque**, pero no lo inicia ahora.
*   **`apt update` vs `apt upgrade`:** `update` solo actualiza la **lista** de lo que hay. `upgrade` **instala** las nuevas versiones de los paquetes que ya tienes.
*   **UID < 1000:** Generalmente son usuarios de sistema o especiales.
*   **UID >= 1000:** Generalmente son usuarios normales (humanos).

