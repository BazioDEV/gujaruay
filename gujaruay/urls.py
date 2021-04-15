from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.urls import path, include
from laolotto import views
from thlotto import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name="index"),
    path('th/', include('thlotto.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    
] 


