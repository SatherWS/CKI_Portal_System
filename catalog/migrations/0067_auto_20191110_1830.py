# Generated by Django 2.1.5 on 2019-11-10 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0066_auto_20191110_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectregistration',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Service_Project', verbose_name='Project'),
        ),
        migrations.AlterField(
            model_name='projectregistration',
            name='service_hrs',
            field=models.TimeField(),
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
