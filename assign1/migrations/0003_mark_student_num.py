# Generated by Django 4.1.1 on 2022-09-24 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign1', '0002_student_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='student_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assign1.student'),
        ),
    ]