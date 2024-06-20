from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import blog

@api_view(['GET'])
def display_all(request):
    blogs=blog.objects.all()
    data=BlogSerializer(blogs, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def display_blog(request, title):
    try:
        blogs=blog.objects.get(title=title)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data=BlogSerializer(blogs).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request)
    
@api_view(['PATCH'])
def edit(request)
