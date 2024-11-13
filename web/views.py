from datetime import datetime

from django.shortcuts import render


def main_view(request):
    year = datetime.now().year
    return render(request, "web/index.html", {
        "year": year
    })
