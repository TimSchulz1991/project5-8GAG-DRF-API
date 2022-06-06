from rest_framework import serializers
from .models import Post
from likes.models import Like
from django.contrib.humanize.templatetags.humanize import naturaltime


class TopicSerializerField(serializers.Field):

    VALUE_MAP = {
        'funny': 'Funny',
        'wholesome': 'Wholesome',
        'wtf': 'WTF',
        'cryptocurrency': 'Cryptocurrency',
        'animals': 'Animals',
        'awesome': 'Awesome',
        'gaming': 'Gaming',
        'meme': 'Meme',
        'relationship': 'Relationship'
    }

    def to_representation(self, obj):
        print(obj)
        return self.VALUE_MAP[obj]

    def to_internal_value(self, data):
        print(data)
        return data


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # Add this field, to show the uppercase topic value
    topic = TopicSerializerField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_topic(self, data):
        if (len(data) == 0):
            raise serializers.ValidationError(
                "You must select a topic"
            )
        return data

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                "Image size larger than 2MB!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image too large (larger than 4096px in width)!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image too large (larger than 4096px in height)!"
            )
        return value

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            liked = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return liked.id if liked else None
        return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)

        if self.context['request'].method == 'PUT':
                if 'image' not in self.context['request'].data:
                    self.fields.pop('image')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'image', 'is_owner', 'profile_id', 'profile_image', 'topic',
            'like_id', 'likes_count', 'comments_count'
        ]
        optional_fields = ['image', ]
        extra_kwargs = {'topic': {'required': True}}
