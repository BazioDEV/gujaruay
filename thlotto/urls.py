from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'th_latest', views.gov_thaiViewSet)
# router.register(r'laos-vip', views.VipResultViewSet)
# router.register(r'laos-lotto', views.LottoResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]