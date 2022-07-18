from users.models.users import User


def serializer_user(user: User) -> dict:
    result = dict()
    result["id"] = user.id
    result["name"] = user.name
    result["nickname"] = user.nickname
    result["phone_number"] = user.phone_number
    result["created_at"] = user.created_at.astimezone()
    return result
