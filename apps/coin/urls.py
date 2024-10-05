from django.urls import path
from .views import (
    CurrencyView, CurrencyDetailView,
    ExchangeRateView, ExchangeRateDetailView,
    CommissionView, CommissionDetailView,
    RangeView, RangeDetailView
)

urlpatterns = [
    path('currencies/', CurrencyView.as_view(), name='currency-list'),
    path('currencies/<int:currency_id>/', CurrencyDetailView.as_view(), name='currency-detail'),
    path('exchange-rates/', ExchangeRateView.as_view(), name='exchange-rate-list'),
    path('exchange-rates/<int:exchange_rate_id>/', ExchangeRateDetailView.as_view(), name='exchange-rate-detail'),
    path('ranges/', RangeView.as_view(), name='range-list'),
    path('ranges/<int:range_id>/', RangeDetailView.as_view(), name='range-detail'),
    path('commissions/', CommissionView.as_view(), name='commission-list'),
    path('commissions/<int:commission_id>/', CommissionDetailView.as_view(), name='commission-detail'),
]