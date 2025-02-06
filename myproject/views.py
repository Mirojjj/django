from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        "username": "ram",
        "age": 23,
        "occupation": "Software engineer"
    }
    return render(request, "index.html", context)
