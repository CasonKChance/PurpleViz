from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Cam
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cam
from .serializers import CamSerializer


# Create your views here.
    
class CamList(APIView):
    def get(self, request, format=None):
        cam = Cam.objects.all()
        serializer = CamSerializer(cam, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)