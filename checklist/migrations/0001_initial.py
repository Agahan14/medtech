# Generated by Django 4.0.2 on 2022-07-08 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0011_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('is_ok', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='MedCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('answer', models.ManyToManyField(to='checklist.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('med_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.medcard')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.question'),
        ),
    ]
