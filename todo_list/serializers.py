from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['url', 'id', 'title', 'is_completed', 'created_at', 'update_at']
