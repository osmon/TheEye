# Generated by Django 3.2.3 on 2021-11-11 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_processor', '0006_remove_payloadmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caterogyfieldsmodel',
            old_name='field',
            new_name='field_name',
        ),
        migrations.RemoveField(
            model_name='payloadmodel',
            name='category',
        ),
     
    ]
