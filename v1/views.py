from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from core.models import Product
from core.forms import ProductForm
# Create your views here.
def index(request):
    products=Product.objects.order_by("-id")
    return render(request,'pages/index.html',{
        "products":products,
        "page_title":"Home",
        "action_title":"home"
    })

def add_product(request):
    form=ProductForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect("v1:index")
        else:
            messages.error(request, "Error adding product. Please check the form.")
    return render(request,"pages/product_form.html",{
        "form":form,
        "action_title": "Save Product",
        "page_title":"Add Product"
    })

def edit_product(request,id):
    product=get_object_or_404(Product,id=id)
    form=ProductForm(request.POST or None, instance=product)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect("v1:index")
        else:
            messages.error(request, "Error updating product.")
    return render(request,'pages/product_form.html',{
        "form":form,
        "product":product,
        "action_title": "Update Product",
        "page_title":"Update Product"
        })

def delete_product(request,id):
    product=get_object_or_404(Product, id=id)
    if request.method=="POST":
        product.delete() 
        messages.success(request, "Product deleted successfully!")
    return redirect("v1:index")