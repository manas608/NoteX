from rest_framework import authentication

from rest_framework import authentication, exceptions
from rest_framework.authtoken.models import Token

class TokenAuthentication(authentication.TokenAuthentication):
    def authenticate_credentials(self, key):
        model = Token
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        return (token.user, token)