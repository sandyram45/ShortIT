# Generated by Django 4.0.4 on 2022-04-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShortIt', '0002_urlentry_shortened_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlentry',
            name='shortened_url',
            field=models.CharField(max_length=6),
        ),
    ]
