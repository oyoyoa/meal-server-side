from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('ping/', views.PingView.as_view()),
    path('signup/', views.RegisterAuthView.as_view()),
    path('signin/', views.AuthView.as_view()),
    path('randomMeal/', views.RandomMeal.as_view()),
    path('randomMeal/config/', views.RandomMealConfigList.as_view()),
    path('randomMeal/config/<int:pk>/', views.RandomMealConfigDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)