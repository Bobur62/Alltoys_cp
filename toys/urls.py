from django.urls import path, re_path
from toys import views


# app_name = "toys"
urlpatterns = [
    # path('', views.dashboard, name="dashboard"),
    path('', views.DashboardView.as_view(), name="dashboard"),
    # path('toys/', views.get_toys, name="toys"),
    # path('toys/', views.GetToysView.as_view(), name="toys"),
    path('toys/', views.ToysListView.as_view(), name="toys"),
    # path('toys/<int:id>/', views.get_toy_detail, name="toy_detail"),
    # re_path('^toys/(?P<id>d+)/$', views.get_toy_detail, name="toy_detail"),
    path('toys/create/', views.ToyCreateView.as_view(), name="toys_create "),
    path('toys/<int:pk>/', views.ToyDetailView.as_view(), name="toy_detail"),
]
