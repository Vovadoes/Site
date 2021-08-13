from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ["article_titel", "article_text"]
        required = {
            'article_titel' : False,
            'article_text': False
        }
        widgets = {
            'article_titel': forms.TextInput(attrs=
            {
                "required placeholder":"Название статьи"
            }),
            'article_text': forms.Textarea(attrs=
            {
                "required placeholder":"Текст статьи"
            })
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['comment_text']
        required = {
            'comment_text': False
        }
        widgets = {
            'comment_text': forms.Textarea(attrs=
            {
                "required placeholder":"Текст комментария"
            })
        }
        