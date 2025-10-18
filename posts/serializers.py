from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'content', 'created_at', 'updated_at')
        read_only_fields = ('author',)

    def create(self, validated_data):
        # Automatically assign the author to the post
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
