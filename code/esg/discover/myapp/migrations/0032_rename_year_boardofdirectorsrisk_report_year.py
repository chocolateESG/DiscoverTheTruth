# Generated by Django 4.2.16 on 2024-12-05 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0031_shareholderrisk_investor_communication_risk_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="boardofdirectorsrisk",
            old_name="year",
            new_name="report_year",
        ),
    ]
