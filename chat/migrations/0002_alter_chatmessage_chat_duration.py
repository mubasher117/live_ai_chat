# Generated by Django 4.2 on 2023-04-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='chat_duration',
            field=models.FloatField(null=True),
        ),
    ]