from django.shortcuts import render, redirect
from django.urls import reverse


def main_view(request, abracadabra):
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
        final_url = reverse('animal', args=('bibizyana', ))
        return redirect(final_url)
