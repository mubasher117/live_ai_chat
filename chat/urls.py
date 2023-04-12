from django.urls import path, include
from rest_framework import routers
from .views import ChatViewSet

router = routers.DefaultRouter()
router.register(r"chat", ChatViewSet, basename="chat")

urlpatterns = [
    path("", include(router.urls)),
]
