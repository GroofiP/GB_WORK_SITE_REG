from django.urls import path
from adminapp import views as adminapp

app_name = "adminapp"

urlpatterns = [

    # Users

    path('users/create/', adminapp.UserCreateView.as_view(), name="user_create"),
    # path('users/create/', adminapp.user_create, name="user_create"),
    path('users/read/', adminapp.UsersListView.as_view(), name="users"),
    # path('users/read/', adminapp.users, name="users"),
    path('users/update/<pk>/', adminapp.UserUpdateView.as_view(), name="user_update"),
    # path('users/update/<pk>/', adminapp.user_update, name="user_update"),
    path('users/delete/<pk>/', adminapp.UserDeleteView.as_view(), name="user_delete"),
    # path('users/delete/<pk>/', adminapp.user_delete, name="user_delete"),

    # Category -- CBA переход осуществлен

    # path('category/create/', adminapp.category_create, name="category_create"),
    path('category/create/', adminapp.ProductCategoryCreateView.as_view(), name="category_create"),
    # path('category/read/', adminapp.categories, name="categories"),
    path('category/read/', adminapp.ProductCategoryListView.as_view(), name="categories"),
    # path('category/update/<pk>/', adminapp.category_update, name="category_update"),
    path('category/update/<pk>/', adminapp.ProductCategoryUpdateView.as_view(), name="category_update"),
    # path('category/delete/<pk>/', adminapp.category_delete, name="category_delete"),
    path('category/delete/<pk>/', adminapp.ProductCategoryDeleteView.as_view(), name="category_delete"),

    # Product

    # path('product/create/category/<pk>/', adminapp.product_create, name="product_create"),
    path('product/create/category/<pk>/', adminapp.ProductCreateView.as_view(), name="product_create"),
    # path('product/products/category/<pk>/', adminapp.products, name="products"),
    path('product/products/category/<pk>/', adminapp.ProductListView.as_view(), name="products"),
    # path('product/read/<pk>/', adminapp.product_read, name="product_read"),
    path('product/read/<pk>/', adminapp.ProductDetailView.as_view(), name="product_read"),
    # path('product/update/<pk>/', adminapp.product_update, name="product_update"),
    path('product/update/<pk>/', adminapp.ProductUpdateView.as_view(), name="product_update"),
    # path('product/delete/<pk>/', adminapp.product_delete, name="product_delete"),
    path('product/delete/<pk>/', adminapp.ProdoctDeleteView.as_view(), name="product_delete")

]

