___

# **UT1. A4. Sirviendo Aplicaciones Php Y Python.**

La actividad consiste en configurar 4 sitios web (virtual hosts) en nuestro servidor web Nginx, con las siguientes características.

___

# **Sitio Web 1.**

* **http://php.alu5904.me.**

Mostrar la aplicación demo_php.zip.

___

# **Sitio Web 2.**

* **http://now.alu5904.me.**

El código del programa python es el siguiente.

~~~

import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Testing Python over Nginx</h1>
    Today is: {today}
    <br>
    Now is: {now}
    """.format(
        today=datetime.datetime.now().strftime("%d/%m/%Y"),
        now=datetime.datetime.now().strftime("%H:%mh")
    )

~~~

El código debe residir en $HOME/now.

Se debe configurar supervisor para gestionar el proceso uwsgi.

Se debe probar los siguientes comandos, y ver cómo es la respuesta del navegador al acceder a la web:

~~~

* supervisorctl status
* supervisorctl start now
* supervisorctl stop now
* supervisorctl restart now

~~~
___
