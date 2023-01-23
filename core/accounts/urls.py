from django.urls import path
from accounts.views import login
urlpatterns=[
    path('' , login , name='login'),
    # path('signup' , signup , name='signup'),
    # path('logout' , logout , name='logout'),
]