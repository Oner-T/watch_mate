# Generated by Django 4.1 on 2023-03-26 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_watchlist_avg_rating_watchlist_number_raitng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='number_raitng',
            new_name='number_rating',
        ),
    ]
