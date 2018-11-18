from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from app.serializers.User import *
from app.models import *

class ChefProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    def update(self, instance, validated_data):
        instance.dishes = validated_data.get("dishes", instance.dishes)
        instance.username = validated_data.get("username", instance.username)
        user_data = validated_data.pop("user")
        instance.user.first_name = user_data.get("fist_name", instance.user.first_name)
        instance.user.last_name = user_data.get("last_name", instance.user.last_name)
        instance.user.username = instance.username
        new_password = user_data.get("password")
        if(new_password):
            instance.user.set_password(new_password)
        instance.user.save()
        instance.save()
        return instance

    class Meta:
        model = ChefProfile
        fields = "__all__"

class ChefProfileSignupSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data, username = "chef_" + validated_data.get("username"))
        profile = ChefProfile.objects.create(user = user, **validated_data)
        return profile

    class Meta:
        model = ChefProfile
        fields = "__all__"