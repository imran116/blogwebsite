from django.contrib.auth.models import User
from django.db import models


# menu section start
class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.menu_name


# menu section end

# Slider section start
class Slider(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Slider section end

# Portfolio section start
class Portfolio(models.Model):
    portfolio_image = models.ImageField(upload_to='portfolio_img/')
    portfolio_name = models.CharField(max_length=100)
    portfolio_subtitle = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_latest = models.BooleanField(default=False)

    def __str__(self):
        return self.portfolio_name


# Portfolio section end

# Tag section start
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


# Tag section end

# Category section start
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name


# Category section end
# Blog section start

class Blog(models.Model):
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    blog_image = models.ImageField(upload_to='blog_img/')
    blog_title = models.CharField(max_length=200)
    blog_desc = models.TextField()
    timeStamp = models.DateField(auto_now=True)
    is_draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timeStamp']

    def get_short_desc(self):
        return self.blog_desc[:400]

    def __str__(self):
        return self.blog_title


# Blog section end

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField()
