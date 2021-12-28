# Generated by Django 3.2 on 2021-12-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0005_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]