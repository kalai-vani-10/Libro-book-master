# Generated by Django 4.2.5 on 2024-04-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapps', '0011_alter_issuedbooks_authorname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedBooks',
            fields=[
                ('bookID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=50)),
                ('authorname', models.CharField(max_length=50)),
            ],
        ),
    ]
