from rest_framework import serializers
from main.models import FoodConfigParam
from main.models import User


class AuthSerializer(serializers.Serializer):
    uuid = serializers.CharField()

    class Meta:
        model = User
        fields = ('uuid')

class FoodConfigParamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False)
    user = AuthSerializer(required=False)
    class Meta:
        model = FoodConfigParam
        fields = ('id', 'name', 'percent', 'user')