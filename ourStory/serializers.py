from rest_framework import serializers
from .models import Story
class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'title', 'description']