from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile_update(request):
    if request.method=='PUT':
        serializer=ProfileSerializer(request.user,data=request.data,partial=True,context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def profile(request,username):
    person=get_object_or_404(get_user_model(),username=username)
    if request.method=='GET':
        serializer=ProfileSerializer(person,context={'request':request})
        return Response(serializer.data)
    elif request.method=='POST':
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
        serializer=ProfileSerializer(person,context={'request':request})
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def followers(request):
    followers=request.user.followers.all()
    if request.method=='GET':
        serializer=ProfileSerializer(followers,many=True)
        return Response(serializer.data)