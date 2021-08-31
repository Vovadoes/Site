from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Article
from django.utils import timezone
from .forms import CommentForm, ArticleForm
from account.models import Profile


def index(request):
    articles_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'articles_list': articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(id = request.user.profile.id)
        except:
            return HttpResponse('<h1>Войдите на сайт<h1>')
        a.comment_set.create(author_name=profile.user.username,
                    comment_text=request.POST.get("comment_text"), profile_id=profile.id)
        return HttpResponseRedirect(reverse('articles:detail', args=[article_id]))
    else:
        form = CommentForm()
        latest_comments_list = a.comment_set.order_by('-id')[:10][::-1]
        return render(request, 'articles/detail.html', 
                    {'article': a, 'latest_comments_list': latest_comments_list, 'form': form})


def create_aticle(request):
    try:
        profile = Profile.objects.get(id = request.user.profile.id)
    except:
        return HttpResponse('<h1>Войдите на сайт<h1>')
    if request.method == 'POST':
        article = profile.article_set.create(article_titel=request.POST.get('article_titel'), 
                    article_text=request.POST.get('article_text'), pub_date=timezone.now())
        return HttpResponseRedirect(reverse('articles:detail', args=(article.id,)))
    else:
        form = ArticleForm()
        return render(request, 'articles/create_aticle.html', {'form': form})
