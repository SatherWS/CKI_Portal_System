# Generated by Django 2.1.5 on 2019-11-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0035_auto_20191103_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_order',
            name='club_id',
        ),
        migrations.RemoveField(
            model_name='work_order',
            name='project_title',
        ),
        migrations.RemoveField(
            model_name='work_order',
            name='user_id',
        ),
        migrations.AlterModelOptions(
            name='service_project',
            options={'ordering': ('project_title',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',)},
        ),
        migrations.AddField(
            model_name='user',
            name='working',
            field=models.ManyToManyField(to='catalog.Service_Project'),
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
        migrations.DeleteModel(
            name='work_order',
        ),
    ]
