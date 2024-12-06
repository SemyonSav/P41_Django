from django.db import models


class Example(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пример"
        verbose_name_plural = "примеры"