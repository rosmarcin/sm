from django.shortcuts import render

from rest_framework import generics, viewsets

from rsm.models import UserProfile, SalesModel, ParametersGroup, Parameter
from rsm.serializers import UserProfileSerializer, SalesModelSerializer, ParametersGroupSerializer, ParameterSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    User Profile CRUD.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SalesModelViewSet(viewsets.ModelViewSet):
    """
    Sales Model CRUD.
    """
    queryset = SalesModel.objects.all()
    serializer_class = SalesModelSerializer

class ParametersGroupViewSet(viewsets.ModelViewSet):
    """
    Parameters Group CRUD.
    """
    queryset = ParametersGroup.objects.all()
    serializer_class = ParametersGroupSerializer

class ParameterViewSet(viewsets.ModelViewSet):
    """
    Parameters CRUD.
    """
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
