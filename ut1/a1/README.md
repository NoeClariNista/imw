# **UT1 - A1 : Mis series favoritas.**

En esta actividad he creado una página web que enlaza con mis 5 series favoritas.

Para acceder a dicha página solo se tiene que pinchar en el siguiente enlace:

**[My Favourite Series](http://alu5904.me/series/).**

## **1. Creación Del Directorio Series.**

Lo que queremos realizar es que en nuestro home, donde tenemos nuestro usuario alu5904, tener un Virtual Host llamado series, el cual nos muestre cuando accedemos a **alu5904.me/series** nuestra web con nuestras 5 series favoritas.

Añadiremos el fichero de configuración de Nginx que tratará las peticiones que se hagan al nombre de dominio alu5904.me/series.

Creamos un fichero dentro de Nginx y en concreto en los sites-available, donde añadiremos la información para que se vaya creando el dominio.

![imagen01](./img/01.png)

![imagen02](./img/02.png)

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde Nginx, en concreto desde los sites-enabled.

![imagen03](./img/03.png)

Tenemos que recargar la configuración de Nginx para que los cambios surtan efecto.

![imagen04](./img/04.png)

Por último, creamos una carpeta dentro de webapps de series donde irá el index.html de nuestro Vitual Host de series.

![imagen05](./img/05.png)

![imagen06](./img/06.png)

## **2. Fondo.**

Descargamos el fondo que queramos de la página web de Subtle Patterns. Lo descargamos en la máquina de desarrollo, luego utilizamos el comando scp y lo copiamos en la máquina de producción.

![imagen07](./img/07.png)

Instalamos unzip para poder descomprimir el archivo y luego lo descomprimimos.

![imagen08](./img/08.png)

![imagen09](./img/09.png)

Finalmente comprobamos que se encuentra en nuestro directorio de series y dentro de nuestro archivo descomprimido vemos que se encuentra la imagen de fondo.

![imagen10](./img/10.png)

![imagen11](./img/11.png)

## **3. Imágenes.**

Antes que nada, para poder poner más imágenes en nuestra máquina de producción, creamos una carpeta para guardar todas las imágenes de las portadas de las series y el fondo anteriormente descargado.

![imagen12](./img/12.png)

Volvemos a la máquina de desarrollo y descargamos todas las portadas de las series que he elegido. Luego las copiamos a mi máquina de producción.

![imagen13](./img/13.png)

Comprobamos que las imágenes se encuentran en la carpeta de images.

![imagen14](./img/14.png)

Copiamos el fondo y lo metemos también en esta carpeta de images.

![imagen15](./img/15.png)

![imagen16](./img/16.png)

## **4. Página Web.**

Para mejorar la página web, que he creado con mis 5 series favoritas, utilizo el Nginx y edito el fichero de index.html para que se cree la página web.

Cada vez que vaya editando algo en el fichero tengo que recargar el servicio de Nginx.

![imagen17](./img/17.png)

Después de trabajar en el fichero el código html nos quedaría como en esta imagen.

![imagen18](./img/18.png)

Finalmente la página web nos quedaría como se ve a continuación.

![imagen19](./img/19.png)
