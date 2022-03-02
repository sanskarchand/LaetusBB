from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("Greetings. Location: /core. DB host is " + os.environ['DB_HOST'])
