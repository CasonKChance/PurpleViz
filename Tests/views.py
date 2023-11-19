from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Tests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tests
from .serializers import TestsSerializer
from rest_framework import viewsets

# Create your views here.
    
class TestsListViewSet(viewsets.ModelViewSet):
        queryset = Tests.objects.all()
        serializer_class = TestsSerializer

class TestsList(APIView):
    
    def get(self, request, format=None):
        tests = Tests.objects.all()
        serializer = TestsSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)