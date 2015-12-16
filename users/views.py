from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    title = "DMP"
    return render(request, 'users/head.html', {"title": title})


# Testing
def test(request):
    return HttpResponse("hello users")