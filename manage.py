#!/usr/bin/env python
import os
import sys

# This is not part of the regular manage.py files, but ensure students
# don't get blocked because they use the wrong Python version
if sys.version_info < (3, 6):
    sys.exit("'Django, an app at a time' requires Python 3.6 or greater")

# This is a hack to allow "ignore_this_directory" to be added to the PYTHON PATH
# and is not part of the usual manage.py file
from project import settings
sys.path.append(str(settings.BASE_DIR / 'ignore_this_directory'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
