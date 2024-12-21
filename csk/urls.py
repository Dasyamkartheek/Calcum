from django.urls import path
from .views import *

app_name='csk'

urlpatterns=[
    path('',team,name='team'),
    path('match/',match,name='match'),
]