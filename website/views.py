from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from website import forms
from website.forms import MessageForms
from website.models import Blog, Category


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogPageView(View):

    def get(self, request):
        blog = Blog.objects.filter(is_draft=False)
        recent_blog = Blog.objects.filter(is_draft=False)[:3]
        paginator = Paginator(blog, 3)
        page_number = request.GET.get("page")
        blog_obj = paginator.get_page(page_number)

        category = Category.objects.filter(is_active=True)
        context = {
            'blog_obj': blog_obj,
            'recent_blog_obj': recent_blog,
            'category_obj': category,
        }

        return render(request, 'blog.html', context=context)


def search(request):
    q = request.GET.get('q')

    blog_obj = Blog.objects.filter(
        Q(category__category_name__icontains=q) |
        Q(blog_title__icontains=q) |
        Q(tag__tag_name__contains=q)

    )

    paginator = Paginator(blog_obj, 3)
    page_number = request.GET.get("page")
    blog_obj = paginator.get_page(page_number)
    recent_blog = Blog.objects.filter(is_draft=False)[:3]
    category = Category.objects.filter(is_active=True)
    context = {
        'blog_obj': blog_obj,
        'recent_blog_obj': recent_blog,
        'category_obj': category,
        'query': q,
    }
    return render(request, 'blog.html', context=context)


def blog_detail_view(request, blog_id):
    q = request.GET.get('q')
    blog_obj = Blog.objects.get(id=blog_id)
    blog_timestamp = Blog.objects.all()[:4]
    recent_blog = Blog.objects.filter(is_draft=False)[:3]
    category = Category.objects.filter(is_active=True)
    category_name = Category.objects.get(category_name=q)
    context = {
        'blog_obj': blog_obj,
        'recent_blog_obj': recent_blog,
        'category_obj': category,
        'blog_timestamp': blog_timestamp,
        'category_name': category_name,

    }
    return render(request, 'single-post.html', context=context)

def message_view(request):

    if request.method == 'POST':
        form = forms.MessageForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'index.html')


def about_us_view(request):
    return render(request, 'about.html')
