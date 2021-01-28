from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPage(request):
    name = "siva"
    # myname = {'myname':name}
    return render(request,'loginapp/index.html',{'name':name})
