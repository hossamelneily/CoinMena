from django.db import models


class Currency(models.Model):
    fiat = models.CharField(max_length=100, verbose_name='Physical Currency')
    crypto = models.CharField(max_length=100, verbose_name='CryptoCurrency')
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Exchange Rate')
    refreshed_date = models.DateTimeField(verbose_name="Last Refreshed Date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{crypto}_{fiat}'.format(crypto=self.crypto, fiat=self.fiat)
