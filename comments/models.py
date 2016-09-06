# coding: utf-8
from __future__ import unicode_literals
from django.db import models


RATING = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5
}


class Comment(models.Model):
    message = models.TextField(u'Сообщение', max_length=4096, help_text=u'Введите Ваш отзыв здесь')
    name = models.CharField(u'Имя', max_length=64, help_text=u'Введите свое имя')
    email = models.CharField(u'Email', max_length=64, help_text=u'Введите свой email')
    rating = models.IntegerField(u'Оценка')
    slug = models.SlugField(u'URL', unique=True)
    add_date = models.DateTimeField(u'Дата добавления', auto_now_add=True)

    def __unicode__(self):
        return self.add_date

    class Meta:
        verbose_name = u'комментарии'
        verbose_name_plural = u'Комментарий'