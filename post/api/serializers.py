from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from post.models import Post

class Postserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']