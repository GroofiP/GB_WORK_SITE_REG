from django.urls import path
from ordersapp import views as ordersapp

app_name = "ordersapp"

urlpatterns = [
    path('', ordersapp.OrderListView.as_view(), name="orders"),
    path('create/', ordersapp.OrderCreateView.as_view(), name="order_create"),
    path('read/<int:pk>/', ordersapp.OrderDetailView.as_view(), name="order_read"),
    path('edit/<int:pk>/', ordersapp.OrderUpdateView.as_view(), name="order_update"),
    path('delete/<int:pk>/', ordersapp.OrderDeleteView.as_view(), name="order_delete"),
    path('complete/<int:pk>/', ordersapp.order_forming_complete, name="order_forming_complete"),
]
