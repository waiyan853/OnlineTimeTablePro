from django.urls import path
from .views import Register,addUSer,home,login

urlpatterns = [
    path('register/', Register, name='register'),
    path('addUSer/', addUSer, name='addUSer'),
    path('', home, name='home'),
    path('login/', login, name='login'),
]
