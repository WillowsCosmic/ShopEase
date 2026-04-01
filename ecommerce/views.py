
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem  

#product listing and category filtering
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })


def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {
        'products': products,
        'category': category
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

#Search and filter products
def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'product_list.html', {'products': products})

#Cart management
@login_required
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price': product.price}   # ✅ FIX
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('view_cart')

@login_required
def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart.objects.get(user=request.user)
    item = CartItem.objects.filter(cart=cart, product=product)

    item.delete()
    return redirect('view_cart')

#Checkout and order management
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    order = Order.objects.create(user=request.user, cart=cart)

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price   # ✅ FIX
        )

    items.delete()

    return redirect('order_list')
#Order History and details
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})


@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    items = order.orderitem_set.all()
    
    # Pre-compute EVERYTHING
    for item in items:
        item.display_subtotal = f"₹{float(item.price * item.quantity):.2f}"
    
    total = sum(item.price * item.quantity for item in items)
    total_display = f"₹{float(total):.2f}"
    
    return render(request, 'order_detail.html', {
        'order': order, 
        'items': items, 
        'total': total_display
    })
#Register, login, logout
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')