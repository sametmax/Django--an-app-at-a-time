*******************************
Django, an app at a time
*******************************

How to use?
==================

Download and extract this project, and run:

    python ./manage.py runserver
    
You can ignore the "You have 15 unapplied migration(s)." warning.

You don't need to install anything.

Go to the URL http://127.0.0.1:8000 and play with the apps.

When you want to see how it works, go to the "apps" directory and watch the commented source code.

Each app assumes you understand the previous ones, and contains a README to guide you.

Download links:

  - `English version <https://github.com/sametmax/Django--an-app-at-a-time/archive/master.zip>`_
  - `Version française <https://github.com/sametmax/Django--an-app-at-a-time/archive/fran%C3%A7ais.zip>`_


What's in there?
==================


- "apps" : contains all the applications, sorted by complexity and requirements. This is what you want to read.
- "project": the Django project itself, containing settings and the main URL routes definition. You should have a look in there from time to time, it puts the apps in context and contains some tips.
- "libs": dependencies such as Django or external libraries that you would have to install otherwise. You don't need to, but you can look into it once you start feeling comfortable with Django.
- "libs/ignore_me": the app that lists all the apps, and the main page of the project. You can ignore it, it's not very interesting.
- "manage.py": the command to interact with the Django project. This one is a bit modified so don't replace it.
- ".gitignore": a configuration file for git. You don't need this for Django. It's here to help me.


Notes
==========

In a real project, you WOULD have to install something. Dependencies are provided here for convenience, dumped in libs/, but you would definitely use pip and virtualenv in a real project.

By the way, this is NOT a tutorial. The purpose is not to replace a full course about how Django works, but rather to give you a concrete example on how each task can be achieved with Django.

Translations and spell corrections welcome!
