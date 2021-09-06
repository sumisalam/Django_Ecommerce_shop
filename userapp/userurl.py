from django.urls import path
from .import views

urlpatterns=[ path('',views.index,name="index"),
              path('log',views.signin,name="signin"),
              path('reg',views.signup,name="signup"),
              path('client',views.client,name="client"),
              path('vegetables',views.vegetables,name="vegetables"),
              path('cart/<id>',views.cart,name="cart"),
              path('orde/<id>',views.orde,name="orde"),
              path('myorders',views.myorders,name='myorders'),
              path('mycart',views.mycarts,name="mycarts"),
              path('order',views.order,name="order"),
              path('payment',views.payment,name="payment"),
              path('pay',views.pay,name="pay"),
              path('remove/<id>',views.remove,name="remove"),
              path('logout',views.log,name="logout")


]