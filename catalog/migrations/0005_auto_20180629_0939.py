# Generated by Django 2.0.6 on 2018-06-29 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180628_0057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('book_edit', 'Edit Book fields'),)},
        ),
    ]