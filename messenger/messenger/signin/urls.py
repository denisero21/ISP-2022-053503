from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name=''),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=''), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('main', views.main, name='main'),
    path('main/searh', views.search, name='search'),
    path('send/', views.RoomCreate.as_view(), name='send'),
]