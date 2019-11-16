
###############################################################################
# This file contains settings for your whole project and is generated         #
# automatically when you do "django-admin.py startproject".                   #
#                                                                             #
# Most values are Django settings, overwriting the default values you can     #
# find in libs/django/conf/global_settings.py. A lot of original Django       #
# settings are not changed so you'll have to refer to global_settings.py to   #
# know their values.                                                          #
#                                                                             #
# REMEMBER: this is just a regular Python file, which means you can put any   #
# Python code in it.                                                          #
#                                                                             #
# NOTE: the scope of this project is to show you how to do things in apps,    #
# not how to deploy Django. Therefor the settings content and layout fit      #
# this purpose and do not reflect how a production site should do it.         #
# I will specifically put a note when warning applies.                        #
#                                                                             #
###############################################################################


# Since it's a regular Python file, you can import stuff

import os
import sys
import os
import tempfile

from pathlib import Path

# We get the 'settings.py' file path (the __FILE__ variable contains
# automatically the path of the current file) and we transform this string
# to unicode in case you got non ASCII characters in this name (
# sys.getfilesystemencoding() get us the file system encoding which can be
# different for Windows, Mac or Linux)
THIS_FILE = Path(__file__).absolute().resolve()

# We dynamically create these settings, giving us the absolute path
# to the project directory, the root directory containing all our work
# and any other directory we might need
PROJECT_DIR = THIS_FILE.parent
BASE_DIR = PROJECT_DIR.parent
APPS_DIR = BASE_DIR / 'apps'
TEMP_DIR = Path(tempfile.gettempdir())

# We add the app directory to the PYTHON PATH, so we can import each
# package without prefixing them with the parent package name. This mimic the
# behavior we would have if they were at the root directory or installed with
# pip.
#
# E.G: we can do from "app1_hello.views import hello" instead of
#      "from apps.app1_hello.views import hello" or "import django" instead of
#      "from libs import django"
sys.path.append(str(APPS_DIR))

# Make this unique, and don't share it with anybody.
# WARNING: set a different value in production, and don't commit it into a
# public repository.
SECRET_KEY = '2fhdcfk-0ctkijtc_rqtj2^qw56yc)6$^j4msj3%yn*ib@9ya_'

# Displays error messages on the Web page if something crashes
# WARNING: default value is True, you should always set it
# to False in production
DEBUG = True

# List here all the URL from which you plan your website to be accessible from.
# E.G: if you plan to have this website available at yourwebsiteaddress.com, you
# should put it in there.
ALLOWED_HOSTS = [
 "127.0.0.1",
 "localhost" # local web site (on my machine only)
]

# List of python import path of all the applications Django should load when
# it starts. It contains Django internal applications, additional pip installed
# applications and your own applications. These are all the same to Django,
# they're just regular importable Python modules.
# Installed applications have their static files, template files and models
# automatically detected.
INSTALLED_APPS = (

    # django apps

    'django.contrib.admin', # an administration tool for the database
    'django.contrib.auth',  # password authentication
    'django.contrib.contenttypes',  # allow generic relations with the ORM
    'django.contrib.sessions',  # persistent sessions for each user
    'django.contrib.messages',  # set a message and display it to the user
    'django.contrib.staticfiles', # serve static file in dev mode
    'django.contrib.humanize', # tools to print values in a human readable way

    # our apps (their are just regular importable Python modules)

    'app1_hello',
    'app2_hello_again',
    'app3_basic_routing',
    'app4_links',
    'app5_get_post_and_cookies',
    'app6_template_tools',
    'app7_static_files',
    'app8_base',

    # ignore this, it's the app to display the listing of other apps
    'ignore_me',
)

# Middleware are the Django mechanism to apply a process to every request.
# These are the default ones, but you can write your own. You don't need
# to fiddle with middleware very often.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# The python import path to the main URLs module. This is where you declare
# the root of all your URLs for all your apps
ROOT_URLCONF = 'project.urls'


# How Django find your templates files (the HTML files)
TEMPLATES = [
    {
        # Look for them locally
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Additional directory where to look for them
        'DIRS': [],
        # Look in every "templates" dir in every apps
        'APP_DIRS': True,
        'OPTIONS': {
            # Callables putting data automatically in the template
            # context. By default the template can see the DEBUG constant,
            # the authenticated user, the request object and flash messages
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Python dotted path to the WSGI application used by Django's runserver.
# For you, useful in production only.
WSGI_APPLICATION = 'project.wsgi.application'


# The database configuration is a big dictionary. It's the same place to
# configure postgresql, mysql, sqlite or oracle, and you can have several
# databases configured for one project (one per dict key, where the dict key
# is the database name). You should at least have one "default" database.
# We will use sqlite because it works out of the box.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(PROJECT_DIR / 'db.sqlite'),
    }
}
# If you install the proper backends, you could also use exotic database such
# as MSAccess or Firebird

# List of the callables used to validate
# passwords when creating a user accoun.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Unless you plan to do a site in your own language only (in which case you
# would benefit from default formatting for time, date, monney, etc), you should
# let this default value and translate later.
LANGUAGE_CODE = 'en-us'

# You can choose the timezone you site will be set to. You usually wants to keep "UTC" and manually format the date to the user timezone.
TIME_ZONE = 'UTC'

# Do you want your text to be translatable in other languages ?
# If you don't, set it to False to gain some performance.
USE_I18N = True

# Do you want Django to translate dates, money and numbers according to the
# locale ? If you don't, set it to False to gain some performance.
USE_L10N = True

# Should Djagno use naive datetime objects, or objects that now about time zone ?
# Use True just in case, it's easier to say True first, and never use it than the reverse.
USE_TZ = True

# URL prefix for static files such as images, css, js, etc
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
