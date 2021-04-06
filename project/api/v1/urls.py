from django.urls import path
from .views import *

urlpatterns = [
    path('quotes/', GetLastExchangeRate.as_view(), name='last_exchange_rate'),
]
