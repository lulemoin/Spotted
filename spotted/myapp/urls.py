from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/<int:book_id>', views.book_by_id, name="book_by_id"),
    path('profile', views.profile),
    path('welcome', views.welcome, name="welcome"),
    path('test_pic', views.test_pic, name="test_pic"),
]
