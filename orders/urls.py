from django.urls import path
from .views import OrderListCreateView
from .oauth_views import google_login, google_callback

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('auth/login/', google_login, name='google-login'),
    path('auth/callback/', google_callback, name='google-callback'),
] 