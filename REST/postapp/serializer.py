from .models import Post
from rest_framwork import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']
        # 이 필드는 읽기만 가능하게
        read_only_fields = ('titile',)  #tuple로 작성