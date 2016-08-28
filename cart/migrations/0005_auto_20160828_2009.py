# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20160828_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_mode',
            new_name='payment_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, help_text='\u041d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e, \u043d\u043e \u043c\u044b \u0442\u0443\u0434\u0430 \u043f\u0440\u0438\u0448\u043b\u0435\u043c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0437\u0430\u043a\u0430\u0437\u0435.', max_length=32, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isAgreed',
            field=models.BooleanField(default=False, verbose_name='\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u0430\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isDelivered',
            field=models.BooleanField(default=False, verbose_name='\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isPaid',
            field=models.BooleanField(default=False, verbose_name='\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e'),
        ),
    ]
