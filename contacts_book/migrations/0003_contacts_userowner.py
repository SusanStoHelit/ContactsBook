# Generated by Django 3.0.4 on 2020-03-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_book', '0002_auto_20200323_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='userowner',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
