from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Blog, Member

#all blogs
@api_view(['GET'])
def display_all(request):
    blogs=Blog.objects.all()
    data=BlogSerializer(blogs, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


#specific blog
@api_view(['GET'])
def display_blog(request, id):
    try:
        blogs=Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data=BlogSerializer(blogs).data
    return Response(data=data, status=status.HTTP_200_OK)

#display members
@api_view(['GET'])
def display_members(request):
    members=Member.objects.all()
    data=MemberSerializer(members, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)