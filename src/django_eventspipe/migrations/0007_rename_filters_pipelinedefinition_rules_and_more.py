# Generated by Django 5.1.2 on 2024-10-14 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_eventspipe', '0006_alter_pipelineartifact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pipelinedefinition',
            old_name='filters',
            new_name='rules',
        ),
        migrations.RemoveField(
            model_name='pipelinedefinition',
            name='event',
        ),
    ]