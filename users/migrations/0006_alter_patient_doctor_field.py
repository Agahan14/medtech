# Generated by Django 3.2 on 2022-08-20 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220818_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='users.doctor'),
        ),
    ]
