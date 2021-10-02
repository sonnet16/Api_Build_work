from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Info

from .serializer import InfoSerializer

# Create your views here.

@api_view(['GET'])
def getAllContact(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
    print(query)
    contact = Info.objects.filter(name__icontains=query)
    serializer = InfoSerializer(contact, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createContact(request):
    serializer = InfoSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)