from main.models import FoodConfigParam
from main.serializers import FoodConfigParamSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import random


class RandomFood(APIView):
    def get(self, request, format=None):
        foodConfigParams = FoodConfigParam.objects.filter(user=request.user)
        serializer = FoodConfigParamSerializer(foodConfigParams, many=True)
        foods = serializer.data

        count =0
        vegi_list=[]
        main_list=[]
        resultMeal=[]
        vegimax =0
        mainmax =0

        #野菜用の配列、肉魚用の配列作る
        for food in foods:
            if(food['food_type'] == 'vegetable'):
                vegi_list.append(food)
                vegimax +=int(food['rate'])
                
            else:
                main_list.append(food)
                mainmax +=int(food['rate'])
                
        randomNum =random.randrange((vegimax))
        for vegi in vegi_list:
            
            count +=vegi['rate']
            
            if randomNum < count:
                resultMeal.append(vegi['name'])
                break

        randomNum =random.randrange((mainmax))
        for main in main_list:
            
            count +=main['rate']
            
            if randomNum < count:
                resultMeal.append(main['name'])
                break
        return Response({'data': resultMeal})