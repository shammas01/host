# Generated by Django 4.2 on 2023-05-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_pricingplan_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]