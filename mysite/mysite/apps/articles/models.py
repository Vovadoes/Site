import datetime
from django.db import models
from django.utils import timezone
from account.models import Profile

class Article(models.Model):
    article_titel = models.CharField('Название статьи', max_length=50)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публиции')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.article_titel

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.TextField('Текст комментрия')
    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
