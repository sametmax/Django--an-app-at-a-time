# -*- coding: utf-8 -*-


from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html', {"name": "world"})


##################################################################################
# This is how it works:                                                          #
#                                                                                #
#                                                                                #
# hello() is a simple function that MUST accept an HTTP request an return a      #
# response.                                                                      #
#                                                                                #
# This function is called automatically when the URL in the urls.py file that    #
# point to it is reached.                                                        #
#                                                                                #
# The request object is passed automatically by Django, and we can do whatever   #
# we want in the function body.                                                  #
#                                                                                #
# The only obligation from our part is to return a HTTP response, which we do by #
# returning the result of render(), which build the response for us from the     #
# initial request, a template name and a template context.                       #
#                                                                                #
# The template name will be the name of the file we want to use to format our    #
# data. In this case, "hello.html" contains just a bit of HTML. You can          #
# find it in the "templates" directory of this app.                              #
#                                                                                #
# The last parameter is the template context, a dictionary of variables we wish  #
# to be available to use in the template. Here we pass the value "world" and we  #
# give it the name "name" so in the template, you can use the variable "name" to #
# display its content.                                                           #
#                                                                                #
# render() mixes the template with it's context and make the web page we need.   #
#                                                                                #
# Django has its own idea on the MVC pattern. The controller is the framework,   #
# models are the ORM classes, but the views are the functions in the views.py,   #
# not the templates.                                                             #
# ################################################################################
