# Crear entorno virtual
python3 -m venv env

# Actualizar pip
pip install --upgrade pip

# Activar entorno virtual
source env/bin/activate

# Para desactivarlo
deactivate

# Verificar versión de django
python -m django --version

# Instalar django
pip install Django==4.0.6

# Creamos el proyecto en la ruta actual
django-admin startproject ecommerce .

# Lanzar servidor django
python manage.py runserver

# Aplicar migraciones
python manage.py migrate

# Creating superuser
python manage.py createsuperuser

# Superuser created
User: jortega
Pass: admin

# Creating our first django app
django-admin startapp usuarios

# Añadimos nuestra app en el archivo settings.py del proyecto

# Crear y ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

/////////////////// PARA TRABAJAR CON MEDIA FILES ///////////////////
# Añadimos el siguiente código al archivo settings.py
# Media files configuration
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Editamos el archivo urls.py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('usuario/', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Finalmente ejecutamos el siguiente comando en la consola

python manage.py collectstatic

/////////////////// EJECUTAR MIGRACION SELECTIVA ///////////////////
# Ver y ejecutar la migración
python manage.py sqlmigrate blog 0001

# Para acceder al shell de django
python manage.py shell

/////////////////// CAMBIAR GESTOR DE USUARIOS DJANGO ///////////////////
# En el modelo de la app accounts
-- Creammos las clases para gestionar las cuentas
-- En el archivo settings.py añadimos la siguiente línea

AUTH_USER_MODEL = 'accounts.Account'

/////////////////// Entorno de trabajo para un equipo ///////////////////
# Creamos una carpeta llamada settings dentro de la carpeta del proyecto

python manage.py runserver --settings=empleado.settings.local

# Para evitar ejecutar la línea anterior cada vez que querramos lanzar el proyecto
-- Editamos nuestro archivo manage.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empleado.settings.local')

# Para organizar mejor las aplicaciones de django:
-- Creamos una carpeta llamada applications
-- cd applications
-- Activamos el entorno virtual
-- Ejecutamos el siguiente comando para crear una app nueva

django-admin startapp <nombre de app>

-- Dentro de la carpeta de la nueva app, buscamos el archivo apps.py
-- Modificamos la siguiente línea

name = 'applications.empleados'

# Para organizar mejor los archivos .html
-- Creamos una carpeta llamada templates en la raíz del proyecto
-- Vamos a la carpeta del proyecto luego a: settings/base.py
-- Editamos la línea agregando un .parent adicional

BASE_DIR = Path(__file__).resolve().parent.parent.parent

-- Eliminamos la carpeta templates dentro de las apps
-- Editamos el archivo views.py para añadir el nombre de la app