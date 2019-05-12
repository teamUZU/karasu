from django import forms
from django.contrib.auth.forms import UserCreationForm # 新規会員登録でインポート文追記
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

# 新規会員登録でUserCreateFormクラス追記
class UserCreateForm(UserCreationForm):
	username = forms.CharField()
	email = forms.EmailField()
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)