from rest_framework import serializers
from quotes.models import Quote
from quotes.models import QuoteCatagory
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote','author']
class QuoteCategorySerializers(serializers.ModelSerializer):
    class Meta:

        model = QuoteCatagory
        fields = ('__all__')