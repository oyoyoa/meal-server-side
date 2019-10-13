from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('signup/', views.RegisterAuthView.as_view()),
    path('signin/', views.AuthView.as_view()),
    path('randomMeal/', views.RandomMeal.as_view()),
    path('randomMeal/config/', views.RandomMealConfigList.as_view()),
    path('randomMeal/user/configDetail/', views.RandomMealConfigDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)