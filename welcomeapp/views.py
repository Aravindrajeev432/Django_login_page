from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import user
# Create your views here.
def index(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            return redirect(home)
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')
