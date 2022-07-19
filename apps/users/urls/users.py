from django.urls import path

from users.views import users as user_views

urlpatterns = [
    path('signin', user_views.UserSignIn.as_view()),
    path('signup', user_views.UserSignUp.as_view()),
    path('me', user_views.UserDetail.as_view()),
    path('password/reset', user_views.UserPasswordReset.as_view())
]
