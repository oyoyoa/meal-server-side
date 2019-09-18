from main.models import FoodConfigParam
from main.serializers import FoodConfigParamSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import random


class RandomMeal(APIView):
    def get(self, request, format=None):
        foodConfigParams = FoodConfigParam.objects.filter(user=request.user)
        serializer = FoodConfigParamSerializer(foodConfigParams, many=True)
        foods = []
        for i in range(len(serializer.data)):
            if serializer.data[i]['percent'] == 0:
                continue
            foods.append(serializer.data[i]['name'])
        food = random.choice(foods)
        return Response(food)