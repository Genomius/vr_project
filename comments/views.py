# coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Comment
import simplejson
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse


def comment(request):
    comments = Comment.objects.all()

    return render_to_response(
        'comments.html',
        {
            'comment': comment,
        }
    )
