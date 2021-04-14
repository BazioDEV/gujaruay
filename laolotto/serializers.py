from rest_framework import serializers
from .models import *

class lao_vipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lao_vip
        fields = '__all__'
        
class lao_lottoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lao_lotto
        fields = '__all__'

