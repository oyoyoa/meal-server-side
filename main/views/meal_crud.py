from main.models import FoodConfigParam
from main.serializers import FoodConfigParamSerializer
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class RandomFoodConfigList(ListCreateAPIView):
    queryset = FoodConfigParam.objects.all()
    serializer_class = FoodConfigParamSerializer
    def create(self, request, *args, **kwargs):
        if type(request.data) == list:
            serializers = []
            for config in request.data:
                serializer = self.get_serializer(data=config)
                if serializer.is_valid():
                    serializers.append(serializer)
                else:
                    return Response(serializer.errors)
            for serializer in serializers:
                serializer.save(user=request.user)
            serializer = self.get_serializer(self.queryset.filter(user=request.user), many=True)
            return Response({'data': serializer.data})

        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({'data': serializer.data})

        return Response(serializer.errors)

class UserFoodConfig(GenericAPIView):
    queryset = FoodConfigParam.objects.all()
    serializer_class = FoodConfigParamSerializer

    def post(self, request):
        food_name = ['牛肉', '豚肉', '鶏肉', '鯖', 'イワシ', 'にんじん', 'キャベツ', '玉ねぎ', 'じゃがいも', 'もやし']
        food_type = ['meat', 'meat', 'meat', 'fish', 'fish', 'vegetable', 'vegetable', 'vegetable', 'vegetable', 'vegetable']
        foods = []
        foodConfigParams = FoodConfigParam.objects.filter(user=request.user)
        if foodConfigParams.first() is not None:
                serializer = FoodConfigParamSerializer(foodConfigParams, many=True)
                return Response({'data': serializer.data})
        for num in range(len(food_name)):
            food = FoodConfigParam.objects.create(name=food_name[num], food_type=food_type[num], rate=100, user=request.user)
            food.save()
            serializer = FoodConfigParamSerializer(food)
            foods.append(serializer.data)
        return Response({'data': foods})

    def get(self, request):
        foodConfigParams = FoodConfigParam.objects.filter(user=request.user)
        serializer = FoodConfigParamSerializer(foodConfigParams, many=True)
        return Response({'data': serializer.data})

    def put(self, request):
        res = []
        for config in request.data['data']:
            name = config['name']
            rate = config['rate']
            foodConfigParam = FoodConfigParam.objects.get(user=request.user, name=name)
            serializer = FoodConfigParamSerializer(foodConfigParam, data={'rate': rate}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            res.append(serializer.data)
        return Response({'data': res})
