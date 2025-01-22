from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator

from .forms import *
from .models import Book


def main_view(request):
    names = ['Title ' + str(i) for i in range(50)]
    if Book.objects.all().count() == 0:
        for name in names:
            book = Book.objects.create(
                name=name,
                year=2007
            )
            book.save()

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
            #group = Group.objects.get(name='reader')
            # user.groups.set([group,]) Задать группы
            # user.groups.add(group) Добавить группу
            # user.groups.remove(group) Удалить группу
            # user.groups.clear() Удалить все группы

            # p = Permission.objects.get(codename='view_book')
            # user.user_permissions.set([p, ]) Всё то же самое с разрешениями
            # user.has_perm(p) Есть ли у пользователя разрешение

            # Создание своего permission
            # content_type = ContentType.objects.get_for_model(Book)
            # permission = Permission.objects.create(name='Reader Permission', codename='reader_perm', content_type=content_type)

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
    books = Book.objects.all()
    page_number = request.GET.get("page", 1)
    paginator = Paginator(books, per_page=10)
    total_count = books.count()

    return render(request, 'web/books.html', {
        'books': paginator.get_page(page_number),
        'total_count': total_count
    })
