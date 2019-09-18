from main.models import FoodConfigParam
from main.serializers import FoodConfigParamSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class RandomMealConfigList(ListCreateAPIView):
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
            return Response(serializer.data)

        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)

        return Response(serializer.errors)


class RandomMealConfigDetail(RetrieveUpdateDestroyAPIView):
    queryset = FoodConfigParam.objects.all()
    serializer_class = FoodConfigParamSerializer