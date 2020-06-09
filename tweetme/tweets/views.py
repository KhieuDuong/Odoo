import random
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from .models import Tweet
# Create your views here.
def home_view(reqest, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(reqest, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 33) } for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return  JsonResponse(data)

def tweet_detail_view(reqest, tweet_id, *args, **kwargs):
    """
    Rest API view
    Con
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "No data"
        status = 404


    return JsonResponse(data, status =status)
