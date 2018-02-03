# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Reviews

# Create your views here.


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def user_inputs(request):
    template_name = 'user_inputs.html'
    context = {}
    return render(request, template_name, context)


def dashboard(request):
    template_name = 'dashboard.html'
    reviews = Reviews.objects.all()
    user_review = []
    user_rating = []
    for obj in reviews:
        user_rating.append(obj.rating)
        user_review.append(obj.review)
    context = {'reviews': user_review, 'ratings': user_rating}
    return render(request, template_name, context)
