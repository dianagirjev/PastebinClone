from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TextForm
from .models import Text


@login_required(login_url="login")
def index(request):
    context = {
        "all_forms": reversed(Text.objects.all())
    }
    return render(request, 'pastebin/index.html', context)


@login_required(login_url="login")
def saveUserInput(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")


@login_required(login_url="login")
def showUserInputDetails(request, userInputId):
    userInput = get_object_or_404(Text, id=userInputId)
    userInfo = request.user
    context = {
        "userInfo": userInfo,
        "userInput": userInput
    }
    return render(request, "pastebin/showUserInputDetails.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user)
                return redirect('login')
        else:
            form = CreateUserForm()
        context = {"form": form}
        return render(request, "pastebin/register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, "pastebin/login.html", context)


def logoutPage(request):
    Text.objects.all().delete()
    logout(request)
    return redirect("login")
