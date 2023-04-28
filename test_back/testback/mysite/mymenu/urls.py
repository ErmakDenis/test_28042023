from django.urls import path
from .views import *

urlpatterns = [

    path('', category_view),#,name='mymenu'
]