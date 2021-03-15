from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name='plant-home' ),
    path('about/',views.about, name='plant-about' ),
    # path('summary/',views.summary, name ='plant-summary'),
    path('checkout/',views.checkout, name ='plant-checkout'),
    path('product/<int:Product_id>/',views.ProductView, name='product' ),
    # path('summary/',views.add_cart, name='plant-add_cart' ),
    path('cart/',views.show_cart, name='plant-cart' ),
    path('cart/<int:Product_id>',views.add_to_cart, name='plant-add_to_cart' ),
    # path('cart/<int:Product_id>',views.remove_from_cart, name='plant-remove_from_cart' ),

]

