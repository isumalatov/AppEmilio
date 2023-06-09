# Generated by Django 4.2.1 on 2023-05-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_address_address_alter_creditcard_card_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='expiration_data',
            new_name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='addresses',
            field=models.ManyToManyField(to='usuarios.address'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='credit_cards',
            field=models.ManyToManyField(to='usuarios.creditcard'),
        ),
    ]
