# Generated by Django 4.2.3 on 2023-07-16 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_academiccalendar_desc_alter_feestructure_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academiccalendar',
            old_name='desc',
            new_name='note',
        ),
    ]