from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

articles = {
    'sports' : 'SPORTS PAGE',
    'finance' : 'FINANCE PAGE',
    'politics' : 'POLITICS PAGE'
}

def simple_view(request):
    return HttpResponse("Simple View")

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = 'No Page for that Topic'   
        #return HttpResponseNotFound(result)
        raise Http404("404 GENERIC ERROR")

def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))


def num_page_view(request, num_page):
    topics_list = list(articles.keys()) # refactor code
    topic = topics_list[num_page]

    webpage = reverse('topic-page', args=[topic])

    return HttpResponseRedirect(webpage)



# def sports_view(request):
#     return HttpResponse('Sports Page')

# def finance_view(request):
#     return HttpResponse('Finance Page')
