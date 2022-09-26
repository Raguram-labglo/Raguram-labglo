# Generated by Django 4.1.1 on 2022-09-24 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_remove_employee_department_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app2.posting'),
        ),
    ]
