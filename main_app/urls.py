from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/', views.account_index, name='account-index'),
path('accounts/<int:account_id>/', views.account_detail, name='account-detail'), 
]