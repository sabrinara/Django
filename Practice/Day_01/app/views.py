from django.shortcuts import render
import datetime
# Create your views here.
def index (request):
    d = {'plus' : 10 , 
         'value' : "I'm good!", 
         'Date' : datetime.datetime.now() , 
        'person' :  [
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
        {'name': 'zed', 'age': 19},] , 
        'number': 15 , 
        'string': "I <i>know </i> Myself!", 
        'filesize' :  123456789 , 
        'list' : [8,9,3,4,5,6] , 
        'line' : "one \n  two \n three" , 
        'first_date' : datetime.datetime(2023, 12, 6) ,
        'last_date' : datetime.datetime(2023, 12, 12) }
    return render(request, 'app/index.html', d)

