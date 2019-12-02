from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('signin/', views.RegisterAuthView.as_view()),
    path('randomFood/', views.RandomFood.as_view()),
    path('randomFood/config/', views.RandomFoodConfigList.as_view()),
    path('randomFood/user/config/', views.UserFoodConfig.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)