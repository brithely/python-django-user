
from rest_framework import serializers

from phones.models import phones as models


class PhoneNumberKeySerializer(serializers.Serializer):
    key = serializers.CharField()


class PhoneNumberCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=False)
    code = serializers.CharField()


class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
