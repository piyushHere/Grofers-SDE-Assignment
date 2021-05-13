# Generated by Django 2.2.5 on 2021-05-13 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lucky_draw', '0002_auto_20210513_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='event_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='name', max_length=30, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]