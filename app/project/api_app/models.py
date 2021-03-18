from django.db import models


class Games(models.Model):
    """ Таблица игр """
    title = models.CharField('Название игры', max_length=150)
    game_views = models.PositiveIntegerField('Кол-во просмотров игры', default=0)
    game_id = models.PositiveIntegerField('ID игры', default=0)
    internalName = models.CharField('internalName', max_length=200)
    image_link = models.URLField('Image link', max_length=600, default='')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Games'


