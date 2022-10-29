from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import Postserializer

class PostApiViewset(ModelViewSet):
    serializer_class = Postserializer
    queryset = Post.objects.all()
