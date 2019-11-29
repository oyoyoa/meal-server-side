from main.models import User, FoodConfigParam
from main.serializers import AuthSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import random

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterAuthView(GenericAPIView):
    permission_classes = ()
    serializer_class = AuthSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if User.objects.filter(uuid=serializer.data['uuid']):
            user = User.objects.get(uuid=serializer.data['uuid'])
            payload = jwt_payload_handler(user)
            return Response({
                'token': jwt_encode_handler(payload),
            })

        user = User.objects.create_user(uuid=serializer.data['uuid'])
        user.save()
        if not user:
            raise AuthenticationFailed()
        payload = jwt_payload_handler(user)
        user = User.objects.filter(uuid=serializer.data['uuid']).last()
        food = FoodConfigParam()
        food.create_defaultfood(user=user)
        return Response({
            'token': jwt_encode_handler(payload),
        })
