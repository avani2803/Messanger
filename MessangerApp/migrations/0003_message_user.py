# Generated by Django 3.0.6 on 2021-08-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessangerApp', '0002_message_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
