# Generated by Django 4.2.7 on 2023-11-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=240, verbose_name='Name')),
                ('last_name', models.CharField(max_length=240, verbose_name='Last Name')),
                ('first_name', models.CharField(max_length=240, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=240, verbose_name='Middle Name')),
            ],
        ),
    ]
