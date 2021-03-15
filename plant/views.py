from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product ,Orderdetail
from carton.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    products = Product.objects.all()
    return render(request,'plant/home.html',{'Products': products})



def about(request):
   return render(request,'plant/about.html')



# def summary(request):
 
#   # orderdetails = Orderdetail.objects.all(){'Orderdetails': orderdetails}
#   return render(request,'plant/summary.html' )
 


def checkout(request):
  return render(request,'plant/checkout.html')


@login_required
def ProductView(request, Product_id):
  selectedProduct = Product.objects.get(id=Product_id)
  Products = Product.objects.all()
  print(selectedProduct)
  return render(request, 'plant/product.html', {'Product': selectedProduct,'Products': Products},)


@login_required
def add_to_cart(request,Product_id):
  cart = Cart(request.session)
  product=Product.objects.get(id=Product_id)
  cart.add(product, product.price)
  

  return HttpResponse("Added")
  


# def remove_from_cart(request, product_id):
#        cart = Cart(request.session)
#     product = Product.objects.get(id=request.GET.get('Product_id'))
#     cart.remove(product)



def show_cart(request):
  cart = Cart(request.session)
  return render(request, 'plant/cart.html', {'cart_items' : cart.items})



# def show(request):
#     return render(request, 'shopping/show-cart.html')
    # print('Fahad', Product_id)
    # order=Orderdetail.objects.all()
    # print('order',list(order))
    # try:
    #     product=Product.objects.get(id=Product_id)
    # except product.DoesNotExist:
    #     pass
    # if product not in order:

    #     order.append(product= product)
    # else:
    #     order.product.remove(product)
    #     print('Fahad 3')
    # return HttpResponseRedirect("product")





