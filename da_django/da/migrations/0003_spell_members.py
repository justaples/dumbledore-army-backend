# Generated by Django 4.1 on 2022-09-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0002_rename_spells_spell'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='members',
            field=models.ManyToManyField(to='da.member'),
        ),
    ]
