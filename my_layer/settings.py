import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "<SECRET_KEY_HERE>"

INSTALLED_APPS = (
    'django.contrib.auth',          # Only needed if you are using a custom or built-in django auth models 
    'django.contrib.contenttypes',  # Only needed if you are using content types django objects 
    "<APP_LABEL_HERE>",
)

# This configuration is for a db 
DATABASES = {
    'default': {
        'ENGINE': "<DB_ENGINE_HERE>",
        'NAME': "<DB_NAME_HERE>",
        'USER': "<DB_USER_HERE>",
        'PASSWORD': "<DB_PASSWORD_HERE>",
        'HOST': "<DB_HOST_HERE>",
        'PORT': "<DB_PORT_HERE>",
    }
}
