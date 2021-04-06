from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('fiat', 'crypto')
    list_display = [
        'crypto',
        'fiat',
        'exchange_rate',
        'refreshed_date'
    ]
