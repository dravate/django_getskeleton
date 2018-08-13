import sys
import os
from django.urls import re_path
from django.shortcuts import render
from django.conf  import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
print (BASE_DIR)

def index(request):
    return render(request, 'getskeleton.html')

urlpatterns = [ re_path(r'^$', index), ]

settings.configure (
   DEBUG=True,
   SECRET_KEY = 'I_AM_SECRETE',
   ROOT_URLCONF=__name__,
   INSTALLED_APPS = ['django.contrib.staticfiles',],
   MIDDLEWARE = [
                 'django.middleware.common.CommonMiddleware',
                 'django.middleware.csrf.CsrfViewMiddleware',
                 'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ],
   TEMPLATES = [
      {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        #'APP_DIRS': True,
        'OPTIONS': {
        },
      },
   ],
  STATIC_URL = '/static/',
  STATICFILES_DIRS = ['/app/django_blogs/django_getskeleton/static', ],
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)  
