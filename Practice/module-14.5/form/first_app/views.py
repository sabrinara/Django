from django.shortcuts import render
from . forms import contactForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, './home.html', {'form': form})