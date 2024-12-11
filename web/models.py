from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
