from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.authors=validated_data.get('authors', instance.authors)
        instance.content=validated_data.get('content', instance.content)
        instance.save()
        return instance