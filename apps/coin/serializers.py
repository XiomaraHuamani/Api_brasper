from rest_framework import serializers
from .models import Currency, ExchangeRate, Commission, Range

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name', 'symbol', 'is_active', 'created_date', 'created_by']

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['id', 'base_currency', 'target_currency', 'rate', 'created_date', 'created_by']

class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = ['id', 'min_amount', 'max_amount', 'created_date', 'created_by']

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'base_currency', 'target_currency', 'range', 'commission_percentage', 'reverse_commission', 'created_date', 'created_by']