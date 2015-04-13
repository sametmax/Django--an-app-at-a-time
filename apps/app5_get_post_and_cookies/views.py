# -*- coding: utf-8 -*-


from django.shortcuts import render


def hello(request):

    # request.GET, request.POST and request.COOKIES are dictionary-like
    # objects, meaning you can access them like you can access a dictionary.
    # So you can make request.GET['name'] or request.POST['name'] or
    # request.COOKIES['name'] to get values from them. But as with dict, this
    # will raise KeyError if the key does not exists. To avoid that, you
    # can, like with dictionaries, use the get() method. It return the value
    # or None if the value doesn't exists. If you provide a second argument
    # it will return it if the key doesn't exist, and return the right value
    # otherwise.

    # Returns the value associated with 'name' passed via COOKIES, or None.
    name = request.COOKIES.get('name')

    # Returns the value associated with 'name' passed via POST, or the
    # value from COOKIES.
    # This way POST always overwrites the value from COOKIES.
    name = request.POST.get('name', name)

    # Returns the value associated with 'name' passed via GET, or from POST.
    # This way GET always overwrites the value from POST and COOKIES
    name = request.GET.get('name', name)

    # Let's add default value to name
    if name is None:
        name = "anonymous"

    # Create a dictionary to pass this values in the context. We add
    # request.method which will contains the string "POST", "GET", "PUT", etc
    # according to the HTTP method that is used to access this view.
    context = {'name': name, 'method': request.method}

    # Instead of just returning the response, we store it in a variable.
    # In Django, responses are objects, and we can manipulate them before
    # sending them to the browser.
    response = render(request, 'app5_hello.html', context)

    # We set a cookie with the value "name" in the response, so next time
    # the browser visit this view, it will send this value via a cookie.
    response.set_cookie('name', name)

    # Returns the modified response.
    return response
