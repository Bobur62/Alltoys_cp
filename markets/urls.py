from django.urls import path
from markets import views

urlpatterns = [
    path('', views.MarketListView.as_view(), name="markets"),
    path('market/', views.MarketProductsListView.as_view(), name="all_products")
]