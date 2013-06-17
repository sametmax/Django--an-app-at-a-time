"settings.py" contains the settings for your Django project. It's an ordinary Python module you can import and use like any other modules.

"urls.py "contains code that associate urls with apps, so when a user go to your website on a specific url, the code of the right app is used.

"wsgi.py" is only used in production and you can ignore it. However, you can't delete it as it became mandatory in the last Django release.