from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    html = '<body><h1>MEME</h1></body>'
    return HttpResponse(html)
