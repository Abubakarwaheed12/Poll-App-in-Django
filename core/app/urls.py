from django.contrib import admin 
from django.urls import path
from app.views import add_question , add_choice , All_question , search
urlpatterns=[
    path('' ,add_question, name='addquesion'),
    path('choice' ,add_choice, name='addchoice'),    
    path('quiz' , All_question , name='quiz'),
    path('search' , search , name='search'),
]