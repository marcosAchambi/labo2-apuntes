systemctl status [unidad]	Muestra el estado detallado de una unidad.
systemctl start [unidad]	Inicia una unidad.
systemctl stop [unidad]	Detiene una unidad.
systemctl restart [unidad]	Reinicia una unidad.
systemctl enable [unidad]	Habilita que una unidad se inicie automaticamente en el arranque.
systemctl disable [unidad]	Deshabilita el inicio automatico de una unidad.
systemctl is-active [unidad]	Comprueba si una unidad esta activa. Devuelve "active" o "inactive".
systemctl list-units	Muestra todas las unidades activas. --type=[tipo]: Filtra por tipo (service, socket, etc.).
  * --all: Muestra todas las unidades, incluyendo las inactivas.
journalctl	Consulta los registros (logs) del sistema gestionados por systemd. 
  * -u [unidad]: Muestra logs de una unidad especifica.
  * -k: Muestra solo los mensajes del kernel. 
  * -n [numero]: Muestra las ultimas [numero] lineas.
  * -f: Muestra los logs en tiempo real.
  * --since [fecha]: Muestra logs desde una fecha especifica.
  * --until [fecha]: Muestra logs hasta una fecha especifica.
  journalctl -u nombre-del-servicio --since "2025-06-01" --until "2025-06-09"
crontab -e	Edita la tabla de cron del usuario actual.
crontab -l	Muestra la tabla de cron del usuario actual.
