from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat_view(request):
    """Create a new conversation or add message to existing conversation"""
    data = request.data
    user = request.user

    try:
        conversation = Conversation.objects.create(
            user=user,
            title=data.get('title', 'New Conversation')
        )
        
        # Add user message
        if 'message' in data:
            Message.objects.create(
                conversation=conversation,
                role='user',
                content=data['message']
            )
        
        serializer = ConversationSerializer(conversation, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def conversation_list_view(request):
    """Get all conversations for authenticated user"""
    conversations = Conversation.objects.filter(user=request.user)
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def conversation_detail_view(request, pk):
    """Get specific conversation with messages"""
    try:
        conversation = Conversation.objects.get(_id=pk, user=request.user)
        serializer = ConversationSerializer(conversation, many=False)
        return Response(serializer.data)
    except Conversation.DoesNotExist:
        return Response({'detail': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)
