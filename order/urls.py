from django.urls import path
from order import views

urlpatterns = [
    path('list/<customer>/', views.OrderList.as_view(), name='list'),
    path('create/', views.OrderCreate.as_view(), name='create'),
    path('modify/<int:pk>/', views.OrderModify.as_view(), name='modify'),
]
