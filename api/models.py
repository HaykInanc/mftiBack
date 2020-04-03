from django.db import models

class Post(models.Model):
	title	= models.CharField(max_length=30)
	body	= models.TextField()
	likeCnt = models.IntegerField()

	def __str__(self):
		return self.title 

class Comment(models.Model):
	body = models.TextField()
	image = models.ImageField(upload_to ='uploads/comment/', blank=True, null=True)
	post = models.ForeignKey(Post,  related_name="comments", on_delete=models.CASCADE)

	def __str__(self):
		return self.body[:25]+'...'

