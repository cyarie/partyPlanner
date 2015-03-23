from django.shortcuts import HttpResponse


def index():
    return HttpResponse("Welcome to my eHomepage!")
