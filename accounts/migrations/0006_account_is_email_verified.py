# Generated by Django 4.0 on 2022-08-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
