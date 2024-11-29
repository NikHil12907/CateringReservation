from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Order, ProductForm, UserProfile, UserProfileForm, OrderItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'theme/base.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'catering/manage_products.html', {'products': products})

@user_passes_test(is_admin)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('manage_products')
    else:
        form = ProductForm()
    return render(request, 'catering/add_edit_product.html', {'form': form, 'action': 'Add'})

@user_passes_test(is_admin)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            redirect('manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catering/add_edit_product.html', {'form': form, 'action': 'Edit'})

@user_passes_test(is_admin)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('manage_products')
    return render(request, 'catering/delete_product.html', {'product':product})    

#list produced by admin
def product_list(request):
    query = request.GET.get('search','')
    category = request.GET.get('category','')
    products = Product.objects.all()
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if category:
        products = products.filter(category__iexact=category)
    
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'catering/product_list.html', {'products': products, 'categories': categories})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})


def product_detail(request, product_id):
    product =  get_object_or_404(Product, id=product_id)
    return render(request, 'catering/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return render(request, 'ErrorPages/not_logged_in.html')
    
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('product_list')

@login_required
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = Cart.objects.filter(user=request.user)
    cart_data = [{
        'id': item.id,
        'product': item.product,
        'quantity':item.quantity,
        'price':item.product.price,
        'total':item.product.price * item.quantity    
    }
    for item in cart_items
    ]
    total_price = sum(item['total'] for item in cart_data)
    return render(request, 'catering/cart.html', {'cart_items': cart_data, 'total_price': total_price})

def update_cart(request, cart_id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('cart')

def delete_cart(request, cart_id):
    if request.method == "POST":
        cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
        cart_item.delete()
    return redirect('cart')

def checkout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=total_price)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product= item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect('order_history')
    
    return render(request, 'catering/checkout.html', {'cart_items':[{'product': item.product, 'quantity':item.quantity, 'total': item.product.price * item.quantity} for item in cart_items ], 'total_price': total_price})

def order_history_view(request):
    if not request.user.is_authenticated:
        redirect('login')
    
    order = Order.objects.filter(user=request.user)
    return render(request, 'catering/order_history.html', {'orders': order})

@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'User_profile/profile.html', {'profile':profile})

@login_required
def profile_edit(request):
    profile = get_object_or_404(UserProfile,  user=request.user)
    
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid:
            form.save()
            redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'User_profile/profile_edit.html', {'form':form, 'profile': profile })    

    