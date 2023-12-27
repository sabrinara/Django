from django.shortcuts import render
# from posts.models import Post
from album.models import Album
def home(request):
    album = Album.objects.all()
    return render(request, 'index.html', {'album' : album})
 