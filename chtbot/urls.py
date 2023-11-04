from django.urls import path
from chtbot.views import *

urlpatterns = [
    path('', chtbot,name ='chatbot')
]
