from rest_framework import serializers
from project.apps.Currency.models import Currency


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['fiat', 'crypto', 'exchange_rate']
