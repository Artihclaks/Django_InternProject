from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='getRoutes'),
    path('<str:pk>/',views.getRoute, name='getRoute')
]

