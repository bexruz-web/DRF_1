from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, CategoryViewSet, BookViewSet

router = routers.DefaultRouter()

router.register(r"authors", AuthorViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"books", BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]