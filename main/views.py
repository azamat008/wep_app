from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Azamat text')


# def about(reguest):
#     return HttpResponse('change')

def index(reguest):
    return render(reguest, 'index.html')

# def index(reguest):
#     return HttpResponse('detaling')
#
#
# def model(reguest):
#     return HttpResponse('navis')


