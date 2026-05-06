from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    now = timezone.now()
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=now,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    now = timezone.now()
    post = get_object_or_404(Post, id=id, is_published=True,
                             pub_date__lte=now, category__is_published=True)
    context = {'post': post}
    print(f"Передаём в шаблон post: {post},"
          f" type: {type(post)}")
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    now = timezone.now()
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = (Post.objects.filter(category=category,
                 is_published=True, pub_date__lte=now)
                 .order_by('-pub_date'))
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
