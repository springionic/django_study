# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 28, 8, 36, 8, 637217, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
