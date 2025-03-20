
from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Product, Rating, RatingAnswer, PaymentMethod, Order
from .forms import ProductCreateForm, ProductUpdateForm
from django.contrib import messages
from django.db.models import Avg


def index_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'main/index.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_update_form = ProductUpdateForm(instance=product)
    product_comments = Rating.objects.filter(product=product)

    rating_avg = product_comments.aggregate(Avg('count'))['count__avg']
    similar_products = Product.objects.filter(category=product.category).exclude(id=product_id)

    return render(
        request=request,
        template_name='main/product_details.html',
        context={
            'product': product,
            'similar_products': similar_products,
            'product_update_form': product_update_form,
            'product_comments': product_comments,
            'rating_avg': rating_avg
        }
    )

def product_create_view(request):
    if not request.user.is_authenticated:
        raise Http404()

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():  # <-- Corrected here
            product_object = form.save(commit=False)
            product_object.user = request.user
            product_object.save()

            messages.success(request, "Created")
            return redirect('index')

    form = ProductCreateForm()
    return render(request, 'main/product_create.html', {'form': form})

def product_update_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated and request.user.is_admin:
        if request.method == 'POST':
            form = ProductUpdateForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, "Changed!")
                return redirect('product_details', product_id)

def rating_create_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        count = int(request.POST.get('count', ''))

        rating = Rating(
            user=request.user,
            product=product,
            count=count,
            comment=comment  # Make sure this line is saving the comment
        )

        rating.save()
        print(f"Comment saved: {rating.comment}, {rating.count}")

        messages.success(request, 'Review submitted!')

        return redirect('product_details', product_id)

def rating_answer_create_view(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    if rating.product.user != request.user:
        messages.error(request, "You have no access!")
        return redirect('product_details', rating.product.id)

    if request.method == 'POST':
        comment = request.POST.get('comment', '')

        rating_answer = RatingAnswer(
            user=request.user,
            rating=rating,
            comment=comment
        )

        rating_answer.save()
        messages.success(request, 'Submitted!')
        return redirect('product_details', rating.product.id)

def user_pofile_view(request):
    return render(
        request=request,
        template_name='main/user_profile.html'
    )

def product_payment_create_view(request, product_id, product_quantity):
    product = get_object_or_404(Product, id=product_id)
    seller_payment_methods = PaymentMethod.objects.filter(user=product.user)

    if product_quantity < 1:
        messages.error(request, 'Add quantity')
        return redirect('product_details', product.id)

    if request.method == 'POST':
        check_image = request.FILES.get('check_image', '')
        order = Order(
            user=request.user,
            product=product,
            quantity=product_quantity,
            check_image=check_image
        )
        order.save()
        messages.success(request, 'Payment sent to the seller')
        return redirect('index')

    return render(
        request=request,
        template_name='main/product_payment.html',
        context={
            "seller_payment_methods":seller_payment_methods,
            "product": product,

        }
    )
