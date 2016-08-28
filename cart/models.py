# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Cart(models.Model):
    add_date = models.DateTimeField(u'Время добавления')

    def __unicode__(self):
        return self.add_date

    