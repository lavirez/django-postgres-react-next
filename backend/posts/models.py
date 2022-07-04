from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=128)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.title