# Generated by Django 3.2 on 2021-12-21 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portofillo', '0003_auto_20211221_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodat',
            name='subtitle',
        ),
    ]
