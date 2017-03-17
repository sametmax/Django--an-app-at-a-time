# -*- coding: utf-8 -*-

from django.db import models

# A model is just a class inheriting from models.Model. Once you call
# "manage.py syncdb", it creates a table in database for this class. This table
# will have a column for each attributes of the class of the type
# models.SomethingField.
# The model is the description of the data you want to store in database
# AND the object you use to manipulate the data itself.
class Person(models.Model):

    # A CharField always needs a limit in character numbers. We choose
    # 32 out of the blue. This will allow us to store a string in data base
    # between 0 and 32 characters in size.
    name = models.CharField(max_length=32)

# After running "manage.py syncdb", we will have a table containing data for
# persons, with one column named "name".