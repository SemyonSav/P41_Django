from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import *


def main_view(request):
    examples = Example.objects.all()
    return render(request, 'web/index.html', {'examples': examples})


def add_view(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(data=request.POST, instance=None)
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/form.html', {'form': form})


def delete_view(request, id):
    ex = get_object_or_404(Example, id=id)
    ex.delete()
    return redirect('main')


def edit_view(request, id):
    ex = get_object_or_404(Example, id=id)
    form = ExampleForm(data=request.POST or None, instance=ex)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'web/form.html', {'form': form})
