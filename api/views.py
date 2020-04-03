from django.http import HttpResponse
from .models import Post as modelPost, Comment
from .serializer import PostSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

import json

class Post(APIView):

	def get(self, request):
		result = modelPost.objects.all()
		json = PostSerializer(result, many=True)
		return Response({'data': json.data})

	# def post(self, request):

	# 	data = request.body
	# 	newPost =  modelPost(
	# 		title = data['title'],  
	# 		body = data['body'], 
	# 		likeCnt = 0)
	# 	newPost.save()
	# 	return Response()

class addLike(APIView):

	def get(self, request, postId):
		post = modelPost.objects.filter(pk=postId).first()
		post.likeCnt += 1
		post.save()
		return Response({'status': 'ok'})


class addComment(APIView):

	def post(self, request):
		result =  json.loads(request.body.decode('utf-8'))
		newComment = Comment(body=result['text'], 
							 post=modelPost.objects.get(pk=result['post_id']))
		newComment.save()
		return Response({'status': 'ok'})
