# Generated by Django 4.2.5 on 2024-04-01 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbooks',
            name='issuedate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='issuedbooks',
            name='returndate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
