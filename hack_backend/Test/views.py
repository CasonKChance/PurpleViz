from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Test
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Test
from .serializers import TestSerializer


# Create your views here.
    
class TestList(APIView):
    def get(self, request, format=None):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)