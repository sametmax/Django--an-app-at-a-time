
from django.urls import path

import app5_get_post_and_cookies.views

urlpatterns = [

    path('', app5_get_post_and_cookies.views.hello),

]
