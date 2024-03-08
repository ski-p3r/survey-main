# Generated by Django 5.0.2 on 2024-02-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_question_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='process_group',
            field=models.CharField(blank=True, choices=[('Initiating', 'Initiating'), ('Planning', 'Planning'), ('Executing', 'Executing'), ('M&C', 'M&C'), ('Closing', 'Closing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='stage',
            field=models.CharField(blank=True, choices=[('standardize', 'Standardize'), ('measure', 'Measure'), ('control', 'Control'), ('improve', 'Improve'), ('humanresources', 'Human Resources'), ('cultural', 'Cultural'), ('technological', 'Technological'), ('structural', 'Structural')], max_length=20, null=True),
        ),
    ]
