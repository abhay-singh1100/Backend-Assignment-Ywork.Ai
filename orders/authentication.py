from rest_framework import authentication, exceptions
from django.contrib.auth.models import User
from .oauth_models import UserSocialAuth

class GoogleOAuth2Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        access_token = auth_header.split(' ')[1]
        try:
            user_auth = UserSocialAuth.objects.get(access_token=access_token)
            user = user_auth.user
            return (user, None)
        except UserSocialAuth.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid or expired token') 