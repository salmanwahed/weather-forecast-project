from rest_framework import serializers
from .models import UserQuery


class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuery
        exclude = ['created_at']
