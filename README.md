Para poder utilizar la API de Django tenemos que seguir los siguientes pasos:

1. Crear una base de datos en PostgresSQL con el nombre: db_cheap_maps
2. Modificar nuestras credenciales de nuestra base de datos en el archivo CheapMaps/setting.py

    DATABASES = {
    'default': {
        #Driver de postgresSQL
        'ENGINE': 'django.db.backends.postgresql',
        #Nombre de la base de datos
        'NAME': 'db_cheap_maps',
        #Usuario de postgres
        'USER': 'postgres',
        #Contraseña de postgres
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
   
3. En el archivo settings.py en esta parte del codigo poner la IP de nuestra computadora para servidor local:
   ALLOWED_HOSTS = ['192.168.1.68', '172.20.10.2']
5.  Los modelos que tengamos en Django REST Framework pasarlos a postgresSQL:
     python manage.py migrate
     python manage.py makemigrations
6. Correr el servidor con: python manage.py runserver 0.0.0.0:8000
