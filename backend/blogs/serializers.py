from rest_framework import serializers
from .models import blog

class BlogSerializer(serializers.Serializer):
    class Meta:
        model = blog
        fields = '__all__'

        def create(self, validated_data):
            return blog.objects.create(**validated_data)
        
        def update(self, blog, validated_data):
            blog.title=validated_data.get('title', blog.title)
            blog.authors=validated_data.get('authors', blog.authors)
            blog.content=validated_data.get('content', blog.content)
            blog.save()
            return blog