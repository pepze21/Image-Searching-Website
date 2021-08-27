from django.urls import path
from . import views

'''
urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo')
]
'''

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_image, name='search_image')
]