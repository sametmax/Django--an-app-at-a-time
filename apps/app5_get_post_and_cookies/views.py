

from django.shortcuts import render


def hello(request):

    # request.GET, request.POST and request.COOKIES sont des objects dictionary-
    # like. C'est à dire que l'on peut faire request.GET['name'],
    # request.POST['name'] or request.COOKIES['name'] pour accéder à leurs
    # valeurs. Mais comme avec un dico, il lèveront KeyError si la clé
    # n'existe pas. Afin d'éviter cela, il est possible, comme avec les dicos,
    # d'utiliser la méthodes get(). Elle retourne la valeur, ou None si cette
    # dernière n'existe pas. Si on fournit un second argument il sera retourné
    # en cas d'absence de la clé à la place de None.

    # Retourne la valeur associée à 'name' passée via COOKIES, ou None.
    name = request.COOKIES.get('name')

    # Retourne la valeur associée à 'name' passée via POST, ou la valeur de
    # COOKIES.
    # Ainsi POST écrase toujours la valeur de COOKIES.
    name = request.POST.get('name', name)

    # Retourne la valeur associée avec 'name' passée via GET, ou celle de POST.
    # Ainsi cette valeur écrase toujours celle de POST ou COOKIES.
    name = request.GET.get('name', name)

    # Ajoutons une valeur par défaut à name
    if name is None:
        name = "anonymous"

    # Créer une dictionaire pour passer ces valeurs dans le contexte. Nous
    # ajoutons request.methods qui contient la string "POST, GET", "PUT", etc
    # selon la valeur de la méthode HTTP utilisée pour accéder à cette vue.
    context = {'name': name, 'method': request.method}

    # Plutôt que de retourner la réponse, nous la stockons dans une variable.
    # En Djagno, les réponses sont des objets, et nous pouvons les manipuler
    # avant de les retourner au navigateur.
    response = render(request, 'app5_hello.html', context)

    # On met dans un cookie la valeur de name, attaché à la réponse, de telle
    # sorte qu'à la prochaine visite du navigateur sur cette vue, il puisse
    # nous la renvoyer via un cookie.
    response.set_cookie('name', name)


    # On retourne la réponse modifiée.
    return response
