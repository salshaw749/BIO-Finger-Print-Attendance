# Generated by Django 2.2.3 on 2019-07-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingerPrint', '0003_auto_20190728_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout1',
            name='date',
            field=models.DateTimeField(),
        ),
    ]