from django.urls import path
from accounts.views import loginuser , signup , logoutuser
urlpatterns=[
    path('login' , loginuser , name='login'),
    path('signup' , signup , name='signup'),
    path('logout' , logoutuser , name='logout'),
]