from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

articles = {
    'sports' : 'SPORTS PAGE',
    'finance' : 'FINANCE PAGE',
    'politics' : 'POLITICS'
}

def simple_view(request):
    return HttpResponse("Simple View")

def news_view(request, topic):
    return HttpResponse(articles[topic])

# def sports_view(request):
#     return HttpResponse('Sports Page')

# def finance_view(request):
#     return HttpResponse('Finance Page')
