from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner'
    """
    topic_choices = [
        ('funny', 'Funny'),
        ('wholesome', 'Wholesome'),
        ('wtf', 'WTF'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('animals', 'Animals'),
        ('awesome', 'Awesome'),
        ('gaming', 'Gaming'),
        ('meme', 'Meme'),
        ('relationship', 'Relationship')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    # content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/'
        # , default='../default_post_qdg53d', blank=True
    )
    topic = models.CharField(max_length=32, choices=topic_choices)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
