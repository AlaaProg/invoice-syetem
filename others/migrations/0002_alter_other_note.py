# Generated by Django 4.0.1 on 2022-01-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]