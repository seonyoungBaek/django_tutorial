from django.urls import path
from articles import views

app_name = "articles"

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner, name='dinner'),
    #string으로, url변수명을 name으로 해서 아이디나 이름을 먼저 받는다. 
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.detail, name='detail'),
    #int(숫자)를 pk라는 변수명에 저장해서 건네주기
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),


]
