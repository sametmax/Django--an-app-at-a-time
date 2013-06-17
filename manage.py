#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# ceci est un hack pour permettre à "libs" d'être ajouté au PYTHON PATH
# et ne fait pas parti du fichier manage.py habituel
import project.settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
