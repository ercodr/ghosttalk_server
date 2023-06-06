from rest_framework.serializers import ModelSerializer
from .models import Message, Profile


class MessageSerializers(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ProfileSerializers(ModelSerializer):
    profile_messages = MessageSerializers(many=True)
    class Meta:
        model = Profile
        fields = '__all__'