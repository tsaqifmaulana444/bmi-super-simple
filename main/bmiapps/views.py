from django.shortcuts import render
from .forms import FormTrack


def home(request):
    if request.method == "POST":
        form = FormTrack(request.POST)
    else :
        form = FormTrack()

    return render(request, 'index.html')


def track(request):
    return render(request, 'index2.html')

