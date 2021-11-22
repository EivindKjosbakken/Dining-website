from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib import messages
# from django.contrib.auth.models import User, auth

# Create your views here.
from .models import User
from .models import UserManager
from dinners.views import feed_view


def signup_view(request):
    print(request.method)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        # password2 = request.POST['password2']
        address = request.POST['address']
        city = request.POST['city']
        try:
            user = User.objects.create(username=username,
                                       password=password1,
                                       email=email,
                                       first_name=first_name,
                                       last_name=last_name,
                                       address=address,
                                       city = city)

            user.save()
            login(request, user)
            return redirect(feed_view)
        except:
            messages.info(request, 'Brukernavnet eksisterer allerede!')

    return render(request, 'users/registrer.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = False
        try:
            u = User.objects.get(username=username)
            print(u)
            if u is not None and u.password == password:
                auth = True
            else:
                messages.info(request, 'Feil passord!')

        except:
            print("FEIL")
            messages.info(request, 'Brukeren eksisterer ikke!')

        # user = auth.authenticate(username=username, password=password)
        print(username)
        print(password)

        if auth:
            # auth.login(request, u)
            login(request, u)
            return redirect(feed_view)
        else:
            return redirect("/")

    return render(request, "users/index.html", {})


def logout_view(request):
    logout(request)
    # evt legge inn i "message" - du er logget ut elns
    # return render(request, 'users/index.html', {})
    return redirect("../")


def profile_view(request, my_username):
    obj = get_object_or_404(User, username=my_username)
    logged_in_user = request.user
    context = {
        "user": obj,
        "logged_in_user": logged_in_user
    }
    return render(request, "users/profile.html", context)


def user_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        return redirect('home')
    context = {
        "user": user
    }
    return render(request, "users/profile_delete.html", context)

def user_edit_view(request):
    user = request.user
    context = {
        "user": user
    }

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password1 = request.POST['password1']
        user.address = request.POST['address']

        user.save()
        return_page = "../../user/"+str(user.username)
        return redirect(return_page)

    return render(request, 'users/profile_edit.html', context)
