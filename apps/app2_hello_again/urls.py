
from django.urls import path


# Une alternative est d'utiliser un import relatif
from app2_hello_again.views import hello


urlpatterns = [
    path('', hello),
]
