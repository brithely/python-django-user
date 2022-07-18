from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from phones.serializers import phones as phone_serializers
from phones.services import phones as phone_services


class VerificationPhoneNumberCodeGenerate(APIView):
    @swagger_auto_schema(
        request_body=phone_serializers.PhoneNumberCodeSerializer,
        responses={201: phone_serializers.PhoneNumberCodeSerializer})
    def post(self, request, *args, **kwargs):
        serializer = phone_serializers.PhoneNumberCodeSerializer(data=request.data)
        phone_number = phone_services.generate_code_phone_number(serializer.data)
        response_body = phone_serializers.PhoneNumberCodeSerializer(phone_number)
        return Response(status=status.HTTP_201_CREATED, data=response_body.data)


class VerificationPhoneNumberVerify(APIView):
    @swagger_auto_schema(
        request_body=phone_serializers.PhoneNumberSerializer,
        responses={201: phone_serializers.PhoneNumberSerializer})
    def post(self, request, *args, **kwargs):
        serializer = phone_serializers.PhoneNumberSerializer(data=request.data)
        phone_number = phone_services.verify_phone_number(serializer.data)
        response_body = phone_serializers.PhoneNumberSerializer(phone_number)
        return Response(status=status.HTTP_201_CREATED, data=response_body.data)
