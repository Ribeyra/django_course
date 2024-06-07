from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=200)     # название статьи
    body = models.TextField()                   # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()                # текст комментария
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.article.name} on {self.timestamp}'
