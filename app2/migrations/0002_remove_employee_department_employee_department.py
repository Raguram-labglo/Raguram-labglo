# Generated by Django 4.1.1 on 2022-09-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ManyToManyField(to='app2.department'),
        ),
    ]
