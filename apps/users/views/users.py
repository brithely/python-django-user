from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.serializers import users as user_serializers
from users.services import users as user_services


class UserSignUp(APIView):
    @swagger_auto_schema(
        request_body=user_serializers.UserSignUpSerializer,
        response={201: user_serializers.UserTokenSerializer})
    def post(self, request, *args, **kwargs):
        serializer = user_serializers.UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = user_services.signup_user(
            **serializer.validated_data
        )
        serializer = user_serializers.UserTokenSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)


class UserSignIn(APIView):
    @swagger_auto_schema(
        request_body=user_serializers.UserSignInSerializer,
        response={201: user_serializers.UserTokenSerializer})
    def post(self, request, *args, **kwargs):
        serializer = user_serializers.UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = user_services.login_user(
            **serializer.validated_data
        )
        serializer = user_serializers.UserTokenSerializer(data={"token": token})
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)


class UserDetail(APIView):
    authentication_classes = (JWTAuthentication, )

    def perform_authentication(self, request):
        if not request.user.is_authenticated:
            raise ValueError("로그인이 필요한 기능입니다.")

    @swagger_auto_schema(response={200: user_serializers.UserSerializer})
    def get(self, request, *args, **kwargs):
        serializer = user_serializers.UserSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserPasswordReset(APIView):
    @swagger_auto_schema(
        request_body=user_serializers.ResetPasswordSerializer,
        responses={201: None})
    def post(self, request, *args, **kwargs):
        serializer = user_serializers.ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_services.reset_password_user(
            **serializer.validated_data
        )
        return Response(status=status.HTTP_201_CREATED)
