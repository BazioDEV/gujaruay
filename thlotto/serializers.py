from rest_framework import serializers
from .models import gov_thai

class gov_thaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = gov_thai
        fields = '__all__'