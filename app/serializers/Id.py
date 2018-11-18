from rest_framework import serializers
from app.models import ChefProfile, UserProfile

class getChefProfileId(serializers.ModelSerializer):
    class Meta:
        model = ChefProfile
        fields = ("id",)

class getUserProfileId(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id",)