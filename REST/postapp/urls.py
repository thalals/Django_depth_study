from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# djagon rest framework -> router 통해서 -> url 받아옴

#postviewset을 통해 router 정의
router = DefaultRouter()
router.register('post', views.PostViewset)

urlpatterns = [
    path('', include(router.urls))
]