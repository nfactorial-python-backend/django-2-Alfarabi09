from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name="news_list"),
    path('102/', views.news_detail, name="news_detail"),
    path('add/', views.add_news, name="add_news"),
]