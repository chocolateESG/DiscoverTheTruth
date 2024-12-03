# Generated by Django 4.2.16 on 2024-12-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_alter_companygovernance_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shareholder",
            name="top_10_shareholders",
            field=models.URLField(blank=True, null=True, verbose_name="前10大股東持股情況"),
        ),
    ]
