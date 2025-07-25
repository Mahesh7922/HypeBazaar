from django.urls import path
from ecommerceapp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('checkout/', views.checkout, name="checkout"),
    path('handlerequest/', views.handlerequest, name="handlerequest"),
    path('profile/', views.profile, name="profile"),
    path('view-order/<str:order_id>/', views.view_order, name="view_order"),
    # path('payment-callback/', views.payment_callback, name='payment_callback'),
    # path('payment-success/', views.payment_success, name='payment_success'),
]
