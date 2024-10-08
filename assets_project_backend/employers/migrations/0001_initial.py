# Generated by Django 5.1.1 on 2024-09-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('personal_no', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('phone_number_1', models.CharField(max_length=15)),
                ('address_1', models.CharField(max_length=255)),
                ('postal_code_1', models.CharField(max_length=10)),
                ('phone_number_2', models.CharField(blank=True, max_length=15, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
