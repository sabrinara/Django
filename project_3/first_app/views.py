from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'name': 'Shubham', 'place': 'Mumbai', 'age': 22 , 'list': [1,2,3,4,5],'list2':['python','is','best'] , 'val' : "",'birthday': datetime.datetime.now(), 'courses' : [
        {
            'id' : 1,
            'name': 'django',
            'fee': 5000
        },
        {
            'id' : 2,
            'name': 'python',
            'fee': 6000
        },
        {
            'id' : 3,
            'name': 'C',
            'fee': 7000
        }
    ]}
    return render(request, 'home.html',d)
