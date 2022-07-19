from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from phones.serializers import phones as phone_serializers
from phones.services import phones as phone_services


class VerificationPhoneNumberCodeGenerate(APIView):
    @swagger_auto_schema(
        request_body=phone_serializers.PhoneNumberSerializer,
        responses={201: phone_serializers.PhoneNumberCodeSerializer})
    def post(self, request, *args, **kwargs):
        serializer = phone_serializers.PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = phone_services.generate_code_phone_number(**serializer.validated_data)
        serializer = phone_serializers.PhoneNumberCodeSerializer(data={"code": phone_number.code})
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)


class VerificationPhoneNumberVerify(APIView):
    @swagger_auto_schema(
        request_body=phone_serializers.PhoneNumberCodeSerializer,
        responses={201: phone_serializers.PhoneNumberSerializer})
    def post(self, request, *args, **kwargs):
        serializer = phone_serializers.PhoneNumberCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = phone_services.verify_phone_number(**serializer.validated_data)
        serializer = phone_serializers.PhoneNumberKeySerializer(data={"key": phone_number.key})
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)
