from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

# GET all stocks and POST a new one
@api_view(['GET', 'POST'])
def stock_list(request):
    if request.method == 'GET':
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# GET, PUT, DELETE single stock
@api_view(['GET', 'PUT', 'DELETE'])
def stock_detail(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
