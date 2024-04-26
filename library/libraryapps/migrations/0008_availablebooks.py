# Generated by Django 4.2.5 on 2024-04-09 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapps', '0007_remove_issuedbooks_number_of_days_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availablebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avail_books_authname', to='libraryapps.books')),
                ('bookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapps.books')),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avail_books_name', to='libraryapps.books')),
            ],
        ),
    ]
