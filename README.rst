*******************************
Django, an app at a time
*******************************

A heavily commented Django project dedicated to teaching the framework or refresh one's memory. Each app demonstrates a few essential Django features so you can see how it all fit together by looking at the code and testing the result in your browser. There is nothing do except run and read.

Currently:

- Project : see how settings and urls.py work
- App 1: hello world
- App 2: hello again
- App 3: basic routing
- App 4: creating links
- App 5: GET, POST and cookies
- App 6: templates, tags and filters
- App 7: static files
- App 8: reusable app

What's to come:

- ORM
- Forms
- Authentification
- Admin
- Command
- Translations


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
- "ignore_this_dir": stuff to make it work that you don't need to know about.
- "manage.py": the command to interact with the Django project. This one is a bit modified so don't replace it.
- ".gitignore": a configuration file for git. You don't need this for Django. It's here to help me.


Notes
==========

In a real project, you WOULD have to install something. Dependencies are provided here for convenience, dumped in ignore_this_dir/, but you would definitely use pip and virtualenv in a real project.

By the way, this is NOT a tutorial. The purpose is not to replace a full course about how Django works, but rather to give you a concrete example on how each task can be achieved with Django.

Translations and spell corrections welcome!
