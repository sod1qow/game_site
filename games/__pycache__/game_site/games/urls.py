from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login_register/', login_register_page, name='login_register'),
]
