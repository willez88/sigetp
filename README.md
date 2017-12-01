# SIGETP

Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP): Se encarga de registrar información acerca de como son las condiciones de las viviendas y sus grupos familiares en los consejos comunales

# Pre-requisitos

Para el correcto funcionamiento del __SIGETP__ se requiere tener instalado previamente los siguientes paquetes:

    apache2
    git
    postgresql
    python3.6
    virtualenv

# Proceso de instalación

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

    ~# apt install git python3.6 postgresql phppgadmin virtualenv

Crear las siguientes carpetas

    ~$ mkdir Programación

Dentro de Programación, ejecutar

    ~$ mkdir EntornosVirtuales ProyectosDjango Repositorios

Dentro de la carpeta EntornosVirtuales, crearemos nuestro entorno

    ~$ virtualenv -p python3.6 sigetp

Para activar el entorno

    ~$ source sigetp/bin/activate

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate

Nos movemos a la Carpeta Repositorios para descargar el sistema con el siguiente comando

    ~$ git clone https://github.com/willez88/sigetp.git

Copiamos la carpeta que se creó hacia ProyectosDjango, allí estará el servidor de desarrollo. De momento tendremos nuestras carpetas estructuradas de la siguiente manera:

    // Entorno virtual
    Programación/EntornosVirtuales/sigetp

    // Servidor de desarrollo
    Programación/ProyectosDjango/sigetp

    // Sistema descargado de los repositorios
    Programación/Repositorios/sigetp

Crear la base de datos para el __SIGETP__

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de postgresql
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario postgres y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: sigetp

Creada la base de datos, moverse a la carpeta donde está el servidor de desarrollo

Instalamos los requemientos que el sistema necesita en el entorno virtual

    ~$ pip install -r requirements.txt

Hacer las migraciones

    ~$ python manage.py makemigrations base usuario vivienda grupo_familiar persona

    ~$ python manage.py migrate

Crear usuario administrador del __SIGETP__

    ~$ python manage.py createsuperuser

Poblar las tablas de la base de datos que lo requieran

    ~$ python manage.py loaddata initial_data.json

Ejecutar el servidor de django

    ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para usar el sistema
