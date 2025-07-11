from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/', views.account_index, name='account-index'),
  path('accounts/<int:account_id>/', views.account_detail, name='account-detail'), 
    path('accounts/create/', views.AccountCreate.as_view(), name='account-create'),
      path('accounts/<int:pk>/update/', views.AccountUpdate.as_view(), name='account-update'),
    path('accounts/<int:pk>/delete/', views.AccountDelete.as_view(), name='account-delete'),
  path(
        'accounts/<int:account_id>/add-transaction/', 
        views.add_transaction, 
        name='add-transaction'
    ),
]