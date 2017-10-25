___

# **UT1. A4. Sirviendo Aplicaciones Php Y Python.**

La actividad consiste en configurar 2 sitios web, virtual hosts, en nuestro Servidor Web Nginx.

___

# **Sitio Web 1.**

* **http://php.alu5904.me.**

Tenemos que mostrar la aplicación demo_php.zip. Para ello descargamos demo_php.zip.

![imagen01](./img/01.png)

Copiamos el archivo comprimido demo_php.zip a la máquina de producción.

![imagen02](./img/02.png)

Descomprimimos el archivo demo_php.zip.

![imagen03](./img/03.png)

Comprobamos que se a descomprimido el archivo.

![imagen04](./img/04.png)

Ahora lo que hacemos es añadir el fichero de configuración de Nginx que tratará las peticiones que se hagan al nombre de dominio php.alu5904.me. Para ello vamos a la ruta `/etc/nginx/sites-available/` y creamos el fichero demo.

![imagen05](./img/05.png)

Ahora añadimos el contenido a demo.

![imagen06](./img/06.png)

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde los sites-enabled. Para ello entramos a `/etc/nginx/sites-enabled`, hacemos un enlace simbólico y lo comprobamos.

![imagen07](./img/07.png)

Por último, tenemos que recargar la configuración de Nginx para que los cambios surtan efecto, para ello utilizamos el comando systemctl reload nginx.

![imagen08](./img/08.png)

Finalmente entramos desde un navegador a http://php.alu5904.me.

![imagen09](./img/09.png)

___

# **Sitio Web 2.**

* **http://now.alu5904.me.**

Creamos un nuevo entorno virtual.

![imagen10](./img/10.png)

Entramos dentro de nuestro entorno virtual.

![imagen11](./img/11.png)

Dentro de nuestro entorno virtual instalamos el paquete pytz.

![imagen12](./img/12.png)

Ahora dentro de nuestro entorno virtual creamos el directorio now.

![imagen13](./img/13.png)

Entramos dentro de este directorio y creamos el fichero main.py.

![imagen14](./img/14.png)

Ahora añadimos el siguiente contenido a main.py.

~~~
import datetime
import pytz
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now(pytz.timezone("Atlantic/Canary"))
    return """
    <h1>Testing Python over Nginx</h1>
    <h2>In Canary Islands...</h2>
    Today is: {today}
    <br>
    Now is: {now}
    """.format(
        today=now.strftime("%d/%m/%Y"),
        now=now.strftime("%H:%Mh")
    )
~~~

![imagen15](./img/15.png)

Ahora lanzamos el proceso que escuchará peticiones.

![imagen16](./img/16.png)

Vamos a un navegador y ponemos http://alu5904.me:8080.

Creamos un fichero de configuración para uWSGI.

![imagen17](./img/17.png)

Ahora añadimos el siguiente contenido a uwsgi.ini.

~~~
[uwsgi]
chdir = /home/alu5904/now
module = main:app
master = true
processes = 1
socket = /tmp/now.sock
chmod-socket = 666
vacuum = true
~~~

![imagen18](./img/18.png)

Ahora tenemos que crear un pequeño script que será el encargado de activar el entorno virtual de nuestra aplicación y de lanzar el proceso uwsgi para que escuche peticiones en el socket especificado.

![imagen19](./img/19.png)

Ahora añadimos el siguiente contenido a run.sh.

~~~
#!/bin/bash

source /home/alu5904/.virtualenvs/now/bin/activate
uwsgi --ini /home/alu5904/now/uwsgi.ini
~~~

![imagen20](./img/20.png)

Ahora le damos permisos de ejecución al script que hemos creado.

![imagen21](./img/21.png)

En este punto, podríamos lanzar el script run.sh sin tener que activar el entorno virtual previamente, ya que el propio script realiza esta tarea.

![imagen22](./img/22.png)

Ahora lo que hacemos es añadir el fichero de configuración de Nginx que tratará las peticiones que se hagan al nombre de dominio now.alu5904.me. Para ello vamos a la ruta `/etc/nginx/sites-available/` y creamos el fichero demo.

![imagen23](./img/23.png)

Ahora añadimos el contenido a now.

~~~
server {
    server_name now.alu5904.me;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/now.sock;
    }

    location /static {
        root /home/alu5904/now;
    }
}
~~~

![imagen24](./img/24.png)

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde los sites-enabled. Para ello entramos a `/etc/nginx/sites-enabled`, hacemos un enlace simbólico y lo comprobamos.

![imagen25](./img/25.png)

Por último, tenemos que recargar la configuración de Nginx para que los cambios surtan efecto, para ello utilizamos el comando systemctl reload nginx.

![imagen26](./img/26.ong)

Para mantener nuestra aplicación "viva" y poder gestionar su arranque/parada de manera sencilla, necesitamos un proceso coordinador. Para este cometido, se ha desarrollado supervisor.

Comprobamos que el servicio está funcionando.

![imagen27](./img/27.png)

Para que nuestro programa now sea gestionado por supervisor, debemos añadir un fichero de configuración.

![imagen28](./img/28.png)

Ahora añadimos el contenido a now.conf.

~~~
[program:hellopython]
user = sdelquin
command = /home/alu5904/now/run.sh
autostart = true
autorestart = true
stopsignal = INT
killasgroup = true
stderr_logfile = /home/alu5904/now/now.err.log
stdout_logfile = /home/alu5904/now/now.out.log
~~~

![imagen29](./img/29.png)

Reiniciamos el servicio del supervisor.

![imagen30](./img/30.png)

Comprobamos que el servicio está funcionando con normalidad.

![imagen31](./img/31.png)

Ahora, desde la máquina de producción, pero con un usuario no privilegiado, vemos que ya podemos hacer uso de la gestión de nuestros procesos.

![imagen32](./img/32.png)

En este punto, podemos comprobar que el acceso a la aplicación está funcionando.

![imagen33](./img/33.png)

Finalmente entramos desde un navegador a http://php.alu5904.me.

![imagen34](./img/34.png)

---
