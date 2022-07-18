from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.serializers import users as user_serializer


class UserSignUp(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        return Response(status=status.HTTP_201_CREATED, data={})


class UserSignIn(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        user, token = user_serializer.login_user(
            email=request_data.get("email"), password=request_data.get("password")
        )
        return Response(status=status.HTTP_201_CREATED, data={})


class UserDetail(APIView):
    authentication_classes = (JWTAuthentication, )

    def perform_authentication(self, request):
        if not request.user.is_authenticated:
            raise ValueError("로그인이 필요한 기능입니다.")

    def get(self, request, *args, **kwargs):
        response_data = serializer_user(user=request.user)
        return Response(status=status.HTTP_200_OK, data=response_data)


class UserPasswordReset(APIView):
    def perform_authentication(self, request):
        pass
    
    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED, data={})
