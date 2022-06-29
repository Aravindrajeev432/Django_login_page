from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Homes
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
            messages.info(request, 'Invalid username/password')
            return redirect(index)
    else:
        return render(request, 'index.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        home = Homes.objects.all()

        return render(request, 'homesell.html', {'usern': request.session['username'],'hdetails':home})

    else:
        return redirect(index)


def user_logout(request):
    # if request.method == 'GET':
    #     log= request.GET['logout']
    #     if 'username' in request.session:
    #
    #         return redirect(home)
    #     else:
    #         print("index")
    #         redirect(index)
    #
    print("A")
    request.session.flush()
    return redirect(index)