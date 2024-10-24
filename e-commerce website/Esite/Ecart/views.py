from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from Ecart.models import ProductCategory,ProductSubCategory,Product,shipping_address
from Ecart.forms import shipping_forms_from_model
from math import ceil
from django.core.mail import send_mail

# Create your views here.

def test(request):
    
    return render(request,"layout.html")

    #return HttpResponse("hey")
    
def home(request):
    database_product = ProductCategory.objects.all()  # Retrieve all products from the database
    n = len(database_product)
    logic_slide = n // 4 + ceil((n / 4) - n // 4)  # Logic to calculate number of slides

    # Splitting products into chunks of 4 for each slide
    products_chunks = [database_product[i:i+4] for i in range(0, n, 4)]

    product_dict = {
        "display_product": products_chunks,  # Chunked product list
        "number_of_slide": logic_slide,
        "range": range(logic_slide),
    }
    
    return render(request, "home.html", {"data": product_dict})

'''
def home(request):
    
    database_product = Product.objects.all()
    n = len(database_product)
    logic_slide = n//4 + ceil((n/4) - n//4) 
    
    product_dict = {
        "display_product" : database_product,
        "number_of_slide" : logic_slide,
        "range" : range(number_of_slide)
        
    }
    return render(request,"home.html",{"data":product_dict})

'''
def about(request):
    return render(request,"about.html")


def contact(request):
    pass


def tracker(request):
    pass


def search(request):
    pass


def productview_category(request,prd_category):
    
    category = get_object_or_404(ProductCategory,product_category_name=prd_category)
    
    productsubcategory_according_category = ProductSubCategory.objects.filter(product_category=category)
    product_according_category = Product.objects.filter(product_category=category)
    
    
    product_category_wise_dict = {
        "p_sub" : productsubcategory_according_category,
        "p_cate" : product_according_category
    }
    
    return render(request,"productviews.html",product_category_wise_dict) 

def productview_SUB_category(request,prd_subcategory):
    Product_subcategory = get_object_or_404(ProductSubCategory,product_sub_category_name=prd_subcategory)
    
    product_according_subcategories = Product.objects.filter(product_sub_category = Product_subcategory)
    
    
    product_subcategory_wise_dict = {
        "product_sub_wise" : product_according_subcategories
    }
    
    return render(request , "productviewaccordingtosubcategory.html",product_subcategory_wise_dict)

'''
def productdetails_page(request,product_id):
    
    Product_details = Product.objects.filter(id = product_id)
    
    product_details_dict = {
        "product_detail" : Product_details
    }
    
    return render(request , "productdetails.html",product_details_dict)


def confirmation_page(request,product_id):
    order_details = Product.objects.filter(id = product_id)
    
    if request.method == "POST":
        product_count = request.POST.get("total_number_of_product")
        total_product_count =int(product_count)
        
        final_order_details_dict = {
        'final_order_detail' : order_details,
        'final_order_total' : total_product_count
    }
        
        return render(request,"order.html",final_order_details_dict)
        
        
    
    order_details_dict = {
        'order_detail' : order_details
    }
    
    return render(request , "confirmation.html" , order_details_dict)
'''

def productdetails_page(request, product_id):
    # Get the product details for a specific product
    product_detail = get_object_or_404(Product, id=product_id)
    
    product_details_dict = {
        "product_detail": product_detail
    }
    
    return render(request, "productdetails.html", product_details_dict)


def confirmation_page(request, product_id):
    # Get the product detail for the specific order
    order_detail = get_object_or_404(Product, id=product_id)
    order_price = float(order_detail.product_price)
    total_product_count = 1
    
    
    shipping_address_of_user = shipping_address.objects.all().first()
    
    if request.method == "POST":
        product_count = request.POST.get("total_number_of_product")
        total_product_count = int(product_count) if product_count else total_product_count
    
      ######
        
        if shipping_address_of_user:
            add = True
            form = shipping_address_of_user
        else:
            add = False
            form = shipping_forms_from_model()
       
       # for add new address      
        if "add_address" in request.POST:
            form = shipping_forms_from_model(request.POST)
            if form.is_valid():
                form.save()
                return redirect('confirmation_page',product_id=product_id) 
                 
        product_cost = total_product_count * order_price
        
        final_order_details_dict = {
            'final_order_detail': order_detail,  # Pass a single product object
            'final_order_total': total_product_count,
            'final_cost' : product_cost,
            'final_shipping_address' : form,
            'add' : add
        }
        
        return render(request, "order.html", final_order_details_dict)
    
    # For GET requests, display the order detail
    order_details_dict = {
        'order_detail': order_detail  # Pass a single product object
    }
    return render(request, "confirmation.html", order_details_dict)


def done(request,product_id):
    
    product_name = Product.objects.get(id=product_id)
    address = shipping_address.objects.all().first()
    
    send_mail(
    "Thanks for buying from E-Mart",  # Fixed typo in subject
    f"Your product will be delivered within 3 days. Your product name is {product_name.product_name}.",  # Adjusted message
    "emailsend587@gmail.com",  # Make sure this email is configured in your settings
    [address.Contact_Person_Email],  # Ensure this field is correct
    fail_silently=False,
)
    
    done_dict = {
        'product' : product_name,
        "address" : address
    }
    
    return render(request,"done.html",done_dict)


def shipping_add_order_displayed(request):
    
    return render(request, "order.html")


def shipping_fillup(request):
    
    if request.method == "POST":
        form = shipping_forms_from_model(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('productdetails_page')
    else:
        form = shipping_forms_from_model()        
    return render(request,"shipping_address.html",{"form":form})

def shipping_add_edit(request,product_id):
    
    old_shipping_add = shipping_address.objects.all().first()
    if request.method == "POST":
        
        form = shipping_forms_from_model(request.POST,instance=old_shipping_add)
        if form.is_valid():
            form.save()
            return redirect("confirmation_page",product_id=product_id)
    else:
        form = shipping_forms_from_model(instance=old_shipping_add)
        
    edit_add_dict = {
            'form':form,
            "product_id":product_id
        }
        
    return render(request,"shipping_address_edit.html",edit_add_dict)













