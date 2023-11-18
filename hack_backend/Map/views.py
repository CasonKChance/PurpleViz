from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Mat
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mat
from .serializers import MatSerializer


# Create your views here.
    
class MatList(APIView):
    def get(self, request, format=None):
        mats = Mat.objects.all()
        serializer = MatSerializer(mats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)