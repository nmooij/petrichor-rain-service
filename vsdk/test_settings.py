from .settings import *

# DATABASES = {
      #  "default": {
        #    "ENGINE": "django.db.backends.sqlite3",
        #    "NAME": ":memory:",
       #     }
       # }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB',
        'USER': 'Admin',
        'PASSWORD': 'SuperUser',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        "NAME": ":memory:",
   }
}       

EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
