# -*- coding: utf-8 -*-


#################################################################################
# Ce fichier contient les paramètres pour le projet complet et est généré       #
# automatiquement quand vous faites "django-admin.py startproject".             #
#                                                                               #
# La plupart des valeurs sont des paramètres de Django, écrasant les valeurs    #
# que vous pouvez trouver dans libs/django/conf/global_settings.py. La plupart  #
# de la configuration originale de Django n'est pas modifiée, donc vous devrez  #
# vous référer à global_settings.py pour connaitre les autres valeurs.          #
#                                                                               #
# D'autres valeurs sont à destinations d'autres apps Django.                    #
#                                                                               #
# Enfin, quelques valeurs sont celles que nous avons créées pour nos propres    #
# apps Django.                                                                  #
#                                                                               #
# SOUVENEZ-VOUS : c'est juste un fichier Python ordinnaire, ce qui signifie que #
# vous pouvez mettre n'importe quel code Python dedans.                         #
#                                                                               #
# NOTE : le but de ce projet est de vous montrer comment faire des choses       #
# dans les apps, pas comment déployer Django. De ce fait, le contenu des        #
# paramètres et leurs organisations sont orientés dans ce but et ne reflètent   #
# pas ce que vous devriez faire en production.                                  #
# Je mettrais des notes là où il faudra faire attention, et la première         #
# d'entre elles est : "Vous devriez avoir plusieurs fichiers de settings        #
# dans un vrai projet pour séparer la produciton, la préproduction et le        #
# développement."                                                               #
#################################################################################



# Puisque c'est un fichier Python ordinaire, on peut y faire des imports

# Ceci va forcer toutes les chaînes à être de type 'unicode', même si on
# n'utilise pas le préfixe 'u'
from __future__ import unicode_literals


import os
import sys
import tempfile

# Cette partie est un peu compliquée et n'est pas forcément nécessaire
# à votre projet, mais elle rend le projet complètement portable car tous
# les chemins de tous les dossiers sont crées dynamiquement au lieu
# d'être écris en dur.

# On récupère le chemin du fichier settings.py (la variable __FILE__ contient
# automatiquement le chemin du fichier en cours) et on transforme la chaîne
# en unicode au cas où il y ait des accents dans ce nom
# (sys.getfilesystemencoding() nous donnes l'encoding du système de fichier
# qui peut être différent sous Windows, Mac ou Unix)
FS_ENCODING = sys.getfilesystemencoding()
SETTINGS_FILE = __file__.decode(FS_ENCODING)

# Nous créons ces paramètres dynamiquement, ce qui nous donne les chemins
# absolus vers le dossier du projet et le dossier racine contenant tout
# notre travail ainsi que tout autre dossier dont nous pourrions avoir
# besoin.
PROJECT_DIR = os.path.dirname(os.path.realpath(os.path.abspath(SETTINGS_FILE)))
ROOT_DIR = os.path.dirname(PROJECT_DIR)
APPS_DIR = os.path.join(ROOT_DIR, 'apps')
libs_DIR = os.path.join(ROOT_DIR, 'libs')
TEMP_DIR = tempfile.gettempdir().decode(FS_ENCODING)


# Nous ajoutons les dossiers "apps" et "libs" au PYTHON PATH, de telle sorte
# que nous puissions importer chaque package sans avoir à les préfixer du nom
# du package parent. Ceci imite le comportement que nous aurions si ils
# étaient à la racine ou installés avec pip.
#
# Ex: nous pouvons importer "from app1_hello.views import hello" plutôt que
#     "from apps.app1_hello.views import hello" ou "import django" à la place
#     de "from libs import django"
#
# Quand vous avez un petit projet, vous pouvez évitez cela et mettre toutes
# les apps dans le dossier racine comme dans le tutorial Django officiel, mais
# dans un gros projet avec beaucoup d'apps, on les met généralement toutes
# dans un dossier "apps" comme nous venons de faire, donc c'est une bonne
# chose à connaître.
sys.path.append(libs_DIR)
sys.path.append(APPS_DIR)


# Affiche des message d'erreurs sur la page Web si quelque chose plante.
# ATTENTION : la valeur par défaut est True, vous devriez toujours la mettre
# sur False en production.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Où envoyer des alertes emails. Vous n'en avez pas besoin pour le moment.
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS


# La configuration de la base de données est un gros dictionnaire. On
# configure postgresql, mysql, sqlite ou oracle au même endroit, et on peut
# avoir plusieurs base de données configurées pour un projet (une par clé du
# dictionnaire, la clé étant le nom de la base de données). Vous devez au
# moins avoir une base de données nommée "default".
# Nous allons utiliser sqlite car cela fonctionne sans plus de configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite'),
    }
}
# Si vous installez votre propre backend, vous pouvez aussi utiliser des
# base de données plus exotiques telles que MSAccess ou Firebird


# Listez ici les URL depuis lesquelles vous souhaitez que votre site soit
# accessible.
# Ex : si vous voulez que votre site soit accessible depuis jaimelesgiraffes.com
# vous devriez le mettre ici.
ALLOWED_HOSTS = [
 "127.0.0.1" # site web local (uniquement sur ma machine)
]


# Vous pouvez choisir le fuseau horaire de votre site. Si vous mettez None,
# il sera configuré pour utiliser celui de votre machine. Je recommande
# cela, mais à la condition que l'heure de votre server soit réglé sur UTC
# (ce qui est recommandé).
TIME_ZONE = None

# À moins de vouloir développer un site dans votre langue uniquement (dans ce
# cas vous bénéficierez du formatage par défaut de l'heure, des dates, de
# l'argent, etc), vous devriez laisser cette valeur et traduire le site plus
# tard.
LANGUAGE_CODE = 'en-us'

# Un identifiant unique pour le site. Utilisé par le framework "site" pour
# identifier le nom du site dans la base de données. Si vous avez plusieurs
# sites, incrémentez cette valeur de un pour chaque site. En général, on peut
# ne pas la modifier.
SITE_ID = 1

# Voulez-vous que le texte soit traductible dans d'autres langues ? Si non,
# vous pouvez mettre False pour gagnez un peu de perf.
USE_I18N = True

# Voulez-vous que Django formate les dates, l'argent et les nombres selon
# culture / langue en cours ? Si non, vous pouvez mettre False pour gagnez un
# peu de perf.
USE_L10N = True

# True par défaut. Mettez le sur False. Stockez tout en UTC, et gérez les
# fuseaux horaires manuellement en utilisant pytz. Sérieusement. Le support
# des fuseaux horaires craint avec la lib standard de Python :
# # http://www.enricozini.org/2009/debian/using-python-datetime/
USE_TZ = False


# Chemin absolu du dossier qui va contenir les fichiers uploadés par les
# utilisateur.
# # Exemple: "/var/www/example.com/media/"
#
# Ne sera probablement jamais utilisé par ce projet, mais je le laisse pour
# que vous puissiez voir une manière de faire. Le dossier n'existe pas pour
# le moment.
MEDIA_ROOT = os.path.join(ROOT_DIR, 'var', 'media')

# URL gérant les fichiers servis depuis MEDIA_ROOT. Soyez certains de mettre
# un slash final.
# Exemples: "http://example.com/media/", "http://media.example.com/", '/media/'
MEDIA_URL = "/media/"

# Chemin absolu vers le dossier dans lequel les fichiers statiques seront
# collectés. Ne metez rien dans ce dossier vous-même, stockez vos fichiers
# statiques dans chaque dossier "static" de chaque app et dans STATICFILES_DIRS.
# # Exemple: "/var/www/example.com/static/"
#
# Ne sera probablement jamais utilisé par ce projet, mais je le laisse pour
# que vous puissiez voir une manière de faire. Le dossier n'existe pas pour
# le moment.
STATIC_ROOT = os.path.join(ROOT_DIR, 'var', 'static')

# Prefixe de l'URL qui va servir les fichiers statiques.
# Exemple: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Un tuple qui contient des chemins absolus de tous les dossiers que l'on
# souhaites que Django détecte automatiquement comme contenant des fichiers
# statiques (CSS, JS, images...).
# Chaque dossier 'static' de chaque app est automatiquement ajouté, donc
# pas la peine de les lister ici.
STATICFILES_DIRS = (
    # Mettez ici des chaînes comme "/home/html/static" ou "C:/www/django/static".
    # Utilisez toujours des slash, même sous Windows.
    # Utilisez des chemins absolus, par relatifs.
)

# La liste des classes chargées de trouver les fichiers statiques dans divers
# endroits.
# Vous pouvez l'ignorer, vous n'en aurez pas besoin à moins de stocker vos
# fichiers statiques sur un CDN, le cloud d'Amazon ou autre.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Soyez sûr que ceci est unique, et ne le partagez avec personne.
# ATTENTION : mettez une valeur différente en production, et ne sauvegardez
# pas ça dans un dépôt publique.
SECRET_KEY = '2fhdcfk-0ctkijtc_rqtj2^qw56yc)6$^j4msj3%yn*ib@9ya_'

# Liste de callables qui savent comment importer les templates depuis divers
# sources. Comme STATICFILES_FINDERS mais pour les templates HTML.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Les middlewares sont le mécanisme de Django pour appliquer un traitement à
# chaque requête. Vous voyez ici les valeurs par défault, mais vous pouvez
# écrire les vôtres. Vous n'aurez pas souvent besoin de jouer avec les
# middlewares.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Décommentez cette ligne pour activer la protection contre le clickjacking
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Le chemin d'import Python du module principal d'urls. C'est dans celui-ci
# qu'on déclare la racine de toutes les URLS de toutes les apps.
ROOT_URLCONF = 'project.urls'

# Le chemin d'import du module de l'application WSGI utilisé par Django.
# Pour vous, utile uniquement pour la production.
WSGI_APPLICATION = 'project.wsgi.application'

# Comme STATICFILES_DIRS mais pour les templates HTML. Les dossiers 'templates'
# de chaque app sont détectés automatiquement.
TEMPLATE_DIRS = (
    # Mettez des chaînes comme "/home/html/django_templates"
    # ou "C:/www/django/templates".
    # Utilisez toujours des slash, même sous Windows.
    # Utilisez des chemins absolus, pas relatifs.
)

# Liste de chemin d'import Python de toutes les applications que Django
# doit charger au démarrage. Elle contient les applications internes de Django
# celles installées en plus avec pip et vos propres applications. Pour Django,
# c'est la même chose.
# Les applications installées ont leurs fichiers statiques, leurs templates et
# modèles détectés automatiquement.
INSTALLED_APPS = (

    # applications Django

    'django.contrib.auth',  # authentification via password
    'django.contrib.contenttypes',  # permet les relations génériques via l'ORM
    'django.contrib.sessions',  # sessions persistantes pour les utilisateurs
    'django.contrib.sites',  # nom du site en base de données
    'django.contrib.messages',  # créer et afficher un message pour l'utilisateur
    'django.contrib.staticfiles', # servir les fichiers statiques en dev
    'django.contrib.admin', # outil d'administration de la base de données

    # nos applications

    'app1_hello',
    'app2_hello_again',

    # vous pouvez ignorer cela, c'est l'app qui liste les autres apps
    'ignore_me',
)

# Django utilise le mécanisme de log standard de Python et ce dictionnaire
# est donc passé à dictConfig (http://docs.python.org/2/library/logging.config.html).
# Ce n'est pas la version originale, celui-ci permet de logger dans la console
# et dans un fichier temporaire.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { # que mettre dans chaque log
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': { # obligatoire depuis django 1.5
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': { # envoyer un email aux admins
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{ # afficher dans la console
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file':{ # écrire dans un fichier temporaire
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(TEMP_DIR, 'project.django.log'),
            'maxBytes': 1000000,
            'backupCount': 1,
        },
    },
    'loggers': {
        'django.request': { # envoyer un email aux admins si une requête échoue
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.project': { # écrire manuellement sur la console et dans un fichier temporaire
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



#################################################################################
# PARAMÈTRES POUR LES AUTRES APPLICATIONS                                       #
#################################################################################

# AUCUN POUR LE MOMENT

#################################################################################
# PARAMÈTRES POUR NOS PROPRES APPLICATIONS                                      #
#################################################################################

# AUCUN POUR LE MOMENT
