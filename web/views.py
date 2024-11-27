from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *


def main_view(request):
    sp = ['Олег', 'Андрей', 'Джон']
    return render(request, "web/index.html", {
        "sp": sp,
        'number': 5
    })


def animals_view(request):
    return render(request, 'web/animals.html')


def animal_view(request, animal):
    age = request.GET.get('age')
    animals = {
        'bibizyana': 'Бибизяна прыгает',
        'lion': 'Лев рычит'
    }
    if animal in animals:
        return render(request, 'web/animal.html', {'animal_info': animals[animal], 'age': age})
    else:
        final_url = reverse('animal', args=('bibizyana',))
        return redirect(final_url)


def form_view(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # age = request.POST.get('age')
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'web/form.html', {'data': data})
        else:
            return render(request, 'web/form.html', {'form': form})
    form = UserForm()
    return render(request, 'web/form.html', {
        'form': form
    })

