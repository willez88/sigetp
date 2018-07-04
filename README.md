# SIGETP

Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP): Se encarga de registrar información acerca de como son las condiciones de las viviendas y sus grupos familiares en los consejos comunales

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Probado en Debian y Ubuntu. Instalar los siguientes programas

    ~# apt install git graphviz graphviz-dev libjpeg-dev postgresql phppgadmin python3-dev virtualenv zlib1g-dev

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ cd Programación/

    ~$ mkdir Python

Entrar a la carpeta Python y hacer lo siguiente

    ~$ cd Python/

    ~$ mkdir EntornosVirtuales ProyectosDjango

Entrar a EntornosVirtuales

    ~$ cd EntornosVirtuales/

    ~$ mkdir Django

Desde el terminal, moverse a la carpeta Django y ejecutar

    ~$ cd Django/

    ~$ virtualenv -p python3 sigetp

Para activar el entorno

    ~$ source sigetp/bin/activate

Nos movemos a la carpeta ProyectosDjango, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (sigetp) ~$ cd ../../ProyectosDjango/

    (sigetp) ~$ git clone https://github.com/willez88/sigetp.git

    (sigetp) ~$ cd sigetp/

    (sigetp) ~$ cp sigetp/settings.py_example sigetp/settings.py

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/Python/EntornosVirtuales/Django/sigetp

    // Servidor de desarrollo
    Programación/Python/ProyectosDjango/sigetp

Instalar las dependencias de css y js: moverse a la carpeta static y ejecutar

    (sofi) ~$ cd static/

    // Usa el archivo package.json para instalar lo que está configurado allí
    (sofi) ~$ npm install

    // Terminado el proceso volver a la carpeta raíz del proyecto
    (sofi) ~$ cd ../

Crear la base de datos para el __SIGETP__

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de postgresql
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario postgres y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: sigetp

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (sigetp) ~$ pip install -r requirements.txt

Para instalar los requerimientos de forma local

    (sigetp) ~$ pip install requirements/pip/Django-2.0.3.tar.gz requirements/pip/django-extensions-2.0.6.tar.gz requirements/pip/Pillow-5.0.0.tar.gz requirements/pip/psycopg2-2.7.4.tar.gz

Hacer las migraciones

    (sigetp) ~$ python manage.py makemigrations base usuario vivienda grupo_familiar persona

    (sigetp) ~$ python manage.py migrate

Crear usuario administrador del __SIGETP__

    (sigetp) ~$ python manage.py createsuperuser

Poblar las tablas de la base de datos que lo requieran

    (sigetp) ~$ python manage.py loaddata 1_country.json 2_state.json 3_municipality.json 4_city.json 5_parish.json 6_communal_council.json

Ejecutar el servidor de django

    (sigetp) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para usar el sistema
