from django.shortcuts import render
from .serializers import FixifyUserSerializer
from .models import FixifyUser
from rest_framework.response import Response
from rest_framework import generics


class FixifyUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = FixifyUser.objects.all()
    serializer_class = FixifyUserSerializer

