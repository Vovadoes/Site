from django.shortcuts import render

def start(request):
    return render(request, 'start/start.html')

def error(request):
    return render(request, 'error.html')