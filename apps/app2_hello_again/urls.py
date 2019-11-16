
from django.urls import path


# An alternative way is to use relative imports
from .views import hello


urlpatterns = [
    path('', hello),
]
