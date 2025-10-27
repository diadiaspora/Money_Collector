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
  path('crypto/create/', views.CryptoCreate.as_view(), name='crypto-create'),
  path('crypto/<int:pk>/', views.CryptoDetail.as_view(), name='crypto-detail'),
  path('crypto/', views.CryptoList.as_view(), name='crypto-index'),
  path('crypto/<int:pk>/update/', views.CryptoUpdate.as_view(), name='crypto-update'),
  path('crypto/<int:pk>/delete/', views.CryptoDelete.as_view(), name='crypto-delete'),
  path('accounts/<int:account_id>/associate-crypto/<int:crypto_id>/', views.associate_crypto, name='associate-crypto'),
  path('accounts/<int:account_id>/remove-crypto/<int:crypto_id>/', views.remove_crypto, name='remove-crypto'),

]
