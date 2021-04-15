from .serializers import gov_thaiSerializer
from .models import gov_thai
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class gov_thaiList(APIView):
    """
    List all Result
    """
    
    def get(self, request, format=None):
        results = gov_thai.objects.all()
        serializer = gov_thaiSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = gov_thaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class gov_thaiDetail(APIView):
    """
    Retrieve, update or delete a Result Instance
    """
    def get_object(self, pk):
        try:
            return gov_thai.objects.get(pk=pk)
        except gov_thai.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = gov_thaiSerializer(gov_thai)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        result = self.get_object(pk)
        serializer = gov_thaiSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        result = self.get_objects(pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

