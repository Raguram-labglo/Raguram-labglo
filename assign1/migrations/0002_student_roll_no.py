# Generated by Django 4.1.1 on 2022-09-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(default=80),
            preserve_default=False,
        ),
    ]
