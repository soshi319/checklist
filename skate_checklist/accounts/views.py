from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

 

def login(request):
    return render(request, 'accounts/login.html')


def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/checklist')
        else:
            return redirect('/login')

def logout(request):
    auth_logout(request)
    context = {'msg':'ログアウトしました！',}
    return render(request, 'checklist/msg.html', context)