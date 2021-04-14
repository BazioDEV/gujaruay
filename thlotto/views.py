from rest_framework import viewsets
from .serializers import gov_thaiSerializer
from .models import gov_thai

class gov_thaiViewSet(viewsets.ModelViewSet):
    queryset = gov_thai.objects.all()
    serializer_class = gov_thaiSerializer
