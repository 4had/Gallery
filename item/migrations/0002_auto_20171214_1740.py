# Generated by Django 2.0 on 2017-12-14 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemimage',
            options={'verbose_name': "Item's image", 'verbose_name_plural': 'Images'},
        ),
    ]
