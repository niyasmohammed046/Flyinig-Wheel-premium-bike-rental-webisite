# Generated by Django 4.1.3 on 2023-01-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyapp', '0008_remove_bikecategory_catimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedata',
            name='PCategory',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]