# Generated by Django 2.1.5 on 2019-11-15 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0078_auto_20191114_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectregistration',
            name='chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.Club_Chapter', verbose_name='Club'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectregistration',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Service_Project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='projectregistration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Worker'),
        ),
        migrations.AlterField(
            model_name='service_project',
            name='club_chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Club_Chapter'),
        ),
        migrations.AlterField(
            model_name='user',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Club_Chapter'),
        ),
    ]
