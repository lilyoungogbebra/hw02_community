from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group



def index(request):
    text = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    text = 'Здесь будет информация о группах проекта Yatube'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/group_list.html', context)
