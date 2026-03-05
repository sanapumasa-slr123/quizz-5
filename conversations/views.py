from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .ai_service import get_ai_response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat_view(request):
    """Create a new conversation with AI response"""
    data = request.data
    user = request.user

    try:
        conversation = Conversation.objects.create(
            user=user,
            title=data.get('title', 'New Conversation')
        )
        
        # Add user message
        user_message_content = data.get('message', '')
        if user_message_content:
            Message.objects.create(
                conversation=conversation,
                role='user',
                content=user_message_content
            )
            
            # Get AI response
            messages = [{'role': 'user', 'content': user_message_content}]
            ai_response = get_ai_response(messages)
            
            # Save AI response
            Message.objects.create(
                conversation=conversation,
                role='assistant',
                content=ai_response
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_message_view(request, pk):
    """Add a message to existing conversation and get AI response"""
    data = request.data
    user = request.user
    
    try:
        conversation = Conversation.objects.get(_id=pk, user=user)
        
        # Add user message
        user_message_content = data.get('message', '')
        if not user_message_content:
            return Response({'detail': 'Message content is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        Message.objects.create(
            conversation=conversation,
            role='user',
            content=user_message_content
        )
        
        # Get conversation history for context
        messages = [
            {'role': msg.role, 'content': msg.content}
            for msg in conversation.messages.all()
        ]
        
        # Get AI response
        ai_response = get_ai_response(messages)
        
        # Save AI response
        Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=ai_response
        )
        
        serializer = ConversationSerializer(conversation, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response({'detail': 'Conversation not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
