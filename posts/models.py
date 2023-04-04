from django.db import models
from users.models import User
from django.db.models import SET_NULL
from categories.models import Category


class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    slug=models.SlugField(max_length=255,unique=True)
    miniature=models.ImageField(upload_to='posts/img/')
    created_at=models.DateTimeField(auto_now_add=True)
    publisher=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=SET_NULL, null=True) #si se borra el usuario, setea esto en null
    category=models.ForeignKey(Category, on_delete=SET_NULL, null=True)