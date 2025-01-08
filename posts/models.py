from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Posts'
        
        
        
class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.voter} voted {self.post}'
    
    class Meta:
        unique_together = ('voter', 'post')