from django.shortcuts import render,get_object_or_404

from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.http.response import HttpResponse

from .serializers import testnowtimeSerializer
from .models import testnowtime



# Create your views here.
class get_time(APIView):
    def get(self,request):
        result = testnowtime.objects.all()
        serializer = testnowtimeSerializer(result,many=True)

        return Response(serializer.data)
    def post(self, request):
        serial = testnowtimeSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

def index(request):
    print(request)
    return HttpResponse('HI')
class testD(APIView):
    def get(self,request,pk,format=None):
        nt = get_object_or_404(testnowtime,pk=pk)
        serial = testnowtimeSerializer(nt)
        return Response(serial.data)
