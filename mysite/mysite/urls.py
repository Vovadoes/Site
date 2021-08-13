from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', include('start.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
]
