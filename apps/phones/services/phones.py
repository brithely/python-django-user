import re
import uuid

from django.utils import timezone
from django.utils.crypto import get_random_string
from rest_framework import exceptions

from phones.models import phones as phone_models


def generate_code_phone_number(phone_number: str) -> phone_models.VerificationPhoneNumber:
    if re.match(r"^01([0|1|6|7|8|9]?)([0-9]{3,4})([0-9]{4})$", phone_number) is None:
        raise exceptions.ValidationError({"detail": "잘못된 번호 입니다."})
    if phone_models.VerificationPhoneNumber.objects.filter(
            phone_number=phone_number, user__isnull=False, verify_type="S").exists():
        raise exceptions.ValidationError({"detail": "이미 인증 된 번호 입니다."})
    generate_code_phone_number = phone_models.VerificationPhoneNumber()
    generate_code_phone_number.phone_number = phone_number
    generate_code_phone_number.key = uuid.uuid4().hex[:7]
    generate_code_phone_number.code = get_random_string(length=6, allowed_chars="0123456789")
    generate_code_phone_number.save()
    return generate_code_phone_number


def verify_phone_number(phone_number: str, code: str) -> phone_models.VerificationPhoneNumber:
    if re.match(r"^01([0|1|6|7|8|9]?)([0-9]{3,4})([0-9]{4})$", phone_number) is None:
        raise exceptions.ValidationError({"detail": "잘못된 번호 입니다."})
    phone_number = phone_models.VerificationPhoneNumber.objects.filter(phone_number=phone_number).latest('created_at')
    if not phone_number.code == code:
        raise exceptions.ValidationError({"detail": "인증 번호가 올바르지 않습니다"})
    if phone_number.created_at.astimezone() + timezone.timedelta(minutes=10) < timezone.now().astimezone():
        raise exceptions.ValidationError({"detail": "인증 시간이 지났습니다"})
    phone_number.verify = True
    phone_number.save()
    return phone_number


def align_phone_number(key: str, user_id: int, verify_type: str) -> bool:
    phone_number = phone_models.VerificationPhoneNumber.objects.get(key=key)
    if not phone_number.verify:
        raise exceptions.ValidationError({"detail": "번호 인증이 완료되지 않았습니다."})
    phone_number.user_id = user_id
    phone_number.save()
    return phone_number


def get_verify_phone_number_by_key(key: str) -> str:
    try:
        phone_number = phone_models.VerificationPhoneNumber.objects.get(key=key)
    except phone_models.VerificationPhoneNumber.DoesNotExist:
        raise exceptions.ValidationError({"detail": "번호 인증이 완료되지 않았습니다."})
    if not phone_number.verify:
        raise exceptions.ValidationError({"detail": "번호 인증이 완료되지 않았습니다."})
    if phone_number.user_id:
        raise exceptions.ValidationError({"detail": "이미 등록된 번호입니다."})
    return phone_number.phone_number
