import random

from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.cache import cache_page

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product
import os
import json

def get_links_menu():
    if settings.LOW_CACHE:
        key = "links_menu"
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key,links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()

def get_category(pk):
    if settings.LOW_CACHE:
        key = f"category_{pk}"
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key,category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)

def get_hot_product():
    products_list = Product.objects.all()
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_products):
    return Product.objects.filter(category__pk=hot_products.category.pk).exclude(pk=hot_products.pk)[:3]


def main(request):
    # products_main = Product.objects.all()[0:4]
    products_main = Product.objects.filter(is_active=True,category__is_active=True).select_related("category")[:3]
    content = {
        'title': 'Главная',
        "products": products_main,
    }
    return render(request, 'mainapp/index.html', content)

@cache_page(3600)
def products(request, pk=None, page=1):
    links_menu = get_links_menu()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {"name": "Все", "pk": 0}
        else:
            # category = ProductCategory.objects.get(pk=pk)
            category = get_category(pk)
            products_list = Product.objects.filter(category__pk=pk)

        paginator = Paginator(products_list,2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)
        content = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'products': product_paginator,
            'category': category,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'products': same_products,
        'hot_product': hot_product
    }

    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = "Продукт"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.all(),
        "product": get_object_or_404(Product, pk=pk)
    }
    return render(request, "mainapp/product.html", content)


def contact(request):
    file_content = os.path.join(settings.BASE_DIR, "mainapp/json/contacts.json")
    with open(file_content) as fc:
        file_contact = fc.read()
        locations = json.loads(file_contact)
        content = {
            'title': 'Продукты',
            'locations': locations,
        }
        return render(request, 'mainapp/contact.html', content)
