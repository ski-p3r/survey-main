# Generated by Django 5.0.2 on 2024-03-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_question_process_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='private',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
