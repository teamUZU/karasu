from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
