from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializer import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(publisher=True)
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['category','category__title'] #con esto puedo filtrar por id de categoria  y nombre de categoria