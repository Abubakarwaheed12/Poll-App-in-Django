from django.contrib import admin 
from django.urls import path
from app.views import add_question , add_choice , All_question
urlpatterns=[
    path('' ,add_question, name='addquesion'),
    path('choice/' ,add_choice, name='addchoice'),    
    path('quiz/' , All_question , name='quiz')
]