from rest_framework import serializers
from rest_registration.api.serializers import DefaultRegisterUserSerializer

from .models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["name", "description"]


class RegisterSerializer(DefaultRegisterUserSerializer):
    primary_channel = ChannelSerializer()

    def create(self, validated_data):
        data = validated_data.copy()
        channel_data = data.pop("primary_channel")
        channel = Channel.objects.create(**channel_data)
        data["primary_channel"] = channel
        user = super().create(data)
        return user
