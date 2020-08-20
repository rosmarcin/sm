from rest_framework import serializers
from rsm.models import UserProfile, SalesModel, ParametersGroup, Parameter


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields="__all__"
#        fields = ("title", "artist")

class SalesModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalesModel
        fields="__all__"


class ParametersGroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParametersGroup
        fields="__all__"

class ParameterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parameter
        fields="__all__"

