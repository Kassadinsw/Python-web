# Generated by Django 2.1.3 on 2018-11-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_goods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='time',
        ),
        migrations.AddField(
            model_name='goods',
            name='keyword',
            field=models.CharField(default='', max_length=50),
        ),
    ]
