from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import user


# Create your views here.
def index(request):
    if 'username' in request.session:
        return redirect(home)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            messages.info(request, 'Error')
            return redirect(index)
    else : return render(request, 'index.html')


def home(request):
    if 'username' in request.session:
        # return redirect(index)
        return render(request, 'home.html')

    else : return redirect(index)
def user_logout(request):

    request.session.flush()
    return redirect(index)