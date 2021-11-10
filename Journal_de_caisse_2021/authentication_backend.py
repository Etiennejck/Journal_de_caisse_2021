from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django_auth_adfs.backend import get_user_model
from .services.ldap import get_LDAP_user
from django.http import HttpResponseRedirect, HttpResponse


class AuthenticationBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        u = get_user_model()
        username = u.username#request.GET.get('username')
        password = u.password#request.GET.get('password')

        # Get the user information from the LDAP if he can be authenticated
        if get_user_model() is None:
            return None

        try:
            user = User.objects.get(username=username)
            if user.check_password(password) is True and user.groups.check(u.group):
                return user
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None