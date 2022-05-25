from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']