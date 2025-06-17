apt-get update	Actualiza la lista de paquetes disponibles desde los repositorios. No actualiza el software, solo el "indice".
apt-get upgrade	Actualiza todos los paquetes instalados a sus versiones mas recientes.
apt-get install [paquete]	Instala un paquete y sus dependencias.
apt-get remove [paquete]	Desinstala un paquete, pero deja sus archivos de configuracion.
apt-get purge [paquete]	Desinstala un paquete y tambien elimina sus archivos de configuracion.
apt-get clean	Borra los paquetes .deb descargados y cacheados en /var/cache/apt/archives/. Libera espacio.
apt-cache search [texto]	Busca un paquete en la lista de paquetes disponibles.
apt-cache depends [paquete]	Muestra las dependencias de un paquete.
apt-get download [paquete]	Descarga un paquete sin instalarlo. Util para obtener el .deb.
# dpkg
> Gestor de paquetes de bajo nivel. Trabaja con archivos .deb locales. 
  * -i [archivo.deb]: Instala un paquete desde un archivo.
  * -r [paquete]: Elimina un paquete.
  * -I [archivo.deb]: Muestra informacion de un paquete .deb (version, etc.).
  * -L [paquete]: Lista los archivos instalados por un paquete.
  * -S [archivo]: Busca que paquete instalo un archivo especifico.
  -i o --install: Palabra clave: "Instalar un archivo .deb". Comando: sudo dpkg -i <paquete.deb>.
-l o --list: Palabra clave: "Listar paquetes instalados". Comando: dpkg -l. Puedes combinarlo con grep para buscar: dpkg -l | grep vlc.
-r o --remove: Palabra clave: "Desinstalar un paquete". Comando: sudo dpkg -r <paquete>.
-P o --purge: Palabra clave: "Desinstalar completamente". Comando: sudo dpkg -P <paquete>.
-s o --status: Palabra clave: "Comprobar si un paquete está instalado". Comando: dpkg -s <paquete>.
-L o --listfiles: Palabra clave: "Saber qué archivos instaló un paquete y dónde están". Comando: dpkg -L <paquete>.
