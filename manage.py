#!/usr/bin/env python
import os
import sys

# this is hack to allow "libs" to be added to the PYTHON PATH
# and is not part of the usual manage.py file
import project.settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
