# Generated by Django 4.0.3 on 2022-04-01 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220401_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
