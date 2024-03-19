from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers


class UserCreateSerializer(UserCreateSerializer):
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({"Failed":"Passwords Do Not Match"})
     
        attrs.pop('confirm_password')

        return attrs

    class Meta(UserCreateSerializer.Meta):
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
            'confirm_password',
        ]


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        ref_name = 'users'
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number']