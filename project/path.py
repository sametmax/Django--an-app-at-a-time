# -*- coding: utf-8 -*-


"""
    This module contains all the paths for alls this project directories, that
    we created dynamically.

    All paths are absolute, without symlink and in unicode.

    We also add the 'apps' and 'libs' directories to the PYTHON PATH, which
    will make the imports much  easier.

"""


from __future__ import unicode_literals

import sys
import os
import tempfile

# This part is a bit complicated and is not mandatory for your project, but
# it renders it completly portable since all directory paths are dyncamically
# generated instead of being hard coded.

# We get the 'settings.py' file path (the __FILE__ variable contains
# automatically the path of the current file) and we transform this string
# in unicode in case you got non ASCII caracters in this name (
# sys.getfilesystemencoding() git us the file system encoding which can be
# different for Windows, Mac or Linux)
FS_ENCODING = sys.getfilesystemencoding()
try:
    THIS_FILE = __file__.decode(FS_ENCODING)
except AttributeError: 
    # In Python 3, __file__ is already decoded
    THIS_FILE = __file__

# We create dynamically these settings, giving us the absolute path
# to the project directory, the root directory containing all our work
# and any other directory we might need
PROJECT_DIR = os.path.dirname(os.path.realpath(os.path.abspath(THIS_FILE)))
ROOT_DIR = os.path.dirname(PROJECT_DIR)
APPS_DIR = os.path.join(ROOT_DIR, 'apps')
LIBS_DIR = os.path.join(ROOT_DIR, 'libs')

try:
    TEMP_DIR = tempfile.gettempdir().decode(FS_ENCODING)
except AttributeError: 
    # In Python 3, __file__ is already decoded
    TEMP_DIR = tempfile.gettempdir()

# We add the apps and libs directory to the PYTHON PATH, so we can import each
# package without prefixing them with the parent package name. This mimic the
# behavior we would have if they were at the root directory or installed with
# pip.
#
# E.G: we can do from "app1_hello.views import hello" instead of
#      "from apps.app1_hello.views import hello" or "import django" instead of
#      "from libs import django"
#
# When you have a small project, you can avoid this and put all apps at the root
# dir like in the official Django tutorial, but in a big project with a lots of
# apps, you usually put them all in an "apps" dir like we did, so it's a good
# thing to know.
sys.path.append(LIBS_DIR)
sys.path.append(APPS_DIR)

