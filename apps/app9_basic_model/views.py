# -*- coding: utf-8 -*-


from django.shortcuts import render

from app9_basic_model.models import Person


def add_person(request):
    """
        Create a new Person object with the provided name and save it to
        the database.
    """

    context = {}

    # If this is a POST request, assume they are creating a new person
    if request.method == 'POST':

        person_name = request.POST.get('name', '')
        # we don't have a person name, display an error
        if not person_name:
            context.update({'message': 'You must enter a person name',
                           'message_type': 'error'})

        elif len(person_name) > 32:
            context.update({'message': "The name can't be longer than 32 characters",
                           'message_type': 'error'})
        else:
            # We have a person name : create a new person object with this name.
            person = Person(name=person_name)
            # By calling "save()", we create a new entry in the database.
            person.save()

            # Addind a success message

            context.update({'message': 'The person has been added !',
                           'message_type': 'success'})

    return render(request, 'app9_basic_model/add_person.html', context)


def person_list(request):
    """
        List all persons saved in the database.
    """

    # To make queries to the database, we use a manager from the model.
    # The default manager is "objects". We can ask for all the objects this way:
    persons = Person.objects.all()

    # persons now contains a 'queryset', an object representing an SQL query.
    # The first time we read the queryset (e.g: by looping on it), we will
    # trigger a query to the database, which will fill the queryset with
    # Person objects containing the data from the database.

    return render(request, 'app9_basic_model/person_list.html',
                  {'persons': persons})