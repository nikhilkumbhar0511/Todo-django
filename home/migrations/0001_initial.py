# Generated by Django 3.0.5 on 2021-08-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddTask', models.CharField(max_length=30)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
