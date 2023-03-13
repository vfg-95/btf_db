from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):

    def get(self, request):
        posts = Post.objects.all().order_by('-posted_at')
        return Response(posts)
