from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from project.apps.Currency.models import Currency

from project.api.v1.serializer import ExchangeRateSerializer
from project.api.tasks import get_exchange_rate


class GetLastExchangeRate(GenericAPIView):
    permission_classes = []
    serializer_class = ExchangeRateSerializer

    def get(self, *args, **kwargs):
        currency_obj = Currency.objects.all().order_by('-refreshed_date').first()
        if currency_obj:
            serializer = self.serializer_class(currency_obj, )
            return Response(serializer.data)
        get_exchange_rate.delay()
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, *args, **kwargs):
        get_exchange_rate.delay()
        return Response(status=status.HTTP_200_OK)
