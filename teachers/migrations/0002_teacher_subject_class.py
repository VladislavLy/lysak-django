# Generated by Django 3.2.6 on 2021-09-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject_class',
            field=models.CharField(max_length=100),
        ),
    ]