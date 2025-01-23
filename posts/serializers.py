from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username') # This will make the poster field read-only
    poster_id = serializers.ReadOnlyField(source='poster.id') # This will make the poster field read-only
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created_at']
        #read_only_fields = ['poster']
        
        
# Vote serializer


class VoteSerializer(serializers.Serializer):
    class Meta:
        fields = ['id']
        