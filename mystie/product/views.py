from django.shortcuts import get_object_or_404, render
from .models import Product , Comments
# Create your views here.
from .forms import Buy

def product_list(request):
    products = Product.objects.all()
    
    context = {
        "products" : list(products),
    }
    return render(request,"product/product_list.html",context)

def product_detail(request,id):
    
    selected_product = get_object_or_404(Product,id=id)
    
    AllComments = list(selected_product.comments.all())
    
    if selected_product.available :
        buy_form = Buy(quantity_m = selected_product.number)
    else :
        buy_form = False
    
    context = {
        "s_product" : selected_product ,
        "buy_form1" : buy_form ,
        "s_comments" : AllComments
    }
    return render(request,"product/product_detail.html",context)

