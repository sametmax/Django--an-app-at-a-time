
#################################################################################
# Ce fichier contient les paramètres pour le projet complet et est généré       #
# automatiquement quand vous faites "django-admin.py startproject".             #
#                                                                               #
# La plupart des valeurs sont des paramètres de Django, écrasant les valeurs    #
# que vous pouvez trouver dans libs/django/conf/global_settings.py. La plupart  #
# de la configuration originale de Django n'est pas modifiée, donc vous devrez  #
# vous référer à global_settings.py pour connaitre les autres valeurs.          #
#                                                                               #
# D'autres valeurs sont à destination d'autres apps Django.                     #
#                                                                               #
# Enfin, quelques valeurs sont celles que nous avons créées pour nos propres    #
# apps Django.                                                                  #
#                                                                               #
# SOUVENEZ-VOUS : c'est juste un fichier Python ordinaire, ce qui signifie que  #
# vous pouvez mettre n'importe quel code Python dedans.                         #
#                                                                               #
# NOTE : le but de ce projet est de vous montrer comment faire des choses       #
# dans les apps, pas comment déployer Django. De ce fait, le contenu des        #
# paramètres et leurs organisations sont orientés dans ce but et ne reflètent   #
# pas ce que vous devriez faire en production.                                  #
# Je mettrai des notes là où il faudra faire attention.                         #
#################################################################################



# Puisque c'est un fichier Python ordinaire, on peut y faire des imports

import os
import sys
import os
import tempfile

from pathlib import Path

import os

# Récupération du chemin absolu vers le fichier settings.py
THIS_FILE = Path(__file__).absolute().resolve()

# A partir de ce chemin, on créé tous les autres chemins dont on aura besoin
PROJECT_DIR = THIS_FILE.parent # le dossier parent, contenant les params du projet
BASE_DIR = PROJECT_DIR.parent  # le dossier grand-parent, contenant tout le code
APPS_DIR = BASE_DIR / 'apps'   # le dossier contenant les apps
TEMP_DIR = Path(tempfile.gettempdir())  # un dossier temporaire

# Nous ajoutons les dossiers "apps" et "libs" au PYTHON PATH, de telle sorte
# que nous puissions importer chaque package sans avoir à les préfixer du nom
# du package parent. Ceci imite le comportement que nous aurions si ils
# étaient à la racine ou installés avec pip.
#
# Ex: nous pouvons importer "from app1_hello.views import hello" plutôt que
#     "from apps.app1_hello.views import hello" ou "import django" à la place
#     de "from libs import django"
sys.path.append(str(APPS_DIR))

# Soyez sûr que ceci est unique, et ne le partagez avec personne.
# ATTENTION : mettez une valeur différente en production, et ne sauvegardez
# pas ça dans un dépôt publique.
SECRET_KEY = '2fhdcfk-0ctkijtc_rqtj2^qw56yc)6$^j4msj3%yn*ib@9ya_'

# Affiche des messages d'erreurs sur la page Web si quelque chose plante.
# ATTENTION : la valeur par défaut est True, vous devriez toujours la mettre
# sur False en production.
DEBUG = True

# Listez ici les URLs depuis lesquelles vous souhaitez que votre site soit
# accessible.
# Ex : si vous voulez que votre site soit accessible depuis jaimelesgiraffes.com
# vous devriez le mettre ici.
ALLOWED_HOSTS = [
 "127.0.0.1" # site web local (uniquement sur ma machine)
]

# Liste de chemins d'import Python de toutes les applications que Django
# doit charger au démarrage. Elle contient les applications internes de Django,
# celles installées en plus avec pip et vos propres applications. Pour Django,
# c'est la même chose, ce sont juste des modules Python importables.
# Les applications installées ont leurs fichiers statiques, leurs templates et
# modèles détectés automatiquement.
INSTALLED_APPS = (

    # applications Django

    'django.contrib.auth',  # authentification via password
    'django.contrib.contenttypes',  # permet les relations génériques via l'ORM
    'django.contrib.sessions',  # sessions persistantes pour les utilisateurs
    'django.contrib.sites',  # nom du site en base de données
    'django.contrib.messages',  # créer et afficher un message pour l'utilisateur
    'django.contrib.staticfiles',  # servir les fichiers statiques en dev
    'django.contrib.admin',  # outil d'administration de la base de données
    'django.contrib.humanize', # tools pour formatter les valeurs humainement

    # nos applications

    'app1_hello',
    'app2_hello_again',
    'app3_basic_routing',
    'app4_links',
    'app5_get_post_and_cookies',
    'app6_template_tools',
    'app7_static_files',
    'app8_base',

    # vous pouvez ignorer cela, c'est l'app qui liste les autres apps
    'ignore_me',
)

# Les middlewares sont le mécanisme de Django pour appliquer un traitement à
# chaque requête. Vous voyez ici les valeurs par défaut, mais vous pouvez
# écrire les vôtres. Vous n'aurez pas souvent besoin de jouer avec les
# middlewares.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Le chemin d'import Python du module principal d'urls. C'est dans celui-ci
# qu'on déclare la racine de toutes les URLs de toutes les apps.
ROOT_URLCONF = 'project.urls'

# Comme Django trouve les templates (les fichiers HTML)
TEMPLATES = [
    {
        # Les chercher localement
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Liste additionelles de dossiers dans lequels les chercher
        'DIRS': [],
        # Chercher dans chaque dossier "templates" de chaque app
        'APP_DIRS': True,
        'OPTIONS': {
            # Liste de callables ajoutant des données automatiquement dans
            # le context de chaque template. Par défaut le template pourra ici
            # voir la constate DEBUG, l'objet user authentifié, l'objet
            # request et les messages flash.
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Le chemin d'import du module de l'application WSGI utilisé par Django.
# Pour vous, utile uniquement pour la production.
WSGI_APPLICATION = 'project.wsgi.application'

# La configuration de la base de données est un gros dictionnaire. On
# configure postgresql, mysql, sqlite ou oracle au même endroit, et on peut
# avoir plusieurs bases de données configurées pour un projet (une par clé du
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
# bases de données plus exotiques telles que MSAccess ou Firebird

# Ce qui est appelé au moment de valider les mots de passe, par exemple
# a la création d'un nouveau compte utilisateur
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



# La localisation de base (langue, pays...) de votre site.
LANGUAGE_CODE = 'fr-fr'

# Vous pouvez choisir le fuseau horaire de votre site. Généralement, il vaut mieux laisser 
# à UTC et faire les conversions à la main
TIME_ZONE = 'UTC'

# Voulez-vous que le texte soit traductible dans d'autres langues ? Si non,
# vous pouvez mettre False pour gagner un peu de perf.
USE_I18N = True

# Voulez-vous que Django formate les dates, l'argent et les nombres selon
# culture / langue en cours ? Si non, vous pouvez mettre False pour gagner un
# peu de perf.
USE_L10N = True

# Djando doit-il ajouter les times zone dans les objets date ? Gardez le à True,
# car il est plus simple de ne jamais s'en servir que de le désactiver et en avoir besoin.
USE_TZ = True

# Prefixe de l'URL qui va servir les fichiers statiques.
# Exemple: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'
