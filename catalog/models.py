import django.utils.timezone

from django.db import models
from smartfields import fields

class Foto(models.Model):
    image = fields.ImageField(upload_to='images', blank=True, verbose_name=u'Фотография:')
    name = models.CharField(blank=False, max_length=100, unique=True, verbose_name=u'Имя:')
    text = models.TextField(verbose_name=u'Описание:')
    date_added = models.DateTimeField(default=django.utils.timezone.now, verbose_name=u'Дата публикации:')

    def __str__(self):
        return self.name
