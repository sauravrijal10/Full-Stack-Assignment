from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate


from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken



from .serializers import UserSerializer
from .models import User

# class UserListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class TaskRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User Registered'}, status = status.HTTP_201_CREATED)

    else:
        data = serializer.errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    refresh = RefreshToken.for_user(user)
    return Response({"message":"user logged-in",
                      "access_token":str(refresh.access_token),
                      "refresh_token":str(refresh)
                      })