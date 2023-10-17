from django.urls import path

from website import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all-blog/', views.BlogPageView.as_view(), name='blog'),
    path('blog-deails/<int:blog_id>/', views.blog_detail_view, name='blog-detail'),
    path('search/', views.search, name='search'),
    path('message/', views.message_view, name='message'),
    path('about-us/', views.about_us_view, name='about-us'),

]
