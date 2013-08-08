# -*- coding: utf-8 -*-


###############################################################################
# This file contains settings for your whole project and is generated         #
# automatically when you do "django-admin.py startproject".                   #
#                                                                             #
# Most values are Django settings, erasing the default values you can find in #
# libs/django/conf/global_settings.py. A lot of original Django settings arez #
# not changed so you'll have to refer to global_settings.py to know their     #
# value.                                                                      #
#                                                                             #
# Some values are for others Django apps.                                     #
#                                                                             #
# Finally, some values are just made up for our own apps.                     #
#                                                                             #
# REMEMBER: this is just a regular Python file, which means you can put any   #
# Python code in it.                                                          #
#                                                                             #
# NOTE: the scope of this project is to show you how to do things in apps,    #
# not how to deploy Django. Therefor the settings content and layout fit      #
# this purpose and do not reflect how a production site should do it.         #
# I will specifically put a note when warning applys, and the first           #
# warning is: "You should have several settings files in a real project       #
# to seperate production, staging and developpement environnements"           #
#                                                                             #
###############################################################################


# Since it's a regular Python file, you can import stuff

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

import os

# We get the path of all this directories from the "path" module. The path.py
# file is something we code ourself, it's not provided by Django, but it's
# very useful to avoid hard coding all these paths.
from path import PROJECT_DIR, ROOT_DIR, TEMP_DIR


# Displays error messages on the Web page if something crashes
# WARNING: default value is True, you should always set it
# to False in production
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Where to send email alerts. You don't need that at the moments.
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS


# The database configuration is a big dictionary. It's the same place to
# configure postgresql, mysql, sqlite or oracle, and you can have several
# database configured for one project (one per dict key, where the dict key
# is the database name). You should at least have one "default" database.
# We will use sqlite because it works out of the box.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite'),
    }
}
# If you install the proper backends, you could also use exotic database such
# as MSAccess or Firebird


# List here all the URL from which you plan your website to be accessible from.
# E.G: if you plan to have this website available at ilovegiraffes.com, you
# should but it in there.
ALLOWED_HOSTS = [
 "127.0.0.1" # local web site (on my machine only)
]


# You can choose the timezone you site will be set to. If you set it to None,
# it will be set to your machine time zone. It recommand this settings, but
# on the strict condition your server time zone is set to UTC (which it should).
TIME_ZONE = None

# Unless you plan to do a site in your own langage only (in which case you
# would benefit from default formatting for time, date, monney, etc), you should
# let this default value and translate later.
LANGUAGE_CODE = 'en-us'

# A unique identifier for your site. It is used by the site framework
# to find your site name in the database. If you have several sites, increment
# it by one for each site. Usually you just need to let that alone.
SITE_ID = 1

# Do you want your text to be translatable in other langages ?
# If you don't, set it to False to gain some perf.
USE_I18N = True

# Do you want Django to translate dates, monney and numbers according to the
# locale ? If you don't, set it to False to gain some perf.
USE_L10N = True

# True by default. Set it to False. Store everything as UTC and deal with
# timezone manually using pytz. Really. TZ support sucks in Python stdlib:
# http://www.enricozini.org/2009/debian/using-python-datetime/
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
#
# We will probably not use it in this project, but I set it so you can see
# a way to do it. The directory does not exists for now.
MEDIA_ROOT = os.path.join(ROOT_DIR, 'var', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/", '/media/'
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#
# We will probably not use it in this project, but I set it so you can see
# a way to do it. The directory does not exists for now.
STATIC_ROOT = os.path.join(ROOT_DIR, 'var', 'static')


# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
# Put here a tuple of absolute path of any directory you want Django
# to detect automatically your static files (CSS, JS, images...).
# Each app 'static' directory is automatically added, no need to list it here.
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
# Just ignore this, you will not need this unless you store your static files
# on a CDN, amazon cloud or else.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# WARNING: set a different value in production, and don't commit it into a
# public repository.
SECRET_KEY = '2fhdcfk-0ctkijtc_rqtj2^qw56yc)6$^j4msj3%yn*ib@9ya_'

# List of callables that know how to import templates from various sources.
# Same as STATICFILES_FINDERS but for html template files.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Middleware are the Django mecanisme to apply a process to every request.
# These are the default ones, but you can write your own. You don't need
# too fiddle with middleware very often.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# The python import path to the main urls module. This is where you declare
# the root of all your urls for all your apps
ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
# For you, useful in production only.
WSGI_APPLICATION = 'project.wsgi.application'

# Same as STATICFILES_DIRS but for html template files. 'template' dirs
# in apps are automatically detected.
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of python import path of all the applications Django should load when
# it starts. It contains Django internal applications, additional pip installed
# applications and your own applications. These are all the same to Django,
# they're just regular importable Python modules.
# Installed applications have their static files, template files and models
# automatically detected.
INSTALLED_APPS = (

    # django apps

    'django.contrib.auth',  # password authentication
    'django.contrib.contenttypes',  # allow generic relations with the ORM
    'django.contrib.sessions',  # persistent sessions for each user
    'django.contrib.sites',  # site name in database
    'django.contrib.messages',  # set a message and display it to the user
    'django.contrib.staticfiles', # serve static file in dev mode
    'django.contrib.admin', # an administration tool for the database

    # our apps (their are just regular importable Python modules)

    'app1_hello',
    'app2_hello_again',
    'app3_basic_routing',
    'app4_links',
    'app5_get_post_and_cookies',

    # ignore this, it's the app to display the listing of other apps
    'ignore_me',
)

# Django uses the Python log standard facility, and this dictionary is passed
# to dictConfig (http://docs.python.org/2/library/logging.config.html).
# This is not the original one, this one allow you to log to the console
# and a file in temp dir.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { # what to dump in each log
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': { # mandatory since django 1.5
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': { # send a mail to admins
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{ # print on the console
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file':{ # write in a temp file
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(TEMP_DIR, 'project.django.log'),
            'maxBytes': 1000000,
            'backupCount': 1,
        },
    },
    'loggers': {
        'django.request': { # send an email to admins if a request fails
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.project': { # write manually to the console and the tempfile
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#################################################################################
# SETTINGS FOR OTHER APPS                                                       #
#################################################################################

# NONE YET

#################################################################################
# SETTINGS YOUR OWN APPS                                                        #
#################################################################################

# NONE YET

