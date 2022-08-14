


from django.urls import path
from favories.views import *

urlpatterns = [
    path('favories/', favori, name='favori'),
]