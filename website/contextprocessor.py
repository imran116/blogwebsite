from django.shortcuts import render

from website.models import Portfolio, Menu, Slider


def portfolio_processor(request):
    context = Portfolio.objects.all()
    return {'portfolio_obj': context}


def menu_processor(request):
    context = Menu.objects.filter(is_active=True)
    return {'menu_obj': context}


def slider_processor(request):
    context = Slider.objects.get()
    return {'slider_obj': context}


def latest_gallery_processor(request):
    context = Portfolio.objects.filter(is_active=True, is_latest=True)
    return {'latest_gallery_obj': context}
