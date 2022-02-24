from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets

from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.http.response import HttpResponse

from .serializers import ProductSerializers,TypelistSerializers,QuestionListSerializers
from .models import Product,Typelist,QuestionList

def index(request):
    def asd(self,request):
        pass
    print(request)
    return HttpResponse('HI')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class TypelistViewSet(viewsets.ModelViewSet):
    queryset = Typelist.objects.all()
    serializer_class = TypelistSerializers

class QuestionlistViewSet(viewsets.ModelViewSet):
    queryset = QuestionList.objects.all()
    serializer_class = QuestionListSerializers

class ProductDetail(APIView):
    def get(self,request,pk,format=None):
        productobj = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(productobj)
        return Response(serializer.data)

class TypelistDetail(APIView):
    def get(self,request,pk,format=None):
        typeobj = get_object_or_404(Product,pk=pk)
        serializer = TypelistSerializers(productobj)
        return Response(serializer.data)

    '''
# Create your views here.
class SELlist(APIView):
    def get(self,request):
        result = Selector.objects.all()
        serializer = SelSerial(result,many=True)
        return Response(serializer.data)
    def post(self, request):
        serial = SelSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
class Quelist(APIView):
    def get(self,request):
        result = Quemod.objects.all()
        serializer = QueSerial(result,many=True)
        return Response(serializer.data)
    def post(self, request):
        serial = QueSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)



    
class testD(APIView):
    def get(self,request,pk,format=None):
        nt = get_object_or_404(Selector,pk=pk)
        serial = SelSerial(nt)
        return Response(serial.data)

class quep(APIView):
    def get(self,request,pk,format=None):
        nt = get_object_or_404(Quemod,pk=pk)
        serial = QueSerial(nt)
        return Response(serial.data)'''