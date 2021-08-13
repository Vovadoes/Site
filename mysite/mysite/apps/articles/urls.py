from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('create_aticle', views.create_aticle, name = 'create_aticle'),
]