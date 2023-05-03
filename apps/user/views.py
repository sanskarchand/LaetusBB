from django.shortcuts import render
from django.template import loader


# Create your views here.
def login(request):
    template = loader.get_template("user/login.html")
