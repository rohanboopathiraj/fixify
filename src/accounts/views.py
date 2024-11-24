from .serializers import FixifyUserRegistrationSerializer, FixifyUserLoginSerializer
from .models import FixifyUser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from home.utils import response


class FixifyUserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FixifyUser.objects.all()
    serializer_class = FixifyUserRegistrationSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = FixifyUserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            user = authenticate(email=email, password=password)

            if user is not None:
                tokens = {
                    'access': str(AccessToken.for_user(user)),
                    'refresh': str(RefreshToken.for_user(user)),
                }

                response_data = {
                    "user": email,
                    "tokens": tokens
                }

                return response(status=True, message="Login successful",
                                data=response_data, http_status=status.HTTP_200_OK)
            else:
                return response(status=False, message="Invalid email or password",
                                http_status=status.HTTP_401_UNAUTHORIZED)

        return response(status=False, message="Invalid data", data={"errors": serializer.errors},
                        http_status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = FixifyUserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return response(status=True, message="User registered successfully.",
                            data=serializer.data, http_status=status.HTTP_201_CREATED)

        return response(status=False, message="Invalid data", data={"errors": serializer.errors},
                        http_status=status.HTTP_400_BAD_REQUEST)
