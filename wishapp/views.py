from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            user_id = request.user.id
            return redirect('wishlist', user_id)
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                user_id = request.user.id
                return redirect('wishlist', user_id)
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("home")

def wishlist(request, user_id):
    user = User.objects.get(id=user_id)
    wishes = Wish.objects.filter(user_id=user)
    userid = user_id
#    wisher = Wish.objects.get(id=user_id)   #just to allow loggedin users to see add wishes
    context = {
        "user": user,
       "wishes": wishes,
       "userid":userid,
#       "wisher":wisher,
    }

    return render(request, 'list.html', context)

def add_wish(request, user_id):
    form = WishForm(request.POST, request.FILES)

    if request.user.is_anonymous:
        return redirect('signin')
#    form = WishForm
#    user = Wish.objects.get(id=wish_id)
#    wishu = User.objects.get(id=user_id)
    if not (request.user.id == user_id):
        return redirect('no-access')
    if request.method == "POST":
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            return redirect("wishlist", user_id)
    context = {
        "form":form,
#        "user":user,
#        "wishu":wishu,
    }
    return render(request, "addwish.html", context)


def delete_wish(request, user_id, wish_id):
    wish = Wish.objects.get(id=wish_id)
    user = User.objects.get(id=user_id)
    if request.user.id != user_id:
        return redirect('no-access')
    wish.delete()
    return redirect('wishlist', user_id,)




def no_access(request):
    return render(request, 'noaccess.html')
