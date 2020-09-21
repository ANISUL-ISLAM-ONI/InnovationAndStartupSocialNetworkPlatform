from django.http import HttpResponse
from django.shortcuts import render

def datainput(request) :
    context = {
        #edit here
    }
    return render(request, 'input.html', context)

def dataoutput(request) :
    context = {
        #edit here
    }
    return render(request, 'output.html', context)
