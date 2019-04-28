from rest_framework import generics

from quotes.models import Quote
from quotes.models import QuoteCatagory

from .serializers import QuoteSerializer
from .serializers import QuoteCategorySerializers

class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCatagory.objects.all()
    serializer_class = QuoteCategorySerializers
