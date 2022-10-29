from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewset

router_posts = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=PostApiViewset)