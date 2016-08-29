# coding: utf-8
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from models import Cart, ProductInCart, Order
import simplejson
from django.views.decorators.csrf import csrf_exempt
from forms import ProductInCartForm, OrderForm
from django.core.mail import send_mail, mail_admins
from vr_project import settings
from django.template.loader import render_to_string


def cart(request):
    if request.session.get("cart_id", False):
        try:
            cart = Cart.objects.get(id=request.session.get("cart_id"))
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id
    else:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id

    if request.method == 'POST':
        return render_to_response(
            'cart.html',
            {
                'cart': cart,
            }
        )
    else:
        return render_to_response(
            'cart.html',
            {
                'cart': cart,
            },
        )


@csrf_exempt
def add(request):
    if request.session.get("cart_id", False):
        try:
            cart = Cart.objects.get(id=request.session.get("cart_id"))
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session["cart_id"] = cart.id
    else:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id

    if request.method == 'POST':
        form = ProductInCartForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            if ProductInCart.objects.filter(product__id=product.id, cart__id=cart.id).exists():
                product_in_cart = ProductInCart.objects.get(product__id=product.id, cart__id=cart.id)
                product_in_cart.quantity += quantity
                quantity = product_in_cart.quantity

                product_in_cart.save()
            else:
                form = form.save(commit=False)
                form.cart = cart
                form.save()
            if request.is_ajax():
                json_dict = {
                    "total_price": cart.total_price(),
                    "products": [{'id': product.id,
                                  'title': product.title,
                                  'price': product.price,
                                  'quantity': quantity,
                                  'cost': product.price * quantity}]
                }
                return HttpResponse(simplejson.dumps(json_dict), content_type="application/json")
            else:
                return HttpResponseRedirect(reverse('cart:cart'))
        else:
            json_dict = {"errors": [(k, v) for k, v in form.errors.items()]}
            return HttpResponse(simplejson.dumps(json_dict), content_type="application/json", status=400)

    else:
        json_dict = {"error": "Only post requests"}
        return HttpResponse(simplejson.dumps(json_dict), content_type="application/json", status=400)


@csrf_exempt
def remove(request):
    pass


@csrf_exempt
def order(request):
    if request.session.get("cart_id", False):
        try:
            cart = Cart.objects.get(id=request.session.get("cart_id"))
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form = order_form.save(commit=False)
            order_form.cart = cart
            order_form.price = cart.total_price()
            order_form.secret = Order.get_random_id()
            order_form.save()

            #TODO: Убрать комментарий после дебага
            #del request.session["cart_id"]
            products_in_cart = ProductInCart.objects.filter(cart=cart.id)

            #TODO: Убрать комментарий после дебага
            #if not settings.DEBUG:
            # Отправляем письмо клиенту с данными о заказе
            if order_form.email:
                message = render_to_string('order_confirmation.txt',
                                           {
                                               'order': order_form,
                                               'products_in_cart': products_in_cart,
                                               'DOMAIN_NAME': settings.DOMAIN_NAME
                                           }
                )
                send_mail(settings.EMAIL_SUBJECT_PREFIX, message, settings.EMAIL_HOST_USER, [order_form.email, ])

            # Отправляем уведомительное письмо админу
            message = render_to_string('admin_order_confirmation.txt',
                                       {
                                           'order': order_form,
                                           'products_in_cart': products_in_cart,
                                           'DOMAIN_NAME': settings.DOMAIN_NAME
                                       }
            )
            mail_admins(settings.EMAIL_SUBJECT_PREFIX, message)

            return HttpResponseRedirect(reverse('cart:thanks', kwargs={'order_id': order_form.id}))
        else:
            return render_to_response(
                'order.html',
                {
                    'cart': cart,
                    'order_form': order_form
                }
            )
    else:
        order_form = OrderForm()

        return render_to_response(
            'order.html',
            {
                'cart': cart,
                'order_form': order_form
            }
        )


#TODO: Убрать @csrf_exempt где не надо
@csrf_exempt
def order_detail(request, secret):
    order = get_object_or_404(Order, secret=secret)
    form = OrderForm(instance=order)
    products_in_cart = ProductInCart.objects.filter(cart=order.cart)

    return render_to_response('order_item.html',
                              {
                                  'order': order,
                                  'form': form,
                                  'products_in_cart': products_in_cart
                              }
    )


def thanks(request, order_id):
    return render_to_response(
        'thanks.html',
        {
            'order': Order.objects.get(id=order_id),
            'DOMAIN_NAME': settings.DOMAIN_NAME
        }
    )