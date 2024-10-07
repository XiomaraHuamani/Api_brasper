from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Currency, ExchangeRate, Commission, Range
from .serializers import CurrencySerializer, ExchangeRateSerializer, CommissionSerializer, RangeSerializer

class CurrencyView(GenericAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        currencies = self.get_queryset()
        serializer = self.serializer_class(currencies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyDetailView(GenericAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, currency_id):
        return get_object_or_404(self.get_queryset(), id=currency_id)

    def get(self, request, currency_id):
        currency = self.get_object(currency_id)
        serializer = self.serializer_class(currency)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, currency_id):
        currency = self.get_object(currency_id)
        serializer = self.serializer_class(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, currency_id):
        currency = self.get_object(currency_id)
        currency.delete()
        return Response({"message": "Currency deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ExchangeRateView(GenericAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        exchange_rates = self.get_queryset()
        serializer = self.serializer_class(exchange_rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExchangeRateDetailView(GenericAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, exchange_rate_id):
        return get_object_or_404(self.get_queryset(), id=exchange_rate_id)

    def get(self, request, exchange_rate_id):
        exchange_rate = self.get_object(exchange_rate_id)
        serializer = self.serializer_class(exchange_rate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, exchange_rate_id):
        exchange_rate = self.get_object(exchange_rate_id)
        serializer = self.serializer_class(exchange_rate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, exchange_rate_id):
        exchange_rate = self.get_object(exchange_rate_id)
        serializer = self.serializer_class(exchange_rate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exchange_rate_id):
        exchange_rate = self.get_object(exchange_rate_id)
        exchange_rate.delete()
        return Response({"message": "Exchange rate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class RangeView(GenericAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        ranges = self.get_queryset()
        serializer = self.serializer_class(ranges, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RangeDetailView(GenericAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, range_id):
        return get_object_or_404(self.get_queryset(), id=range_id)

    def get(self, request, range_id):
        range_obj = self.get_object(range_id)
        serializer = self.serializer_class(range_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, range_id):
        range_obj = self.get_object(range_id)
        serializer = self.serializer_class(range_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, range_id):
        range_obj = self.get_object(range_id)
        range_obj.delete()
        return Response({"message": "Range deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class CommissionView(GenericAPIView):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        commissions = self.get_queryset()
        serializer = self.serializer_class(commissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommissionDetailView(GenericAPIView):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, commission_id):
        return get_object_or_404(self.get_queryset(), id=commission_id)

    def get(self, request, commission_id):
        commission = self.get_object(commission_id)
        serializer = self.serializer_class(commission)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, commission_id):
        commission = self.get_object(commission_id)
        serializer = self.serializer_class(commission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, commission_id):
        commission = self.get_object(commission_id)
        serializer = self.serializer_class(commission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, commission_id):
        commission = self.get_object(commission_id)
        commission.delete()
        return Response({"message": "Commission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)