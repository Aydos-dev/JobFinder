from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):

    class Meta:
        fields = ('author',
                  'id',
                  'title',
                  'body',
                  'created_at',
                  'phone',
                  'price',
                  'category',

        )
        model = Post