# Authentication Endpoints
from rest_framework import generics, permissions, authentication, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Note
from .serializers import NoteSerializer, UserSerializer, UserLoginSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

# class LoginView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = UserSerializers
#     authentication_classes = (TokenAuthentication,)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = User.objects.filter(username=username).first()
#             if user and user.check_password(password):
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({"token": token.key})
#             else:
#                 return Response({"error": "Invalid username or password"}, status=400)
#         else:
#             if 'username' in serializer.errors:
#                 return Response({"error": "A user with that username already exists."}, status=400)
#             else:
#                 return Response(serializer.errors, status=400)
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials '}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Note Endpoints
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

class NoteShareView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NoteSearchView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return self.queryset.filter(title__icontains=query, owner=self.request.user)