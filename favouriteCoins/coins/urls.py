from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [

    path('datetime', views.current_datetime),
    path('coinPage', views.coinPage),
    path('topcoins', views.topCoins),
    path('toppers', TemplateView.as_view(template_name='CoinData.html')),
    path('coinMiner.html', TemplateView.as_view(template_name='coinMiner.html')),

]
