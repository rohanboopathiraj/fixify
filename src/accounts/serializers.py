from rest_framework import serializers
from .models import FixifyUser


class FixifyUserSerializer(serializers.ModelSerializer):
    # Write-only field, not returned in response
    password = serializers.CharField(write_only=True)

    class Meta:
        model = FixifyUser
        fields = ['id', 'email', 'first_name',
                  'last_name', 'password', 'is_staff', 'is_active']

    def create(self, validated_data):
        user = FixifyUser.objects.create_user(**validated_data)
        user.save()
        return user
