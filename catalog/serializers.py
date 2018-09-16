from rest_framework import serializers
from . import models


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Foto
        fields = ('name', 'text', 'image', 'date_added',)