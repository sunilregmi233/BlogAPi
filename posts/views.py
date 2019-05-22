from django.shortcuts import render

# Create your views here.
from rest_framework import generics 
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
# new
    queryset = Post.objects.all()
    serializer_class = PostSerializer