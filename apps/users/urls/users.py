from django.urls import path

from users.views.users import UserDetail, UserPasswordReset, UserSignIn, UserSignUp

urlpatterns = [
    path('signin', UserSignIn.as_view()),
    path('signup', UserSignUp.as_view()),
    path('me', UserDetail.as_view()),
    path('password/reset', UserPasswordReset.as_view())
]
