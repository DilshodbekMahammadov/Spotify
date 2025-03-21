from datetime import timedelta

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

# class QoshiqchiPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Qoshiqchi
#         fields = '__all__'
#
#     def validate_fayl(self, value):
#         if not value.lower().endswith('.mp3'):
#             raise serializers.ValidationError("Faqat .mp3 formatdagi fayllarga ruxsat beriladi.")
#         return value

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class JadvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadval
        fields = '__all__'

    def validate_davomiylik(self, value):
        max_davomiylik = timedelta(minutes=7)
        if value > max_davomiylik:
            raise ValidationError("Qo‘shiq davomiyligi 7 daqiqadan oshmasligi kerak.")
        return value