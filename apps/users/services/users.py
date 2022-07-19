from django.db import transaction
from django.utils import timezone
from phones.services import phones as phone_services
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import exceptions

from users.models import users as user_models


def signup_user(email: str, password: str, name: str, nickname: str, key: str) -> user_models.User:
    with transaction.atomic():
        phone_number = phone_services.get_verify_phone_number_by_key(key)
        user = user_models.User()
        user.email = email
        user.set_password(password)
        user.phone_number = phone_number
        user.name = name
        user.nickname = nickname
        user.save()
        phone_services.align_phone_number(key=key, user_id=user.id, verify_type='S')
        token = AccessToken.for_user(user=user)
    return user, str(token)


def login_user(password: str, email: str = None, phone_number: str = None) -> user_models.User:
    if email is None and phone_number is None:
        raise exceptions.ValidationError({"detail": '이메일 또는 핸드폰 번호 입력 필요'})

    try:
        if email and phone_number:
            user = user_models.User.objects.get(email=email, phone_number=phone_number)
        elif email:
            user = user_models.User.objects.get(email=email)
        elif phone_number:
            user = user_models.User.objects.get(phone_number=phone_number)
    except user_models.User.DoesNotExist:
        raise exceptions.ValidationError({"detail": "아이디 또는 비밀번호가 잘못 되었습니다"})

    if not user.check_password(password):
        raise exceptions.ValidationError({"detail": "아이디 또는 비밀번호가 잘못 되었습니다"})

    user = user
    user.last_login = timezone.now()
    user.save()
    token = AccessToken.for_user(user=user)
    return user, str(token)


def reset_password_user(key: str, password: str) -> user_models.User:
    with transaction.atomic():
        phone_number = phone_services.get_verify_phone_number_by_key(key)
        user = user_models.User.objects.get(phone_number=phone_number)
        user.set_password(password)
        user.save()
        phone_services.align_phone_number(key=key, user_id=user.id, verify_type='R')
    return user
