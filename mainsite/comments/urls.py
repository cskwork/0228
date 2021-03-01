from django.urls import path
from . import views


urlpatterns = [
    #path('', views.board, name="board"),
    path('', views.CommentList.as_view(), name='comments'),
    
]