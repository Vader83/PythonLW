from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key = True)
	firstName = models.CharField(max_length = 256)
	lastName = models.CharField(max_length = 256)
	password = models.CharField(max_length = 256)
	email = models.EmailField(max_length = 254, unique = True)

class News(models.Model):
	id = models.AutoField(primary_key = True)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	subject = models.CharField(max_length = 256)
	text = models.TextField()