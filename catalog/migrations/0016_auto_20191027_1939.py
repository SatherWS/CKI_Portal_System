# Generated by Django 2.1.5 on 2019-10-27 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20191027_1834'),
    ]

    operations = [
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
