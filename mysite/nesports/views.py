from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.core.signals import request_finished



# Create your views here.
def home(request):
    return HttpResponse("Welcome to the New England Sports")

def images(request):
    return render(request, 'nesports/index.html')

def patriots(request):
    table = "<table><tr><td>latha</td><td>100</td></tr><tr><td>daya</td><td>200</td></tr></table>"
    data_list = [[1,2],[3,4]]
#     return HttpResponse(table)
    return render(request, 'nesports/patriots.html', {"data":data_list})

def celtics(request):
    return render(request, 'nesports/table.html')

def redsox(request):
    return render(request, 'nesports/redsox.html')

def bruins(request):
    return render(request, 'nesports/bruins.html')
