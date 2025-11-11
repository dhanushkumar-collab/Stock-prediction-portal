from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Stock
from .serializers import StockSerializer


@api_view(['GET'])
def stock_list(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)

