from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, filters
from .permissions import *


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):    
    queryset = Company.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields =("name",)
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]
    
class UserViewSet(viewsets.ModelViewSet):    
    queryset = User.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields =('username',)
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'username'
    
   
""" get_queryset(self) : Si l'utilisateur est Admin, elle renvoie tous les objets File. 
Si l'utilisateur est office, elle renvoie uniquement les objets File qui sont associés à la société de l'utilisateur. """

""" perform_create(self, serializer) : Cette méthode est appelée lorsqu'un nouvel objet File est créé via l'API. 
Elle associe le fichier à la Company de l'utilisateur actuellement authentifié. """

class FileViewSet(viewsets.ModelViewSet):    
    queryset = File.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields =("name",)
    serializer_class = FileSerializer
    permission_classes = [IsOfficeUser]

    def get_queryset(self): 
        user = self.request.user
        if user.is_staff:
            return File.objects.all()
        else:
            return File.objects.filter(company=user.company)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)
    
