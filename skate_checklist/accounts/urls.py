from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name ='accounts'

urlpatterns =[
    # ex: /login/
    path('login/', views.login, name='login'),
    # ex: /signin/
    path('signin/', views.signin, name='check'),
    # ex: /logout/
    path('logout/', views.logout, name='logout'),
]