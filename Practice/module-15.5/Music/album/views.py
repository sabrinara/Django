from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def all_album(request):
    album = models.Album.objects.all()
    return render(request, 'all_album.html', {'album' : album})

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : album_form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('all_album')
    else:
        album_form = forms.AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form' : album_form})

def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('all_album')