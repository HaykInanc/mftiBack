from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'body', 'image']


class PostSerializer(serializers.ModelSerializer):
    
    comments =  CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ['pk', 'title', 'body', 'likeCnt', 'comments']