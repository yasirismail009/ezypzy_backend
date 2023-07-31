from rest_framework import serializers
from .models import fileTable

class FileTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = fileTable
        fields = '__all__'