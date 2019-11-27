from django.db import models
from .user import User


class FoodConfigParam(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=10)
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_defaultfood(self, user):
        food_name = ['牛肉', '豚肉', '鶏肉', '鯖', 'イワシ', 'にんじん', 'キャベツ', '玉ねぎ', 'じゃがいも', 'もやし']
        food_type = ['meat', 'meat', 'meat', 'fish', 'fish', 'vegetable', 'vegetable', 'vegetable', 'vegetable', 'vegetable']
        foodConfigParams = FoodConfigParam.objects.filter(user=user)
        for num in range(len(food_name)):
            food = FoodConfigParam.objects.create(name=food_name[num], food_type=food_type[num], rate=100, user=user)
            food.save()
        return None