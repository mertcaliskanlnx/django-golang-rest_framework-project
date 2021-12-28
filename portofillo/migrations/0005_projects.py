# Generated by Django 3.2 on 2021-12-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0004_remove_goodat_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='portofillo')),
            ],
        ),
    ]
