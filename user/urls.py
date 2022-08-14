from django.urls import path
from user.views import *


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register', userRegister, name='register'),  
    path('logout/', userLogout, name='logout'),
]



