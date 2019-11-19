#!/usr/bin/env python
import os
import sys

# Ne fait pas partie du fichier original. C'est un garde-fou pour
# eviter aux etudiant de rester bloquer parce qu'ils utilisent la
# mauvaise version de Python
if sys.version_info < (3, 6):
    sys.exit("'Django, an app at a time' requiere Python 3.6 ou plus")


# Hack pour ajouter "ignore_this_directory" dans le PYTHON PATH
# ce qui n'est pas dans le manage.py original
from project import settings
sys.path.append(str(settings.BASE_DIR / 'ignore_this_directory'))



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
