import uuid

from django.utils.crypto import get_random_string

from phones import models


def generate_code_phone_number(phone_number: str) -> models.VerificationPhoneNumber:
    """
    1) 번호 유효성 검증
    2) 같은 번호로 하루 10회만 가능
    """
    generate_code_phone_number = models.VerificationPhoneNumber()
    generate_code_phone_number.phone_number = phone_number
    generate_code_phone_number.key = uuid.uuid4().hex[:7]
    generate_code_phone_number.code = get_random_string(length=6, allowed_chars="0123456789")
    generate_code_phone_number.save()
    return generate_code_phone_number


def verify_phone_number(phone_number: str, code: str) -> models.VerificationPhoneNumber:
    phone_number = models.VerificationPhoneNumber.objects.filter(phone_number=phone_number).latest('created_at')
    if not phone_number.code == code:
        raise ValueError("코드가 잘못됨")
    phone_number.verify = True
    phone_number.save()
    return phone_number


def align_phone_number(key: str, user_id: int) -> bool:
    phone_number = models.VerificationPhoneNumber.objects.get(key=key)
    if not phone_number.verify:
        raise ValueError('번호 인증이 완료되지 않았습니다.')
    phone_number.user_id = user_id
    phone_number.save()
    return phone_number

