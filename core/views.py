from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message, Profile
from .serializers import MessageSerializers, ProfileSerializers


@api_view(['GET'])
def messages(request, owner):   
    messages = Message.objects.filter(profile__user__username=owner)
    serializer = MessageSerializers(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, owner):
    profile = Profile.objects.filter(user__username=owner)
    if not profile:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfileSerializers(profile, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def response(request):
    data = request.data
    
    try:
        profile = Profile.objects.get(name=data['profile'])
    except Exception as e:
        return Response({'status': str(e)})
    
    try:
        Message.objects.create(
            profile=profile,
            content=data['content']
        )
    except Exception as e:
        return Response({'status' : e})
    return Response({'status': 'Response sent successfully!'})
    