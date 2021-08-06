from rest_framework import serializers
from.models import User


class UserSerializer(serializers.ModelSerializer):

    last_login = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'second_name',
                  'last_login', 'is_active', 'password', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}
