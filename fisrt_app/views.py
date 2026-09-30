from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

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

def num_page_view(reques,num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    return HttpResponseRedirect(topic)
