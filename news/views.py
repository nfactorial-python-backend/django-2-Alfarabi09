from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment
from .forms import NewsForm, CommentForm

def news_list(request):
    news = News.objects.order_by("-created_at").all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    comments = news_item.comments.order_by('-created_at').all()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.save()
            return redirect('news_detail', news_id=news_item.id)
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {'news': news_item, 'comments': comments, 'form': form})

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', {'form': form})