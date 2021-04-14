from rest_framework import viewsets
from .serializers import lao_vipSerializer, lao_lottoSerializer
from .models import *

class lao_vipViewSet(viewsets.ModelViewSet):
    queryset = lao_vip.objects.all()
    serializer_class = lao_vipSerializer
    
class lao_lottoViewSet(viewsets.ModelViewSet):
    queryset = lao_lotto.objects.all()
    serializer_class = lao_lottoSerializer