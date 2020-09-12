from django.shortcuts import render
from . models import Post
from .serializer import PostSerializer

#cbv
# api 상에 crud를 가능하게하는 class
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
