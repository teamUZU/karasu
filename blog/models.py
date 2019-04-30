from django.db import models
from django.utils import timezone
from stdimage.models import StdImageField

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=18, blank=True)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	pickup_check = models.BooleanField(default=False)
	image = StdImageField(
		upload_to='image/',
		blank=True,
		variations={
			'large': (600, 400),
			'thumbnail': (400, 300, True),
			# 'medium': (300, 200),
		}
	)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title