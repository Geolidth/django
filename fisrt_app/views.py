from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic):
    try:
        result=articles[topic]
        return HttpResponse(result)
    except:
        raise Http404('404 GENERIC ERROR')

def add_view(request,num1,num2):
    result = num1 + num2
    return HttpResponse(str(result))
