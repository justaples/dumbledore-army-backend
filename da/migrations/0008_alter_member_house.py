# Generated by Django 4.1 on 2022-09-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0007_alter_member_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='house',
            field=models.CharField(max_length=20),
        ),
    ]
