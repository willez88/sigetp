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

    ~$ mkdir python

Entrar a la carpeta python y hacer lo siguiente

    ~$ cd python/

    ~$ mkdir entornos_virtuales proyectos_django

Entrar a entornos_virtuales

    ~$ cd entornos_virtuales/

    ~$ mkdir django

Desde el terminal, moverse a la carpeta django y ejecutar

    ~$ cd django/

    ~$ virtualenv -p python3 sigetp

Para activar el entorno

    ~$ source sigetp/bin/activate

Nos movemos a la carpeta proyectos_django, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (sigetp) ~$ cd ../../proyectos_django/

    (sigetp) ~$ git clone https://github.com/willez88/sigetp.git

    (sigetp) ~$ cd sigetp/

    (sigetp) ~$ cp sigetp/settings.default.py sigetp/settings.py

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/python/entornos_virtuales/django/sigetp

    // Servidor de desarrollo
    Programación/python/proyectos_django/sigetp

Instalar las dependencias de css y js: moverse a la carpeta static y ejecutar

    (sigetp) ~$ cd static/

    // Usa el archivo package.json para instalar lo que está configurado allí
    (sigetp) ~$ npm install

    // Terminado el proceso volver a la carpeta raíz del proyecto
    (sigetp) ~$ cd ../

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

    (sigetp) ~$ pip install -r requirements/dev.txt

Hacer las migraciones

    (sigetp) ~$ python manage.py makemigrations base user living_place family_group person

    (sigetp) ~$ python manage.py migrate

Crear usuario administrador del __sigetp__

    (sigetp) ~$ python manage.py createsuperuser

Poblar las tablas de la base de datos que lo requieran

    (sigetp) ~$ python manage.py loaddata initial_data.json initial_data_group.json 1_country.json 2_state.json 3_city.json 4_municipality.json 5_parish.json 6_communal_council.json

Ejecutar el servidor de django

    (sigetp) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para usar el sistema
