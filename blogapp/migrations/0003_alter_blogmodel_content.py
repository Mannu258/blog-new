# Generated by Django 5.0 on 2024-01-05 18:07

import froala_editor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]