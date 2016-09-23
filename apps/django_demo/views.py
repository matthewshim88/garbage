from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Pokes
from ..new_login.models import User

# Create your views here.
def index(request):
    this_user = User.objects.get(id=request.session['id'])
    all_users = User.objects.all()
    context = {
        'all_users':all_users,
        'this_user':this_user,
    }
    return render(request, 'django_demo/index.html', context)

def addPoke(request):
    print "fuck this bullshit"
    if request.method =='POST':
        target_user = User.objects.get(id=id)
        addPoke = Pokes.pokeMgr.addPoke(request.POST, target_user)
    return redirect(reverse('pokes:index'))

def logOut(request):
    request.session.clear()
    return redirect(reverse('users:index'))
