#coding: utf-8
import datetime
import time
from django.db.models import Sum, Count
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name
from catalog.models import Product


class StatisticModule(modules.DashboardModule):
    def is_empty(self):
        return False

    def __init__(self, **kwargs):
        super(StatisticModule, self).__init__(**kwargs)
        self.template = 'admin/statistic_block.html'
        self.css_classes.append('big-block')
        self.column = 3
        self.collapsible = False
        self.total_1 = "NONE1"
        self.total_2 = "NONE2"
        self.total_3 = "NONE2-NONE1"
        self.total_4 = Product.get_sales_count()
        self.total_5 = Product.get_in_stoke_count()

        request = kwargs.get('context').get('request')


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            u'Приложения',
            collapsible=False,
            column=1,
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            u'Пользователь',
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        self.children.append(StatisticModule(title=u"Статистика", context=context))


        # append another link list module for "support".
        self.children.append(modules.LinkList(
            u'Полезные ссылки',
            collapsible=False,
            column=2,
            children=[
                {
                    'title': u'Google cardboard на Alliexpress',
                    'url': 'https://ru.aliexpress.com/item/Google-Cardboard-3d-Glasses-Virtual-Reality-Glasses-Vr-Box-DIY-Google-Vr-Cardboard-3d-Glass-For/32648336472.html?spm=2114.30010708.3.20.ASTERi&ws_ab_test=searchweb201556_0,searchweb201602_3_10039_10048_10057_10047_10056_10065_10055_10054_10059_10046_10058_10045_10017_107_10060_10061_10052_414_10062_10053_10050_10051,searchweb201603_2&btsid=9198cc60-0a67-4569-9d33-d7d80ba9e15f',
                    'external': True,
                },
                {
                    'title': u'VR BOX 1.0 на Alliexpress',
                    'url': 'https://ru.aliexpress.com/item/VR-Box-3d-glasses-for-mobile-Virtual-Reality-Headset-Head-Mount-Goggles-Oculus-Rift-Google-Cardboard/32673135081.html?spm=2114.30010708.3.1.dcAJTO&ws_ab_test=searchweb201556_0,searchweb201602_3_10039_10048_10057_10047_10056_10065_10055_10054_10059_10046_10058_10045_10017_107_10060_10061_10052_414_10062_10053_10050_10051,searchweb201603_2&btsid=9198cc60-0a67-4569-9d33-d7d80ba9e15f',
                    'external': True,
                },
                {
                    'title': u'Google Cardboard Official Site',
                    'url': 'https://vr.google.com/cardboard/get-cardboard/',
                    'external': True,
                },
                {
                    'title': u'Описание очков',
                    'url': 'https://vc.ru/p/vrglass-review',
                    'external': True,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            u'Последние заказы',
            collapsible=False,
            column=2,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _(u'Последние действия'),
            limit=5,
            collapsible=False,
            column=2,
        ))

