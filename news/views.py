from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.order_by("-created_at").all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request):
    news_item = get_object_or_404(News, id=102)
    return render(request, 'news/news_detail.html', {'news': news_item})

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