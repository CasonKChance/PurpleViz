from rest_framework import serializers
from .models import Mat

class MatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mat
        fields = ['id', 'matWidth', 'matLength', 'matSize']
