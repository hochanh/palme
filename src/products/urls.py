from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_canceled/', views.payment_canceled, name='payment_canceled'),
]
