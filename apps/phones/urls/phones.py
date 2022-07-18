from django.urls import path

from phones import views

urlpatterns = [
    path('generate-code', views.VerificationPhoneNumberCodeGenerate.as_view()),
    path('verify', views.VerificationPhoneNumberVerify.as_view())
]
