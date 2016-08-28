# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Main(models.Model):
    spent_money = models.IntegerField(u'Потраченные деньги', default=0)
    earned_money = models.IntegerField(u'Заработанные деньги', default=0)
    sold_all = models.IntegerField(u'Продано всего', default=0)

    class Meta:
        verbose_name = u'основная информация'
        verbose_name_plural = u'Основная информация'