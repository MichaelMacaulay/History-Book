from django.shortcuts import render
from django.http import HttpResponse


def TestPage(request):
    return render(request, 'test.html')


def ThanksPage(request):
    return render(request, 'thanks.html')


def index(request):
    return render(request, 'index.html')
