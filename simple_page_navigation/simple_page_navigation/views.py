from django.shortcuts import render
# home.html rendering
def home(request):
   return render (request, 'home.html')