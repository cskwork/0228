from django.urls import path
from . import views


urlpatterns = [
    #path('', views.board, name="board"),
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    #comment forms display with this
    #path('<slug:slug>/', views.post_detail.as_view(), name='post_detail'),
]