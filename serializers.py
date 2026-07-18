from rest_framework import serializers
from .models import Task

# Для списка (кратко)
class TaskShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'created_at']

# Для деталей (подробно)
class TaskFullSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    tags_list = serializers.StringRelatedField(source='tags', many=True, read_only=True)
    author = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'
