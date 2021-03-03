from django.db import models


class Games(models.Model):
    title = models.CharField('Название игры', max_length=150)
    game_views = models.PositiveIntegerField('Кол-во просмотров игры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Games'
