
from rest_framework import serializers

from phones.models import phones as models


class PhoneNumberSerializer(serializers.ModelSerializer):
    key = serializers.CharField(read_only=True)
    code = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = models.VerificationPhoneNumber
        fields = ["phone_number", "key", "code"]


class PhoneNumberCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.VerificationPhoneNumber
        fields = ["code", "phone_number"]
