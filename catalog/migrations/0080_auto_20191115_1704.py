# Generated by Django 2.1.5 on 2019-11-15 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0079_auto_20191115_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectregistration',
            name='chapter',
        ),
        migrations.AlterField(
            model_name='projectregistration',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Service_Project', verbose_name='Project'),
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
