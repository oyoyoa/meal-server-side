from rest_framework import serializers
from main.models import FoodConfigParam
from main.models import User


class AuthSerializer(serializers.Serializer):
    uuid = serializers.CharField()

    class Meta:
        model = User
        fields = ('uuid')

class FoodConfigParamSerializer(serializers.ModelSerializer):
    user = AuthSerializer(required=False)
    class Meta:
        model = FoodConfigParam
        fields = ('name', 'food_type', 'rate', 'user')
