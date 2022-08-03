from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken


class Email:
    @staticmethod
    def send_email(user_email, subject, message):
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])


def get_user_by_token(token):
    access_token_obj = AccessToken(token)
    user_id = access_token_obj['user_id']
    user = User.objects.get(id=user_id)
    return user
