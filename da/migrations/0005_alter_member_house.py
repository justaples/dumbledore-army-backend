# Generated by Django 4.1 on 2022-09-08 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0004_alter_spell_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='house',
            field=models.CharField(choices=[('Gryffindor', 'Gryffindor'), ('Ravenclaw', 'Ravenclaw'), ('Hufflepuff', 'Hufflepuff'), ('Slytherin', 'Slytherin')], default='Choose your house', max_length=20),
        ),
    ]
