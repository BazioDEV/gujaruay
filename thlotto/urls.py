from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from thlotto import views

urlpatterns = [
    path(r'result/', views.gov_thaiList.as_view()),
    path(r'result/<int:pk>/', views.gov_thaiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)