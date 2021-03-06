# Generated by Django 2.1.5 on 2019-10-29 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20191027_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_order',
            name='club_chapter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='catalog.Club_Chapter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work_order',
            name='project_title',
            field=models.CharField(default=1, help_text='Enter field documentation', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club_chapter',
            name='total_members',
            field=models.IntegerField(default=3, null=True),
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
