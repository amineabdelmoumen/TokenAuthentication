from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(['POST',])
def RegisterNewUser(request):
    serializer=UserSerializer(data=request.data)
    data={}
    if serializer.is_valid():   
        account=serializer.save()
        data["success"]="sucessfully register a new user"
        data['username']=account.username        
        data['email']=account.email 
        token=Token.objects.get(user=account).key
        data['token']=token              
    else:
        data=serializer.errors
    return Response(data)