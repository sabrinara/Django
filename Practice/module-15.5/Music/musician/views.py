from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def all_musician(request):
    musician = forms.Musician.objects.all()
    return render(request, 'all_musician.html', {'musician' : musician})


def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : musician_form})