# Generated by Django 3.2 on 2022-08-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbook',
            name='week',
            field=models.PositiveSmallIntegerField(default=1, unique=True),
        ),
    ]
