apt-get update	Actualiza la lista de paquetes disponibles desde los repositorios. No actualiza el software, solo el "indice".
apt-get upgrade	Actualiza todos los paquetes instalados a sus versiones mas recientes.
apt-get install [paquete]	Instala un paquete y sus dependencias.
apt-get remove [paquete]	Desinstala un paquete, pero deja sus archivos de configuracion.
apt-get purge [paquete]	Desinstala un paquete y tambien elimina sus archivos de configuracion.
apt-get clean	Borra los paquetes .deb descargados y cacheados en /var/cache/apt/archives/. Libera espacio.
apt-cache search [texto]	Busca un paquete en la lista de paquetes disponibles.
apt-cache depends [paquete]	Muestra las dependencias de un paquete.
# dpkg
> Gestor de paquetes de bajo nivel. Trabaja con archivos .deb locales. 
  * -i [archivo.deb]: Instala un paquete desde un archivo.
  * -r [paquete]: Elimina un paquete.
  * -I [archivo.deb]: Muestra informacion de un paquete .deb (version, etc.).
  * -L [paquete]: Lista los archivos instalados por un paquete.
  * -S [archivo]: Busca que paquete instalo un archivo especifico.
