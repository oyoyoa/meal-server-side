from django.contrib.auth import authenticate
from main.models import FoodConfigParam, User
from main.serializers import FoodConfigParamSerializer
from main.serializers import AuthSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import random

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

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

class RandomMealConfigList(generics.ListCreateAPIView):
    queryset = FoodConfigParam.objects.all()
    serializer_class = FoodConfigParamSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class RandomMealConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodConfigParam.objects.all()
    serializer_class = FoodConfigParamSerializer

class AuthView(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = AuthSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(uuid=serializer.data['uuid'])
        if not user:
            raise AuthenticationFailed()
        payload = jwt_payload_handler(user)
        return Response({
            'token': jwt_encode_handler(payload),
        })

class RegisterAuthView(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = AuthSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(uuid=serializer.data['uuid']):
            message = {'detail': 'すでにそのユーザーは登録済みです。'}
            return Response(message)

        user = User.objects.create_user(uuid=serializer.data['uuid'])
        user.save()
        
        if not user:
            raise AuthenticationFailed()
        payload = jwt_payload_handler(user)
        return Response({
            'token': jwt_encode_handler(payload),
        })

class PingView(generics.GenericAPIView):
    def get(self, request, format=None):
        print('user', request.user)
        return Response(data={'uuid': ''})