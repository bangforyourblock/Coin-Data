from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import services
from django.views import generic
from django.shortcuts import render_to_response



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def coinPage(request):
    coins_list = {}
    return render(request, 'CoinData.html',coins_list)



def topCoins(request):
    return HttpResponse(services.get_coins(5))


# Create your views here.
