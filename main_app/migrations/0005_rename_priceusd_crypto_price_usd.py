# Generated by Django 5.2.3 on 2025-07-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_crypto_alter_transaction_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='priceusd',
            new_name='price_usd',
        ),
    ]
