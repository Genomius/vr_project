# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
import simplejson
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse


def main(request):
    return render_to_response(
        'main.html',
        {

        },
    )

