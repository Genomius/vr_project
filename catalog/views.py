# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Product
import simplejson
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse


def catalog(request):
    products = Product.objects.all()

    return render_to_response(
        'catalog.html',
        {
            'products': products,
        }
    )


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    return render_to_response(
        'product.html',
        {
            'product': product,
        }
    )