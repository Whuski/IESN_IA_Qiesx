# Generated by Django 2.2.6 on 2019-12-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191209_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_IA',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='size_x',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='game',
            name='size_y',
            field=models.IntegerField(default=4),
        ),
    ]
