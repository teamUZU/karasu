from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('<int:num>', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	# path('signup/', views.signup, name='signup'),
	# path('logout_view/', views.logout_view, name='logout_view'),
	path('about/', views.about, name='about'),
	path('tip_list/', views.tip_list, name='tip_list'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)