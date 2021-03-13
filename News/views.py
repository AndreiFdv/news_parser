from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    html = '<body><h1>MEME</h1></body>'
    return HttpResponse(html)


class IndexView(generic.ListView):
    template_name = 'news/base.html'

    def get_queryset(self):
        pass
