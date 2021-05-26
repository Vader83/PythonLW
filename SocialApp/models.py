from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	subject = models.CharField(max_length = 256)
	text = models.TextField()

	def __str__(self):
		return self.subject

class Comment(models.Model):
	id = models.AutoField(primary_key = True)
	news = models.ForeignKey(News, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	comment = models.TextField()

	def __str__(self):
		return self.user
