from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chat.views import ChatViewSet
router = routers.DefaultRouter()
router.register(r"chat", ChatViewSet, basename="chat")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
