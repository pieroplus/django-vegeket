from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [

    # Account
    path('login/', Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('account/', AccountUpdateView.as_view()),
    path('profile/', ProfileUpdateView.as_view()),

    # Items
    path('', IndexListView.as_view()),
    path('items/<str:pk>/', ItemDetailView.as_view()),
    path('categories/<str:pk>/', CategoryListView.as_view()),
    path('tags/<str:pk>/', TagListView.as_view()),

    # Items(関数バージョン)
    # path('index_func/', index),
    # path('detail_func/<str:pk>/', detail),

    # Order
    path('orders/<str:pk>/', OrderDetailView.as_view()),
    path('orders/', OrderIndexView.as_view()),

    # Cart
    path('cart/', CartListView.as_view()),
    path('cart/add/', AddCartView.as_view()),
    path('cart/remove/<str:pk>', RemoveCartView.as_view()),

    # Cart(removeクラスビュー別バージョン)
    # path('cart/remove', RemoveCartView.as_view()),

    # Cart(remove関数バージョン)
    # path('cart/remove/<str:pk>/', remove_from_cart),

    # Pay
    path('pay/checkout/', PayWithStripe.as_view()),
    path('pay/success/', PaySuccessView.as_view()),
    path('pay/cancel/', PayCancelView.as_view()),

]