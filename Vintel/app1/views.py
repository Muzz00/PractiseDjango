from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Profile was created for ' + username)
                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'app1/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'app1/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')