# Generated by Django 3.1.1 on 2020-10-07 16:50

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ("jstocks", "0003_auto_20201002_0241"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="ssn",
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default="", max_length=32, verbose_name="person number")),
        ),
    ]