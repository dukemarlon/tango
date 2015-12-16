from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#    return HttpResponse("Rango says hey there world!"
#                        "<br /><br /><a href=http://192.168.1.159:8000/rango/about/>About</a>"
    context_dict = { 'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)
#)


def about(request):
#    return HttpResponse("Rango says here is the about page."
#                        "<br /><br /><a href=http://192.168.1.159:8000/rango/>Main</a>")
    return render(request, 'rango/about.html')
