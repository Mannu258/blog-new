# Generated by Django 5.0 on 2024-01-05 18:08

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]