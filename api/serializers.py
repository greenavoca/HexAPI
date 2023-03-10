from rest_framework import serializers
from .models import Image



class ImageSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = [
            'id',
            'image',
            'image_thumbnail'
        ]
