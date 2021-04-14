from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lao-vip', views.lao_vipViewSet)
router.register(r'lao-lotto', views.lao_lottoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
