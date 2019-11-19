

from django.shortcuts import render


def hello(request):
    return render(request, 'hello.html', {"name": "world"})



###################################################################################
# Voici comment ça marche :                                                       #
#                                                                                 #
# hello() est une simple fonction qui DOIT accepter une requête HTTP et retourner #
# une réponse.                                                                    #
#                                                                                 #
# Cette fonction est appelée automatiquement quand l'url de urls.py qui pointe    #
# dessus est atteinte.                                                            #
#                                                                                 #
# L'objet "request" est passé automatiquement par Django, et nous pouvons         #
# faire ce que bon nous semble dans le corps de la fonction.                      #
#                                                                                 #
# La seule obligation de notre part est de retourner une réponse HTTP,            #
# ce que nous faisons en retournant le résultat de render(), qui construit pour   #
# nous une réponse en utilisant la requête initiale, un nom de template et        #
# le contexte du template.                                                        #
#                                                                                 #
# Le nom du template est le nom du fichier que nous souhaitons utiliser pour      #
# formater nos données. Dans ce cas, "hello.html" contient juste un peu de HTML.  #
# Vous pouvez le trouver dans le dossier "templates" de cette app.                #
#                                                                                 #
# Le dernier paramètre est le contexte du template, c'est un dictionnaire de      #
# variables que nous souhaitons rendre disponibles dans le template. Ici          #
# nous passons la valeur "world", et nous lui donnons le nom "name" donc,         #
# dans le template, nous pourrons utiliser la variable "name" pour afficher son   #
# contenu.                                                                        #
#                                                                                 #
# render() mélange le template et son contexte et fabrique la page Web dont       #
# nous avons besoin.                                                              #
#                                                                                 #
# Django a sa propre vision du pattern MVC. Le contrôleur est le framework,       #
# le modèle sont les classes ORM, mais les vues sont les fonctions de views.py,   #
# pas les templates.                                                              #
###################################################################################



