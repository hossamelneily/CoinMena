import pytz
import requests
from django.conf import settings
from project.celery import app
from datetime import datetime
from project.apps.Currency.models import Currency

ALPHAVANTAGE_API_URL = settings.ALPHAVANTAGE_API_URL
ALPHAVANTAGE_API_URL_FUNCTION = settings.ALPHAVANTAGE_API_URL_FUNCTION
ALPHAVANTAGE_API_KEY = settings.ALPHAVANTAGE_API_KEY


@app.task(name='realtime-exchange-rate')
def get_exchange_rate():
    api_endpoint = ALPHAVANTAGE_API_URL + '?function={function}&from_currency=BTC&' \
                                          'to_currency=USD&apikey={key}'. \
        format(function=ALPHAVANTAGE_API_URL_FUNCTION, key=ALPHAVANTAGE_API_KEY)
    response = requests.get(api_endpoint)
    try:
        response.raise_for_status()
    except ConnectionError as e:
        print(e)
    res = response.json()
    if 'Error Message' in res:
        error_message = res['Error Message']
        print(error_message)
    if 'Note' in res:
        print(res['Note'])
    try:
        realtime_exchange_rate = res['Realtime Currency Exchange Rate']
        fiat_currency = realtime_exchange_rate['1. From_Currency Code']
        crytpo_currency = realtime_exchange_rate['3. To_Currency Code']
        exchange_rate = realtime_exchange_rate['5. Exchange Rate']
        refreshed_date = realtime_exchange_rate['6. Last Refreshed']
        timezone = pytz.timezone(realtime_exchange_rate['7. Time Zone'])
        refreshed_date_with_tz = timezone.localize(datetime.strptime(refreshed_date, '%Y-%m-%d %H:%M:%S'))
        Currency.objects.create(fiat=crytpo_currency, crypto=fiat_currency, exchange_rate=exchange_rate,
                                refreshed_date=refreshed_date_with_tz)
    except KeyError as e:
        print(e)


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3600.0, get_exchange_rate.s(), name='get-exchange-rate-hourly')
