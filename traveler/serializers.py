from rest_framework import serializers
from .models import Photo, Diagnosis

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo 
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis 
        fields = '__all__'
