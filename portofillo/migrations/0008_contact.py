# Generated by Django 3.2 on 2021-12-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0007_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=244)),
                ('message', models.TextField()),
            ],
        ),
    ]
