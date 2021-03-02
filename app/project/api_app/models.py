from django.db import models


class Games(models.Model):
    title = models.CharField('Название игры', max_length=150)
    cheapest_price = models.PositiveSmallIntegerField('Самая низкая цена', default=0)
    store = models.CharField('Магазин', max_length=150)


    class Meta:
        verbose_name = 'Games'
        verbose_name_plural = 'Games'


