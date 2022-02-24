from rest_framework import serializers
from .models import Product,Typelist,QuestionList


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ('name','taglist')

class TypelistSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Typelist
        fields = ('name',)
class QuestionListSerializers(serializers.ModelSerializer):
    class Meta:
        model  = QuestionList
        fields = ('que','ans1','ans2')
