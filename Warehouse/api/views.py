from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

'''HelloApiView and connected elements are based on LondonAppDev training course about APIs'''

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of api view info"""

        an_apiview = ['Apple', 'Grapes']

        return Response({'message': an_apiview})

    def post(self, request):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Tests put request for updating whole object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Tests patch request for partial update"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Tests delete request for delete ;)"""
        return Response({'message': 'DELETE'})