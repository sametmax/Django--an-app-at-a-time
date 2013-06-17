*******************************
Django, an app at a time
*******************************

How to use ?
==================

Download then extract this project, and run `python ./manage.py`.

You don't need to install anything.

Go to the URL http://127.0.0.1:8000 and play with the apps.

When you want to see how it works, go to the "apps" directory and watch the commented source code.

Each app assumes you understand the previous ones, and contains a README to guide you.

Download links:

  - `English version <https://github.com/sametmax/Django--an-app-at-a-time/archive/master.zip>`_


What's in there ?
==================


- "apps" : contains all the applications, sorted by complexity and requirements. This is what you want to read.
- "project": the django project itself, containing settings and the main url route definition. You should have a look in there from time to time, it will put the apps in the context of the project and contains so tips.
- "libs": dependancies such as django or external librariies that you would have otherwise to install. You don't need to look into it, but you can when you start feeling confortable with Django.
- "libs/ignore_me": the app that list all the apps, and the main page of the project. You can ignore it, not very interesting.
- "manage.py": the command to interact with the Django project. This one is a bit modified so don't replace it.
- ".gitignore": a configuration file for git. You don't need this for Django. It's here to help me.


Notes
==========

In a real project, you WOULD have to install something. Dependancies are here provided and dumped in the project for convenience, but you would usually use pip and virtual env in a real project.

By the way, this is NOT a tutorial. The purpose is not to replace a full course to learn how Django works, but rather give you a concret example on how each task can be achieve with Django.

Translations and spell corrections welcome !