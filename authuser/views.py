from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as v_logout
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import SignupForm, LoginForm, ProfileUpdateForm, UserUpdatedForm
from .models import Profile


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Hello! '{user}' you're welcome to Gamers Palace,"
                                      f" share your previous game experience ")
            return redirect("blog:index")

    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "authuser/login.html", context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            messages.success(request, f"Account for {username} was created successfully, Now Login!")
            return redirect("authuser:login")
    else:
        form = SignupForm()
    return render(request, "authuser/signup.html", {
        "form": form
    })


def logout(request):
    v_logout(request)
    messages.warning(request, "Logged out.")
    return redirect("blog:index")


@login_required
def profile(request):
    user = request.user

    if request.method == "POST":
        u_form = UserUpdatedForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect("authuser:profile")

    else:
        u_form = UserUpdatedForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    return render(request, "authuser/profile.html", {
        "u_form": u_form,
        "p_form": p_form
    })


def other_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    context = {
        "user": user,
        "profile": profile,
    }
    return render(request, "authuser/other_user_profile.html", context)
