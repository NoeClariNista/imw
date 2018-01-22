___

# **UT4 - A1: Implantación De Wordpress.**

---

## **1. Instalación De Wordpress.**

Vamos a instalar un sitio web Wordpress en nuestra máquina de producción. Para ello accedemos a la máquina de producción vía ssh.

![imagen01](./img/01.png)

---

## **2. Configuración De La Base De Datos.**

Wordpress necesita un usuario/contraseña para acceder a una base de datos. Para ello, usaremos el intérprete de MySQL.

![imagen02](./img/02.png)

Tenemos que crear la base de datos, el usuario y asignar privilegios.

![imagen03](./img/03.png)

---

## **3. Descarga De Código.**

Descargamos el código fuente de Wordpress desde su página web.

![imagen04](./img/04.png)

Descomprimimos el código y lo copiamos en /usr/share.

![imagen05](./img/05.png)

![imagen06](./img/06.png)

Ahora tenemos que establecer los permisos necesarios para que el usuario web www-data pueda usar estos ficheros.

![imagen07](./img/07.png)

---

## **4. Editar Ficheros De Configuración.**

Debemos especificar el nombre de la base de datos, el usuario y la contraseña, para que Wordpress pueda usarlos.

![imagen08](./img/08.png)

~~~
...
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wpdatabase');

/** MySQL database username */
define('DB_USER', 'wpuser');

/** MySQL database password */
define('DB_PASSWORD', 'Testing_1234');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');
...
~~~

![imagen09](./img/09.png)

---

## **5. Acceso Mediante Nginx.**

Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web Nginx.

Supongamos que queremos acceder a nuestro Wordpress desde la url wordpress.imwpto.me. Para ello tendremos que crear un nuevo virtual host de la siguiente manera.

![imagen10](./img/10.png)

~~~
server {
    server_name wordpress.imwpto.me;
    index index.php;
    root /usr/share/wordpress;
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.0-fpm.sock;
    }
}
~~~

![imagen11](./img/11.png)

Enlazamos la configuración para que el virtual host esté disponible.

![imagen12](./img/12.png)

Recargamos el servidor web Nginx para que los cambios sean efectivos.

![imagen13](./img/13.png)

---

## **6. Configuración Del Sitio Vía Web.**

Ahora podemos acceder a la dirección de nuestro servidor para configurar nuestro Wordpress vía web.

Cuando accedemos a `http://wordpress.alu5904.me` nos redirige a `http://wordpress.alu5904.me/wp-admin/install.php`.

Elegimos el idioma Español y le damos a Continuar.

![imagen14](./img/14.png)

Rellenamos los campos que nos piden y pulsamos Instalar Wordpress.

![imagen15](./img/15.png)

![imagen16](./img/16.png)

Pulsamos en el botón Acceder e ingresamos nuestras credenciales.

![imagen17](./img/17.png)

Así habremos podido acceder a la interfaz administrativa de Wordpress.

![imagen18](./img/18.png)

---

## **7. Ajuste De Permalinks.**

En primer lugar activamos esta opción dentro de la interfaz administrativa de Wordpress.

Seleccionamos el ajuste Día y nombre. Pulsamos en Guardar cambios.

![imagen19](./img/19.png)

Ahora debemos indicar a Nginx que procese estas URLs.

![imagen20](./img/20.png)

~~~
location / {
    try_files $uri $uri/ /index.php?$args;
}
~~~

![imagen21](./img/21.png)

No olvidarnos de recargar la configuración de Nginx:

![imagen22](./img/22.png)

Una ventaja que tiene este método es que podemos acceder a la zona administrativa utilizando la siguiente URL. http://wordpress.imwpto.me/admin

![imagen23](./img/23.png)

![imagen24](./img/24.png)

## **8. Instalar Y Activar Un Tema.**

Instalamos y activamos un tema gratuito.

![imagen25](./img/25.png)

![imagen26](./img/26.png)

![imagen27](./img/27.png)

![imagen28](./img/28.png)

![imagen29](./img/29.png)

![imagen30](./img/30.png)

![imagen31](./img/31.png)

![imagen32](./img/32.png)

![imagen33](./img/33.png)

## **9. Post Con Las Estadísticas De Uso De Wordpress .**

Escribimos un post con las estadísticas de uso de Wordpress.

![imagen34](./img/34.png)

![imagen35](./img/35.png)

![imagen36](./img/36.png)

Entramos a dicho post.

![imagen37](./img/37.png)

![imagen38](./img/38.png)

---