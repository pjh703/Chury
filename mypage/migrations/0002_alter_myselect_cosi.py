# Generated by Django 4.1.1 on 2023-03-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mypage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myselect",
            name="cosi",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
