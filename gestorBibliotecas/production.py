from .settings import *
import os

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

hostname = os.environ['DBHOST']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.getenv('DB_NAME', 'gestorBibliotecas'),
		'USER': os.getenv('DB_USER', 'django'),
		'PASSWORD': os.getenv('DB_PASS', 'django'),
		'HOST': os.getenv('DB_HOST' + ".postgres.database.azure.com", 'localhost'),
		'PORT': os.getenv('DB_PORT', '3306'),
	}
}