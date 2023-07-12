from django.shortcuts import render, redirect
from second.models import Post
from .forms import PostForm

# Create your views here.


def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('/second/list/')
    else:
        form = PostForm()
        return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST) # 사용자가 제출한 POST 값을 사용해서 PostForm을 만들어줌
    if form.is_valid(): # 유효성 검사를 해줌
        return render(request, 'second/confirm.html', {'form': form})
    else:
        return redirect('/create/')