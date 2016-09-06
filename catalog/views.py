# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Product, get_max_price, get_min_price
import simplejson
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string


def catalog(request):
    if request.POST:
        if request.is_ajax():
            products = Product.objects.filter(price__lte=request.session['max_price'], price__gte=request.session['min_price'])
            data = render_to_string('catalog.ajax.html', {'products': products})
            return JsonResponse({'status': 200, 'result': data})
    else:
        products = Product.objects.all()

        return render_to_response(
            'catalog.html',
            {
                'products': products,
                'max_price': get_max_price,
                'min_price': get_min_price,
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