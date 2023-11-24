from django.shortcuts import render
from .models import Category,Product
from django.shortcuts import get_object_or_404
import random
from . import ml_popular,ml_content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def product_info(request,product_slug):
    content_slug = ml_content.get_recommendations(slug=product_slug).tolist()
    recc_products = Product.objects.filter(slug__in=content_slug)
    product = get_object_or_404(Product,slug=product_slug)
    context = {'product': product,'content_product':recc_products}
    return render(request, 'store/product-info.html',context=context)



def store(request):
    all_products= Product.objects.all()
    my_titles= ml_popular.popular_products()['title'].tolist()
    pop_prodcts= Product.objects.filter(title__in=my_titles)
    shuffled_products = random.sample(list(all_products),4)
    context = {'my_products': shuffled_products}
    return render(request,'store/store.html',context=context)

def all(request):
    all_products =Product.objects.all()
    paginator = Paginator(all_products, 50)  # Show 50 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {'products': products}
    return render(request,'store/all.html',context=context)

def categories(request):
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}




def list_category(request,category_slug=None):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html',{'category': category,'products':products})
