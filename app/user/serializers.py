"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from django.utils.translation import gettext as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user Object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password':{'write_only': True, 'min_length':5}}

    def create(self, validate_data):
        """create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validate_data)

    def update(self, instance, validate_date):
        """Update and return user"""
        password = validate_date.pop('password', None)
        user = super().update(instance, validate_date)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and autheticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg  = _('Unable to autheticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs