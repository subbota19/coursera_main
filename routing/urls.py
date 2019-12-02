from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.NegativeIntConverter, 'negative_int')

urlpatterns = [
    path('simple_route/', views.simple_route, name="simple_route_1"),
    path('simple_route/<str:string>', views.simple_route, name="simple_route_2"),
    re_path(r'^slug_route/(?P<slug>([\w\d_-]{1,16})$)', views.slug_route, name='slug_route'),
    path('sum_route/<negative_int:number_1>/<negative_int:number_2>/', views.sum_route, name='sum_route'),
    path('sum_get_method/', views.sum_get_method, name='sum_get_method'),
    path('sum_get_method/<str:string>', views.sum_get_method, name='sum_get_method'),
    path('sum_post_method/', views.sum_post_method, name='sum_post_method'),

]
