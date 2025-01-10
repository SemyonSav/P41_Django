from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from .forms import *


def main_view(request):
    return render(request, "web/index.html")


def register_view(request):
    form = RegisterForm()
    is_success = False
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = MyUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, 'web/register.html', {'form': form, 'is_success': is_success})


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Данные введены некорректно")
            else:
                login(request, user)
                return redirect('main')
    return render(request, 'web/auth.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


@permission_required(perm='web.view_book', raise_exception=True)
def books_view(request):
    return render(request, 'web/books.html')
