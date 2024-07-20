# Generated by Django 4.1 on 2022-08-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=60, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Info',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
