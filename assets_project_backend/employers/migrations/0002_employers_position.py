# Generated by Django 5.1.1 on 2024-09-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employers',
            name='position',
            field=models.CharField(default='Inactive', max_length=20),
            preserve_default=False,
        ),
    ]
