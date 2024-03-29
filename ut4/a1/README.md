___

# **UT4 - A1: Implantación De Wordpress.**

---

## **1. Instalación de Wordpress.**

Vamos a instalar un sitio web Wordpress en nuestra máquina. Para ello accedemos a la máquina de producción vía ssh.

![imagen01](./img/01.png)

Wordpress necesita un usuario y una contraseña para acceder a una base de datos. Para ello, usaremos el intérprete de MySQL.

![imagen02](./img/02.png)

Tenemos que crear la base de datos, el usuario y asignar privilegios.

![imagen03](./img/03.png)

Descargamos el código fuente de Wordpress desde su página web.

![imagen04](./img/04.png)

Descomprimimos el código y lo copiamos en `/usr/share`.

![imagen05](./img/05.png)

![imagen06](./img/06.png)

Ahora tenemos que establecer los permisos necesarios para que el usuario web www-data pueda usar estos ficheros.

![imagen07](./img/07.png)

Debemos especificar el nombre de la base de datos, el usuario y la contraseña, para que Wordpress pueda usarlos.

![imagen08](./img/08.png)

![imagen09](./img/09.png)

Para que nuestro sitio Wordpress sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del Servidor web Nginx.

Queremos acceder a nuestro Wordpress desde la url `wordpress.alu5904.me`. Para ello tendremos que crear un nuevo virtual host de la siguiente manera.

![imagen10](./img/10.png)

![imagen11](./img/11.png)

Enlazamos la configuración para que el virtual host esté disponible.

![imagen12](./img/12.png)

Recargamos el Servidor web Nginx para que los cambios surtan efecto.

![imagen13](./img/13.png)

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

## **2. Instalación Y Activación De Un Tema.**

Instalamos y activamos un tema gratuito.

Para instalar un nuevo tema tenemos que ir a Apariencia y ahí añadir un tema nuevo.

![imagen19](./img/19.png)

Elegimos el tema que más nos guste, en mi caso Sparkling.

![imagen20](./img/20.png)

Una vez instalado le damos a Activar.

![imagen21](./img/21.png)

Ya tenemos instalado y activado el tema.

![imagen22](./img/22.png)

Vamos a `wordpress.alu5904.me` y comprobamos el tema instalado.

![imagen23](./img/23.png)

Para personalizar nuestro tema volvemos a ir a Apariencia y le damos a Personalizar.

![imagen24](./img/24.png)

Dentro de personalizar hacemos algunos cambios para poder verlos.

![imagen25](./img/25.png)

Volvemos a ir a `wordpress.alu5904.me` y comprobamos los cambios hechos.

![imagen26](./img/26.png)

---

## **3. Ajuste De Permalinks.**

Activamos esta opción dentro de la interfaz administrativa de Wordpress, concretamente en Ajustes, enlaces permanentes.

Seleccionamos el ajuste Día y nombre. Pulsamos en Guardar cambios.

![imagen27](./img/27.png)

Ahora debemos indicar a Nginx que procese estas URLs.

![imagen28](./img/28.png)

![imagen29](./img/29.png)

Recargamos la configuración de Nginx.

![imagen30](./img/30.png)

Una ventaja que tiene este método es que podemos acceder a la zona administrativa utilizando la URL `http://wordpress.alu5904.me/admin`.

![imagen31](./img/31.png)

![imagen32](./img/32.png)

---

## **4. Post Con Las Estadísticas De Uso De Wordpress.**

Escribimos un post con las estadísticas de uso de Wordpress.

![imagen33](./img/33.png)

Una vez escrito el post lo publicamos.

![imagen34](./img/34.png)

![imagen35](./img/35.png)

Entramos a dicho post.

![imagen36](./img/36.png)

![imagen37](./img/37.png)

---
