# Generated by Django 4.1.7 on 2023-03-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='Mobile',
            field=models.CharField(max_length=100),
        ),
    ]
