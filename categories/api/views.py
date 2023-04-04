from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    serializer_class=CategorySerializer
    #queryset=Category.objects.all() para que me devuelva todos
    #queryset=Category.objects.filter(publisher=True)  con esto puedo filtrar por un campo. 
    #lookup_field='slug' con esto puedo sustituir el metodo de busqueda en las peticiones, en vez de por ID se busca por slug. El campo especificado aca tiene que ser unique.
    queryset=Category.objects.all()
    filter_backends=[DjangoFilterBackend] #esto es para filtros por query
    filterset_fields=['publisher']