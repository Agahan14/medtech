# Generated by Django 3.2 on 2022-08-08 13:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'System user',
                'verbose_name_plural': 'System users',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('resign', models.TextField()),
                ('education', models.TextField()),
                ('professional_sphere', models.TextField()),
                ('work_experience', models.TextField()),
                ('achievements', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='OfficeManager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.user')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('date_of_pregnancy', models.DateField(blank=True, null=True)),
                ('inn', models.CharField(max_length=14, unique=True)),
                ('doctor_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='users.doctor')),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
